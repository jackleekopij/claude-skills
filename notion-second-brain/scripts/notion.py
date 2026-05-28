#!/usr/bin/env python3
"""
Notion Second Brain CLI
Reads NOTION_TOKEN from environment or ~/.notion_token.

Usage:
  notion.py list-projects
  notion.py list-topics
  notion.py list-areas
  notion.py search "query" [--db notes|tasks|journal|all]
  notion.py read-page <page-id>
  notion.py add-note "Title" [--project-id ID ...] [--topic-id ID ...] [--content "text"] [--due YYYY-MM-DD]
  notion.py add-task "Title" [--project-id ID] [--horizon "Today"] [--work-style "Deep Work"] [--due YYYY-MM-DD]
  notion.py add-journal "Title" [--journal-type "Daily"] [--mood "Good"] [--energy "High"] [--content "text"]
  notion.py upload-md "Title" /path/to/file.md [--project-id ID ...] [--topic-id ID ...]
  notion.py archive <page-id>

IDs for Projects, Topics etc. come from list-projects / list-topics output.
Multiple --project-id or --topic-id flags are supported for notes.
"""

import os, sys, json, time, urllib.request, urllib.error, argparse, re
from datetime import datetime

TOKEN = os.environ.get('NOTION_TOKEN') or open(os.path.expanduser('~/.notion_token')).read().strip()
BASE = 'https://api.notion.com/v1'
HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

# --- Database IDs (Kyle Saltmarsh's Notion Second Brain) ---
DB = {
    'notes':    '1f7fa8e2-920b-81a8-9522-cbe0f406e9ad',
    'projects': '1f7fa8e2-920b-815c-8048-fcfaca0a10b8',
    'topics':   '1f7fa8e2-920b-81bd-93c9-ed9c9957a487',
    'tasks':    '1f3fa8e2-920b-808e-9b74-f023a477d541',
    'journal':  '1f4fa8e2-920b-814a-86d2-ed04dc37a029',
    'areas':    '21afa8e2-920b-8014-b156-ea987d6a2b00',
}


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def _request(method, path, body=None, retries=15, delay=3):
    url = BASE + path
    data = json.dumps(body).encode() if body else None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, data=data, headers=HEADERS, method=method)
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            body_text = e.read().decode()
            print(f'HTTP {e.code}: {body_text}', file=sys.stderr)
            sys.exit(1)
        except (urllib.error.URLError, OSError) as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                print(f'ERROR: request failed after {retries} attempts: {e}', file=sys.stderr)
                sys.exit(1)


def get(path): return _request('GET', path)
def post(path, body): return _request('POST', path, body)
def patch(path, body): return _request('PATCH', path, body)


# ---------------------------------------------------------------------------
# Database queries
# ---------------------------------------------------------------------------

def query_db(db_id, filter_body=None, sorts=None):
    body = {'page_size': 100}
    if filter_body:
        body['filter'] = filter_body
    if sorts:
        body['sorts'] = sorts
    result = post(f'/databases/{db_id}/query', body)
    return result.get('results', [])


def page_title(page):
    props = page.get('properties', {})
    for key in ('Name', 'Title', 'title'):
        prop = props.get(key, {})
        if isinstance(prop, dict):
            rich = prop.get('title', prop.get('rich_text', []))
            if rich:
                return ''.join(r.get('plain_text', '') for r in rich)
    return '(untitled)'


# ---------------------------------------------------------------------------
# List commands
# ---------------------------------------------------------------------------

def cmd_list_projects():
    rows = query_db(DB['projects'], sorts=[{'property': 'Name', 'direction': 'ascending'}])
    print(f'{"ID":<40}  {"Name"}')
    print('-' * 70)
    for r in rows:
        archived = r.get('properties', {}).get('Archive', {}).get('checkbox', False)
        if not archived:
            print(f'{r["id"]}  {page_title(r)}')


def cmd_list_topics():
    rows = query_db(DB['topics'], sorts=[{'property': 'Name', 'direction': 'ascending'}])
    print(f'{"ID":<40}  {"Name"}')
    print('-' * 70)
    for r in rows:
        archived = r.get('properties', {}).get('Archive', {}).get('checkbox', False)
        if not archived:
            print(f'{r["id"]}  {page_title(r)}')


def cmd_list_areas():
    rows = query_db(DB['areas'], sorts=[{'property': 'Name', 'direction': 'ascending'}])
    print(f'{"ID":<40}  {"Name"}')
    print('-' * 70)
    for r in rows:
        print(f'{r["id"]}  {page_title(r)}')


# ---------------------------------------------------------------------------
# Search command
# ---------------------------------------------------------------------------

def cmd_search(query, db_name='all'):
    """Search pages by title across one or all databases."""
    targets = {}
    if db_name == 'all':
        targets = {'notes': DB['notes'], 'tasks': DB['tasks'], 'journal': DB['journal']}
    elif db_name in DB:
        targets = {db_name: DB[db_name]}
    else:
        print(f'Unknown database: {db_name}')
        sys.exit(1)

    found = False
    for name, db_id in targets.items():
        filt = {'property': 'Name', 'title': {'contains': query}}
        rows = query_db(db_id, filter_body=filt)
        if rows:
            found = True
            print(f'--- {name} ({len(rows)} results) ---')
            print(f'{"ID":<40}  {"Name"}')
            for r in rows:
                print(f'{r["id"]}  {page_title(r)}')
            print()
    if not found:
        print(f'No pages found matching "{query}"')


# ---------------------------------------------------------------------------
# Read page content
# ---------------------------------------------------------------------------

def cmd_read_page(page_id):
    """Read the full content of a Notion page as plain text."""
    # First get the page title
    page = get(f'/pages/{page_id}')
    title = page_title(page)
    print(f'# {title}')
    print()

    # Then read all child blocks (paginated)
    has_more = True
    cursor = None
    while has_more:
        path = f'/blocks/{page_id}/children?page_size=100'
        if cursor:
            path += f'&start_cursor={cursor}'
        result = get(path)
        for block in result.get('results', []):
            btype = block.get('type', '')
            content = block.get(btype, {})
            texts = content.get('rich_text', [])
            prefix = ''
            if 'heading_1' == btype:
                prefix = '# '
            elif 'heading_2' == btype:
                prefix = '## '
            elif 'heading_3' == btype:
                prefix = '### '
            elif btype == 'bulleted_list_item':
                prefix = '- '
            elif btype == 'numbered_list_item':
                prefix = '1. '
            elif btype == 'to_do':
                checked = content.get('checked', False)
                prefix = '[x] ' if checked else '[ ] '
            elif btype == 'quote':
                prefix = '> '
            elif btype == 'code':
                lang = content.get('language', '')
                code_text = ''.join(t.get('plain_text', '') for t in texts)
                print(f'```{lang}')
                print(code_text)
                print('```')
                continue
            elif btype == 'divider':
                print('---')
                continue
            elif btype == 'image':
                img = content.get('file', content.get('external', {}))
                url = img.get('url', '')
                print(f'[image: {url}]')
                continue
            elif btype == 'bookmark':
                url = content.get('url', '')
                print(f'[bookmark: {url}]')
                continue
            elif btype == 'embed':
                url = content.get('url', '')
                print(f'[embed: {url}]')
                continue
            elif btype == 'child_page':
                child_title = content.get('title', '')
                print(f'[child page: {child_title}]')
                continue
            elif btype == 'child_database':
                child_title = content.get('title', '')
                print(f'[child database: {child_title}]')
                continue
            elif btype == 'table':
                print('[table]')
                continue
            line = prefix + ''.join(t.get('plain_text', '') for t in texts)
            if line.strip():
                print(line)
        has_more = result.get('has_more', False)
        cursor = result.get('next_cursor')


# ---------------------------------------------------------------------------
# Create commands
# ---------------------------------------------------------------------------

def make_rich_text(text):
    return [{'type': 'text', 'text': {'content': text}}]


def cmd_add_note(title, project_ids, topic_ids, content, due):
    props = {
        'Name': {'title': make_rich_text(title)},
    }
    if project_ids:
        props['Projects + Notebooks'] = {'relation': [{'id': pid} for pid in project_ids]}
    if topic_ids:
        props['Topics'] = {'relation': [{'id': tid} for tid in topic_ids]}
    if due:
        props['Due'] = {'date': {'start': due}}

    body = {
        'parent': {'database_id': DB['notes']},
        'properties': props,
    }
    if content:
        body['children'] = [{
            'object': 'block',
            'type': 'paragraph',
            'paragraph': {'rich_text': make_rich_text(content)},
        }]

    page = post('/pages', body)
    print(f'Created note: {page["url"]}')
    print(f'  id: {page["id"]}')


def cmd_add_task(title, project_ids, horizon, work_style, due):
    props = {
        'Name': {'title': make_rich_text(title)},
    }
    if project_ids:
        props['Projects + Notebooks'] = {'relation': [{'id': pid} for pid in project_ids]}
    if horizon:
        props['Time Horizon'] = {'select': {'name': horizon}}
    if work_style:
        props['Work Style'] = {'select': {'name': work_style}}
    if due:
        props['Due'] = {'date': {'start': due}}

    body = {
        'parent': {'database_id': DB['tasks']},
        'properties': props,
    }
    page = post('/pages', body)
    print(f'Created task: {page["url"]}')
    print(f'  id: {page["id"]}')


def cmd_add_journal(title, journal_type, mood, energy, content):
    today = datetime.now().strftime('%Y-%m-%d')
    props = {
        'Name': {'title': make_rich_text(title)},
        'Date ': {'date': {'start': today}},
    }
    if journal_type:
        props['Journal Type'] = {'select': {'name': journal_type}}
    if mood:
        props['Mood'] = {'select': {'name': mood}}
    if energy:
        props['Energy'] = {'select': {'name': energy}}

    body = {
        'parent': {'database_id': DB['journal']},
        'properties': props,
    }
    if content:
        body['children'] = [{
            'object': 'block',
            'type': 'paragraph',
            'paragraph': {'rich_text': make_rich_text(content)},
        }]

    page = post('/pages', body)
    print(f'Created journal entry: {page["url"]}')
    print(f'  id: {page["id"]}')


def cmd_append(page_id, text):
    body = {
        'children': [{
            'object': 'block',
            'type': 'paragraph',
            'paragraph': {'rich_text': make_rich_text(text)},
        }]
    }
    result = patch(f'/blocks/{page_id}/children', body)
    print(f'Appended {len(result.get("results", []))} block(s) to {page_id}')


def cmd_archive(page_id):
    data = json.dumps({'archived': True}).encode()
    for attempt in range(15):
        try:
            req = urllib.request.Request(
                f'{BASE}/pages/{page_id}',
                data=data,
                headers=HEADERS,
                method='PATCH',
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                json.loads(resp.read())
                print(f'Archived page {page_id}')
                return
        except Exception as e:
            if attempt < 14:
                time.sleep(3)
            else:
                print(f'ERROR: could not archive {page_id}: {e}', file=sys.stderr)
                sys.exit(1)


# ---------------------------------------------------------------------------
# Markdown → Notion blocks
# ---------------------------------------------------------------------------

def _chunk(text, size=1900):
    """Split text into chunks that fit Notion's 2000-char rich_text limit."""
    return [text[i:i+size] for i in range(0, len(text), size)] if text else ['']


def md_to_blocks(md_text):
    """Convert markdown text to a list of Notion block dicts.
    Handles: h1/h2/h3, dividers, code fences, blockquotes, bullets, numbered lists, paragraphs.
    Tables are rendered as plain paragraphs (Notion API doesn't support tables).
    """
    blocks = []
    lines = md_text.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Code fence
        if line.startswith('```'):
            lang = line[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code_lines.append(lines[i])
                i += 1
            code_text = '\n'.join(code_lines)
            # Notion code blocks have a 2000-char limit too
            for chunk in _chunk(code_text):
                blocks.append({
                    'object': 'block', 'type': 'code',
                    'code': {
                        'rich_text': [{'type': 'text', 'text': {'content': chunk}}],
                        'language': lang or 'plain text',
                    },
                })
            i += 1
            continue

        # Heading 1
        if line.startswith('# '):
            text = line[2:].strip()
            for chunk in _chunk(text):
                blocks.append({
                    'object': 'block', 'type': 'heading_1',
                    'heading_1': {'rich_text': [{'type': 'text', 'text': {'content': chunk}}]},
                })
            i += 1
            continue

        # Heading 2
        if line.startswith('## '):
            text = line[3:].strip()
            for chunk in _chunk(text):
                blocks.append({
                    'object': 'block', 'type': 'heading_2',
                    'heading_2': {'rich_text': [{'type': 'text', 'text': {'content': chunk}}]},
                })
            i += 1
            continue

        # Heading 3
        if line.startswith('### '):
            text = line[4:].strip()
            for chunk in _chunk(text):
                blocks.append({
                    'object': 'block', 'type': 'heading_3',
                    'heading_3': {'rich_text': [{'type': 'text', 'text': {'content': chunk}}]},
                })
            i += 1
            continue

        # Divider
        if re.match(r'^---+$', line.strip()):
            blocks.append({'object': 'block', 'type': 'divider', 'divider': {}})
            i += 1
            continue

        # Blockquote
        if line.startswith('> '):
            text = line[2:].strip()
            for chunk in _chunk(text):
                blocks.append({
                    'object': 'block', 'type': 'quote',
                    'quote': {'rich_text': [{'type': 'text', 'text': {'content': chunk}}]},
                })
            i += 1
            continue

        # Bullet list
        if re.match(r'^[-*] ', line):
            text = line[2:].strip()
            for chunk in _chunk(text):
                blocks.append({
                    'object': 'block', 'type': 'bulleted_list_item',
                    'bulleted_list_item': {'rich_text': [{'type': 'text', 'text': {'content': chunk}}]},
                })
            i += 1
            continue

        # Numbered list
        m = re.match(r'^\d+\. ', line)
        if m:
            text = line[m.end():].strip()
            for chunk in _chunk(text):
                blocks.append({
                    'object': 'block', 'type': 'numbered_list_item',
                    'numbered_list_item': {'rich_text': [{'type': 'text', 'text': {'content': chunk}}]},
                })
            i += 1
            continue

        # Table row — render as paragraph
        if line.startswith('|'):
            text = line.strip()
            # Skip separator rows like |---|---|
            if re.match(r'^[\|\s\-:]+$', text):
                i += 1
                continue
            # Strip markdown pipes and render as text
            cells = [c.strip() for c in text.strip('|').split('|')]
            text = '  |  '.join(cells)
            for chunk in _chunk(text):
                blocks.append({
                    'object': 'block', 'type': 'paragraph',
                    'paragraph': {'rich_text': [{'type': 'text', 'text': {'content': chunk}}]},
                })
            i += 1
            continue

        # Blank line → skip
        if line.strip() == '':
            i += 1
            continue

        # Plain paragraph
        text = line.strip()
        for chunk in _chunk(text):
            blocks.append({
                'object': 'block', 'type': 'paragraph',
                'paragraph': {'rich_text': [{'type': 'text', 'text': {'content': chunk}}]},
            })
        i += 1

    return blocks


def upload_blocks(page_id, blocks):
    """Upload blocks in batches of 100 (Notion API limit). Uses PATCH as required."""
    batch_size = 100
    total = 0
    for start in range(0, len(blocks), batch_size):
        batch = blocks[start:start+batch_size]
        result = patch(f'/blocks/{page_id}/children', {'children': batch})
        total += len(result.get('results', []))
        print(f'  Uploaded blocks {start+1}–{start+len(batch)} ({total} total so far)')
    return total


def cmd_upload_md(title, filepath, project_ids, topic_ids):
    """Create a Note page and upload the full content of a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()

    blocks = md_to_blocks(md_text)
    print(f'Parsed {len(blocks)} blocks from {filepath}')

    # Create the page (no inline content yet)
    props = {'Name': {'title': make_rich_text(title)}}
    if project_ids:
        props['Projects + Notebooks'] = {'relation': [{'id': pid} for pid in project_ids]}
    if topic_ids:
        props['Topics'] = {'relation': [{'id': tid} for tid in topic_ids]}

    page = post('/pages', {'parent': {'database_id': DB['notes']}, 'properties': props})
    page_id = page['id']
    url = page['url']
    print(f'Created page: {url}')

    # Upload all blocks
    total = upload_blocks(page_id, blocks)
    print(f'Done — {total} blocks uploaded to {url}')
    return url


def cmd_upload_blocks_to_page(page_id, filepath):
    """Upload markdown file blocks to an already-existing page (resume after partial failure)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()

    blocks = md_to_blocks(md_text)
    print(f'Parsed {len(blocks)} blocks from {filepath}')
    total = upload_blocks(page_id, blocks)
    print(f'Done — {total} blocks uploaded to page {page_id}')



# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Notion Second Brain CLI')
    sub = parser.add_subparsers(dest='cmd', required=True)

    sub.add_parser('list-projects')
    sub.add_parser('list-topics')
    sub.add_parser('list-areas')

    p_search = sub.add_parser('search')
    p_search.add_argument('query', help='Text to search for in page titles')
    p_search.add_argument('--db', default='all', help='Database to search: notes, tasks, journal, or all (default: all)')

    p_note = sub.add_parser('add-note')
    p_note.add_argument('title')
    p_note.add_argument('--project-id', action='append', default=[], dest='project_ids')
    p_note.add_argument('--topic-id', action='append', default=[], dest='topic_ids')
    p_note.add_argument('--content', default='')
    p_note.add_argument('--due', default='')

    p_task = sub.add_parser('add-task')
    p_task.add_argument('title')
    p_task.add_argument('--project-id', action='append', default=[], dest='project_ids')
    p_task.add_argument('--horizon', default='')
    p_task.add_argument('--work-style', default='')
    p_task.add_argument('--due', default='')

    p_journal = sub.add_parser('add-journal')
    p_journal.add_argument('title')
    p_journal.add_argument('--journal-type', default='')
    p_journal.add_argument('--mood', default='')
    p_journal.add_argument('--energy', default='')
    p_journal.add_argument('--content', default='')

    p_append = sub.add_parser('append')
    p_append.add_argument('page_id')
    p_append.add_argument('text')

    p_upload = sub.add_parser('upload-md')
    p_upload.add_argument('title')
    p_upload.add_argument('filepath')
    p_upload.add_argument('--project-id', action='append', default=[], dest='project_ids')
    p_upload.add_argument('--topic-id', action='append', default=[], dest='topic_ids')

    p_resume = sub.add_parser('resume-upload')
    p_resume.add_argument('page_id')
    p_resume.add_argument('filepath')

    p_read = sub.add_parser('read-page')
    p_read.add_argument('page_id')

    p_archive = sub.add_parser('archive')
    p_archive.add_argument('page_id')

    args = parser.parse_args()

    if args.cmd == 'list-projects':   cmd_list_projects()
    elif args.cmd == 'list-topics':   cmd_list_topics()
    elif args.cmd == 'list-areas':    cmd_list_areas()
    elif args.cmd == 'search':        cmd_search(args.query, args.db)
    elif args.cmd == 'add-note':      cmd_add_note(args.title, args.project_ids, args.topic_ids, args.content, args.due)
    elif args.cmd == 'add-task':      cmd_add_task(args.title, args.project_ids, args.horizon, args.work_style, args.due)
    elif args.cmd == 'add-journal':   cmd_add_journal(args.title, args.journal_type, args.mood, args.energy, args.content)
    elif args.cmd == 'append':        cmd_append(args.page_id, args.text)
    elif args.cmd == 'read-page':     cmd_read_page(args.page_id)
    elif args.cmd == 'upload-md':     cmd_upload_md(args.title, args.filepath, args.project_ids, args.topic_ids)
    elif args.cmd == 'resume-upload': cmd_upload_blocks_to_page(args.page_id, args.filepath)
    elif args.cmd == 'archive':       cmd_archive(args.page_id)


if __name__ == '__main__':
    main()

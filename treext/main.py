#! /usr/bin/env python
import json
import os
import sys


MAX_SIZE = 1024 * 128  # 128 KB
MAX_LS = 50
MAX_DEPTH = 20


def tree(name, path, depth):
    if depth > MAX_DEPTH:
        return {'name': 'TOO DEEP'}

    read_only = os.access(path, os.R_OK) and not os.access(path, os.W_OK)
    if os.path.isdir(path):
        return {'name': name,
                'children': [tree(name, os.path.join(path, name), depth+1)
                             for name in os.listdir(path)[:MAX_LS]],
                'readOnly': read_only}
    with open(path, 'rb') as f:
        content = f.read(MAX_SIZE + 1)

    if len(content) > MAX_SIZE:
        return {'name': name, 'content': None, 'tooBig': True, 'readOnly': read_only}

    try:
        content = content.decode('utf-8')
    except UnicodeDecodeError:
        return {'name': name, 'content': None, 'isBinary': True,
                'tooBig': False, 'readOnly': read_only}

    return {'name': name, 'content': content, 'isBinary': False,
            'tooBig': False, 'readOnly': read_only}


def main():
    path = sys.argv[1]
    d = tree('', path, 0)
    print(json.dumps(d, ensure_ascii=False))

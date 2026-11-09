#!/usr/bin/env python3
import sys
import json

md5_file = sys.argv[1]
jsonl_file = sys.argv[2]

md5_map = {}

with open(md5_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        md5, path = line.split(None, 1)
        md5_map[path] = md5

with open(jsonl_file, "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        key = f"{obj['bucket']}/{obj['path']}"
        obj["md5"] = md5_map.get(key)
        print(json.dumps(obj, ensure_ascii=False))


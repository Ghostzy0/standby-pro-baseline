#!/usr/bin/env python3
import hashlib,json,pathlib,sys
root=pathlib.Path(__file__).resolve().parent
manifest=json.loads((root/'PROVENANCE.json').read_text())
bad=[name for name,digest in manifest['app_sha256'].items() if not (root/name).is_file() or hashlib.sha256((root/name).read_bytes()).hexdigest()!=digest]
if bad:
 print('Changed or missing pinned source:',*bad,sep='\n');sys.exit(1)
print(f"Verified {len(manifest['app_sha256'])} pinned source files at {manifest['upstream_commit']}")

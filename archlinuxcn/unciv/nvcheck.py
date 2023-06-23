#!/usr/bin/env python

import json
import urllib.request
import re
from pyalpm import vercmp
from functools import cmp_to_key

github_repo = "yairm210/Unciv"
from_pattern = r'(.*)-patch(\d+)'
to_pattern = r'\1.\2'
prefix = ''

def custom_preproc(vers):
  # Sometimes, vers contains a `-XXX` suffix
  # that is not covered by `from_pattern`.
  if "-" in vers:
    vers = vers.replace('-', '.')
  return f'{vers}.REL' if len(vers.split('.')) == 3 else vers

def remove_prefix(s, prefix):
  return s[len(prefix):] if s.startswith(prefix) else s

# Check github tags
# Replace by regex before sorting. This is not currently supported by nvchecker
req = urllib.request.Request(
    f'https://api.github.com/repos/{github_repo}/tags')
body = None
with urllib.request.urlopen(req) as res:
  body = json.load(res)

versions = [ custom_preproc(remove_prefix(re.sub(from_pattern, to_pattern, it['name']), prefix)) for it in body ]
versions.sort(key=cmp_to_key(vercmp))

print(versions[-1])

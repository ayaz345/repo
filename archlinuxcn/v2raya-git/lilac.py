#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('yarn config set'):
            line = f'#{line}'
        elif line.strip().startswith('export GO111MODULE'):
            line = f'#{line}'
        elif line.strip().startswith('export GOPROXY'):
            line = f'#{line}'
        print(line)

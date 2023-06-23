#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('depends='):
            line = (
                f'#{line}' + '\n'
                "depends=('camlp-streams' 'ocaml-easy-format')"
            )
        elif line.startswith('makedepends='):
            line = (
                f'#{line}' + '\n'
                "makedepends=('dune' 'ocaml' 'ocaml-findlib')"
            )
        print(line)

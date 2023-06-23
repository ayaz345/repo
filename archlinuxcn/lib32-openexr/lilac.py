#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='sbmomeni')
    pkgver, pkgrel = get_pkgver_and_pkgrel()
    so_ver = pkgver[:pkgver.rfind('.')].replace('.', '_')
    add_provides([f'libIex-{so_ver}.so', f'libIlmThread-{so_ver}.so', f'libOpenEXR-{so_ver}.so', f'libOpenEXRUtil-{so_ver}.so'])
    add_depends(['libImath-3_1.so', 'libz.so'])

def post_build():
    check_library_provides()
    aur_post_build()

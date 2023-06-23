from lilaclib import *

def pre_build():
  for line in edit_file('PKGBUILD'):
    if line.startswith('_pkgver'):
      line = f"_pkgver={_G.newver}"
    print(line)
  newver = _G.newver.replace("-",".")
  update_pkgver_and_pkgrel(newver)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()

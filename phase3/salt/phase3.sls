---
sudo:
  pkg:
    - installed
bash:
  pkg:
    - installed
zsh:
  pkg:
    - installed
ksh93:
  pkg:
    - installed
python:
  pkg:
    - installed
py-bsddb:
  pkg:
    - installed
    - name: "py27-bsddb"
py-gdbm:
  pkg:
    - installed
    - name: "py27-gdbm"
py-sqlite3:
  pkg:
    - installed
    - name: "py27-sqlite3"
py27-msgpack:
  pkg:
    - installed

foouser:
  user.present:
    - shell: /bin/sh

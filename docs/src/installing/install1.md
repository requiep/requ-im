# Installation
There are two ways to install a project: manually and automatically, if your system is `Unix` then automatically and if your system is `Windows` then only manually.

## Install automatically
```bash
git clone https://github.com/requiep/requ-im.git && cd requ-im

source bin/requ.sh

requ -i

requ <path-to-edit-file>
```

## Manual setting
```bash
git clone https://github.com/requiep/requ-im.git && cd requ-im

python -m pip install --upgrade pip

python -m pip install -r requirements.txt

python setup.py <path-to-edit-file>
```

> For installation, you must have installed Python version 3.11 and higher, this is necessary for the correct operation of the application.

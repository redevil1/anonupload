# anonfiles-script
An upload script for anonfile.com made in python. Supports multiple files.

 [![PyPI version](https://badge.fury.io/py/anonupload.svg)](https://pypi.org/project/anonupload/)
 [![Downloads](https://pepy.tech/badge/anonupload/month)](https://pepy.tech/project/anonupload)
 [![Downloads](https://static.pepy.tech/personalized-badge/anonupload?period=total&units=international_system&left_color=green&right_color=blue&left_text=Total%20Downloads)](https://pepy.tech/project/anonupload)
 ![GitHub Contributors](https://img.shields.io/github/contributors/redevil1/anonfiles)
 ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/redevil1/anonfiles)
 ![GitHub last commit](https://img.shields.io/github/last-commit/redevil1/anonfiles)
 ![Python 3.6](https://img.shields.io/badge/python-3.6-yellow.svg)


## Installation

```sh
pip3 install anonupload
```

## Usage 
```sh
anon up {path-to-file_1} {path-to-file _2} ...  # upload file to anonfile server
anon d {url1} {url2} ...              # download file 
```

## install old version 1.0.1
```sh
pip3 install anonupload==1.0.1
```

## Usage for version 1.0.1 

```sh
anon {path-to-file 1} {path-to-file 2}...
```
## You can change file name before upload on anonfile server

# API

The anonfile-upload client is also usable through an API (for test integration, automation, etc)

### anonupload.main.upload([file_path])

```py
from anonupload.main import upload

upload([file_path])
```

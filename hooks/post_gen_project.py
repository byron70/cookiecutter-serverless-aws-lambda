#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.md')

    remove_file('tests/__init__.py')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

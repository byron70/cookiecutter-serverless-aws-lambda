
Cookiecutter Python AWS Lambda with Serverless
===

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for a Python AWS Lambda with [Serverless](https://serverless.com/framework/docs/), [Pipenv]( https://docs.pipenv.org/) etc..

* GitHub repo: https://github.com/byron70/cookiecutter-serverless-aws-lambda/

## Why Pipenv?

Packaging in Python can be a pain, but it doesn't need to be. The new Pipenv project
has rapidly improved packaging in Python by tackling two related problems: automatic
package dependency management and virtualenv management. Pipenv uses the new [Pipfile](https://github.com/pypa/pipfile)
format that is the endorsed replacement for `requirements.txt`. Pipenv is the future of
Python package management in *application development*, and is even recommended to newcomers in the Python 
[tutorial](https://packaging.python.org/tutorials/managing-dependencies/#managing-dependencies).

## Features

* Testing setup with `python setup.py test` or `py.test`
* [Tox](http://testrun.org/tox/) testing: Setup to easily test for Python multiple Python versions
* [Bumpversion](https://github.com/peritus/bumpversion): Pre-configured version bumping with a single command (e.g. `bumpversion minor`)


## Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher):

```
pip install -U cookiecutter
```

Install the latest Pipenv:

```
pip install -U pipenv
```

Generate a Python project that uses Pipenv:

```
cookiecutter gh:byron70/cookiecutter-serverless-aws-lambda
```

Once your project has been created, change directories:

```
cd <project-name>
```

**Then:**

* Create a repo and put it there (e.g. `git init`).
* Setup the project (`make setup`).
* Deploy your serverless AWS service (`make deploy [STAGE=stage]`).
* Remove the serverless stack (`make remove [STAGE=stage]`).

## Fork This / Create Your Own

This project itself is a fork of [cookiecutter-serverless-aws-lambda](https://github.com/hypoport/cookiecutter-serverless-aws-lambda)


## Or Submit a Pull Request

I will consider pull requests as they come in, if they enhance the overall packaging experience.


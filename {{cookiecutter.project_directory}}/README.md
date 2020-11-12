{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
[![](https://img.shields.io/pypi/v/{{ cookiecutter.project_directory }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_directory }})

[![](https://img.shields.io/travis/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_directory }}.svg)](https://travis-ci.org/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_directory }})

[![Documentation Status](https://readthedocs.org/projects/{{ cookiecutter.project_directory | replace("_", "-") }}/badge/?version=latest)](https://{{ cookiecutter.project_directory | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest)
{%- endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_directory | replace("_", "-") }}.readthedocs.io.
{% endif %}

# Quickstart

1. Setup the python & serverless environment for testing, development & deployment
    ```
    make setup
    ```

2. Deploy your serverless AWS service 
    ```
    make deploy [STAGE=stage]
    ```

3. Remove the serverless stack 
    ```
    make remove [STAGE=stage]
    ```

# Features

**Testing** - using pytest:
```
make test
```

**Testing** - Using tox (includes linting using flake8 & linting of `serverless.yml`):
```
make test-all
```

**Testing** - test coverage:
```
make coverage
```

**Clean up** the environment (pipenv installation, serverless & npm, build-artifacts etc):
```
make clean
```

# Credits

This software was created with [Cookiecutter] and [`byron70/cookiecutter-serverless-aws-lambda`], based on [`hypoport/cookiecutter-serverless-aws-lambda`] which is forked from other repositories noted.

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[`byron70/cookiecutter-serverless-aws-lambda`]: https://github.com/hypoport/cookiecutter-serverless-aws-lambda
[`hypoport/cookiecutter-serverless-aws-lambda`]: https://github.com/hypoport/cookiecutter-serverless-aws-lambda
[`elgertam/cookiecutter-pipenv`]: https://github.com/elgertam/cookiecutter-pipenv
[`audreyr/cookiecutter-pypackage`]: https://github.com/audreyr/cookiecutter-pypackage

# What is this project?

This project is the culmination of research and implementation into automated tests and simplifying the build/publish cycle of Python projects into `PyPI` or other repositories. The three main components are:

- `Tox`
	- The test automation tool
- `Poetry`
	- The dependency management and build/publish framework
- `pyproject.toml`
	- The centralized dependency hub that contains metainformation about your project.

# Tox

`Tox` is a command-line test automating framework that allows you to configure several isolated virtual environments for testing. This verifies your code works across various configurations, while maintaining a simplified process of continuous integration. For example, you can test different `Python` versions, such as `py36`, `py37`, and then also test for `coverage`, `linting`, `unit tests`, etc.

## High-level summary

To work with `Tox`, you use the `tox.ini` file to setup configurations and test environments that the tool will read and execute. The project has a `tox.ini` file, but a simpler `tox.ini` example might have only two environments, such as this:

```
[tox]
envlist = py312, test

[testenv]
deps = pytest

[testenv:test]
command = pytest
```

## Tox commands

Before running commands, please install `tox` by running `pip install tox` in a virtual environment.

The basic structure of `Tox` commands look like the following:

- `tox`
	- This will run every environment, including `testenv`, which is the master environment that all other environments inherit from.
- `tox -e <ENV_NAME>`
	- This will run the environment you specify
- `tox -e <ENV_NAME1,ENV_NAME2,ENV_NAME3,...>`
	- This will run all the environments you specify

# pyproject.toml

`pyproject.toml` acts as the modern approach to uploading your project to `PyPI` and holding all your dependencies in one centralized location. Instead of writing a `Python` script to upload your files, you can quickly learn and understand the configuration file's rules and do everything much faster. However, `pyproject` is somewhat new, so many modern features are still being ironed out. 

# High-level summary

`pyproject.toml` is a file you keep in the root of your folder that provides metadata about your project, such as the dependencies it will use, the name of the project, its version, the authors, etc. To begin using it, we have to create a `pyproject.toml` file. Each section in the file starts with `[...]`, which signifies different parts. For example, you might have the `[project]` section, which has all the information about the project like its name and authors. The project has a `pyproject.toml` file, but a simpler example would only contain the necessary ingredients to make the file complete, like so:

```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "spam-eggs"
version = "2020.0.0"
dependencies = [
  "httpx",
  "gidgethub[httpx]>4.0.0",
  "django>2.1; os_name != 'nt'",
  "django>2.0; os_name == 'nt'",
]
requires-python = ">=3.8"
authors = [
  {name = "Pradyun Gedam", email = "pradyun@example.com"},
  {name = "Tzu-Ping Chung", email = "tzu-ping@example.com"},
  {name = "Another person"},
  {email = "different.person@example.com"},
]
maintainers = [
  {name = "Brett Cannon", email = "brett@example.com"}
]
description = "Lovely Spam! Wonderful Spam!"
readme = "README.md"
license = {file = "LICENSE.txt"}
keywords = ["egg", "bacon", "sausage", "tomatoes", "Lobster Thermidor"]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python"
]
```

This is a bit more complicated with a lot of parts, but don't worry. `Poetry`, our next section, leverages `pyproject.toml` and reorganizes it for its needs so you don't need to worry about semantics here. Just understand the structure and the overall picture.

# Poetry

`Poetry` is a dependency management and packaging tool that leverages the `pyproject.toml` file's utility for holding all the dependencies. Specifically, `poetry` handles everything from dependency resolution to environment management, allowing developers to maintain consistent and reproducible project setups.

# High-level summary

`Poetry` utilizes `pyproject.toml` to house its dependencies, as well as any configurations you need. In addition, it uses a `poetry.lock` file to lock the dependencies to a specific version, ensuring compatibility across different environments.

To start using `poetry`, we need to structure the `pyproject.toml` file with `poetry` sections. The project's `pyproject.toml` file has already been restructured, but a simpler example might look like this:

```
[tool.poetry]
name = "poetry-demo"
version = "0.1.0"
description = ""
authors = ["Sébastien Eustace <sebastien@eustace.io>"]
readme = "README.md"
packages = [{include = "poetry_demo"}]

[tool.poetry.dependencies]
python = "^3.7"

[tool.poetry.group.dev.dependencies]
pytest = "^8.3.2"
pylint = "^3.2.6"
black = "^24.4.2"
pytest-cov = "^5.0.0"
poetry = "^1.8.3"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

Here we see that `[project]` changed to become `[tool.poetry]`, although the metainformation will stay relatively the same. The primary difference is when we start looking at dependencies, as `Poetry` enables the separation of dependencies based on role. For example, we `[tool.poetry.dependencies]` and `[tool.poetry.group.dev.dependencies]`. The first contains the dependencies to run the application, whereas the `dev` group contains dependencies to lint, format, and test the application.

# Poetry commands

- `poetry init`
	- Initializes a `poetry` and creates a `pyproject.toml` file
- `poetry add <package>`
	- Adds a package (such as `coverage`, `pytest`, ...) to `pyproject.toml` and `poetry.lock`
- `poetry run <package>`
	- Runs a package (such as `coverage`, `pytest`, ...) from `poetry`
	- Uses the configurations found in `pyproject.toml` and the version from `poetry.lock`
- `poetry install`
	- Installs all the dependencies listed in `pyproject.toml` and `poetry.lock`
	- Can use the option `--without` to exclude certain groups, such as `dev`.
	- Can use the option `--no-root` to exclude downloading the package itself
- `poetry update`
	- Updates the project dependencies to their latest compatible versions
- `poetry build`
	- Builds the project, creating distribution files
- `poetry publish`
	- Publishes the project to `PyPI` or another repo.
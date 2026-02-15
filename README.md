# PyPackage

[Cookiecutter](https://cookiecutter.io/) template for a Python package.

## Features

- the package is an app, a library, or both — includes a CLI entrypoint and an importable package out of the box
- [mise](https://mise.jdx.dev/) — tool version management and task runner (manages uv). Add tools like Node, Go, Terraform, etc. to `mise.toml` as your project grows.
- [uv](https://docs.astral.sh/uv/) — package manager and build backend (manages Python)
- [ruff](https://docs.astral.sh/ruff/) — linter and formatter
- [devcontainer](https://containers.dev/) — reproducible development environment
- [docker](https://www.docker.com/) — multi-stage production build
- configurations for IDEs:
  - vscode (et al.)

## Prerequisites

First install [mise](https://mise.jdx.dev/).

## Usage

Create your new project:

```bash
mise x uv -- uvx cookiecutter gh:guziks/pypackage
```

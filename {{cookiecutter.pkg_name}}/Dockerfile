FROM ghcr.io/astral-sh/uv:python{{ cookiecutter.python_version }}-alpine AS export
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv export \
    --no-dev \
    --frozen \
    --no-emit-project \
    --format requirements.txt \
    --output-file requirements.txt

FROM python:{{ cookiecutter.python_version }}-slim AS base
WORKDIR /app
COPY --from=export /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install --no-deps .

FROM base AS app
CMD ["{{ cookiecutter.pkg_name }}"]

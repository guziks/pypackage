import re
import shutil
import subprocess
import sys


# -- Prerequisites ------------------------------------------------------------

if not shutil.which("mise"):
    print("Error: mise is required. Install from https://mise.jdx.dev", file=sys.stderr)
    sys.exit(1)


# -- Dev dependencies to add via `uv add --dev` -------------------------------

DEV_DEPS = [
    "ruff",
]


# -- Helpers ------------------------------------------------------------------

def run(cmd: list[str]) -> None:
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"Command failed: {' '.join(cmd)}", file=sys.stderr)
        sys.exit(result.returncode)


def mise_uv_version() -> str:
    result = subprocess.run(
        ["mise", "exec", "--", "uv", "--version"],
        capture_output=True, text=True, check=True,
    )
    # output: "uv 0.9.26 (...)" or "uv 0.9.26.build_editable (...)"
    raw = result.stdout.strip().split()[1]
    return re.match(r"\d+\.\d+\.\d+", raw).group()


# -- Init git repo ------------------------------------------------------------

run(["git", "init"])


# -- Install tools ------------------------------------------------------------

run(["mise", "trust"])
run(["mise", "install"])


# -- Pin build backend --------------------------------------------------------

uv_build_version = mise_uv_version()
pyproject_path = "pyproject.toml"
content = open(pyproject_path).read()
content = content.replace('requires = ["uv_build"]', f'requires = ["uv_build>={uv_build_version}"]')
open(pyproject_path, "w").write(content)

for dep in DEV_DEPS:
    run(["mise", "exec", "--", "uv", "add", "--dev", dep])

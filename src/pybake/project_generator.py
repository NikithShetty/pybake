"""Project generation logic."""

from pathlib import Path

from .config import ProjectConfig
from .templates import get_project_templates


class ProjectGenerator:
    """Generates new Python projects with all required files and configurations."""

    def __init__(self, config: ProjectConfig) -> None:
        """Initialize the project generator."""
        self.config = config
        self.templates = get_project_templates()

    def create_project(self, project_path: Path) -> None:
        """Create a complete Python project at the specified path."""
        # Create project directory
        project_path.mkdir(parents=True, exist_ok=True)

        # Create project structure
        self._create_directory_structure(project_path)

        # Generate all project files
        self._generate_project_files(project_path)

        # Make scripts executable (Unix-like systems)
        self._make_scripts_executable(project_path)

    def _create_directory_structure(self, project_path: Path) -> None:
        """Create the project directory structure."""
        directories = [
            "src",
            f"src/{self.config.package_name}",
            "tests",
            ".github",
            ".github/workflows",
        ]

        for directory in directories:
            (project_path / directory).mkdir(parents=True, exist_ok=True)

    def _generate_project_files(self, project_path: Path) -> None:
        """Generate all project files from templates."""
        # Generate main project files
        self._generate_file(
            project_path, "pyproject.toml", self._get_pyproject_content()
        )
        self._generate_file(project_path, ".python-version", self.config.python_version)
        self._generate_file(project_path, ".gitignore", self._get_gitignore_content())
        self._generate_file(project_path, "README.md", self._get_readme_content())

        # Tool configurations are now consolidated in pyproject.toml
        self._generate_file(
            project_path, ".pre-commit-config.yaml", self._get_precommit_content()
        )

        # Generate GitHub Actions
        self._generate_file(
            project_path / ".github" / "workflows",
            "ci.yml",
            self._get_github_actions_content(),
        )

        # Generate source code files
        self._generate_file(
            project_path / "src" / self.config.package_name,
            "__init__.py",
            self._get_init_content(),
        )
        self._generate_file(
            project_path / "src" / self.config.package_name,
            "main.py",
            self._get_main_content(),
        )

        # Generate test files
        self._generate_file(project_path / "tests", "__init__.py", "")
        self._generate_file(
            project_path / "tests",
            f"test_{self.config.package_name}.py",
            self._get_test_content(),
        )

    def _generate_file(self, path: Path, filename: str, content: str) -> None:
        """Generate a file with the specified content."""
        file_path = path / filename
        file_path.write_text(content, encoding="utf-8")

    def _make_scripts_executable(self, project_path: Path) -> None:
        """Make shell scripts executable on Unix-like systems."""
        # This is a no-op on Windows, but useful for cross-platform compatibility
        pass

    def _get_pyproject_content(self) -> str:
        """Generate pyproject.toml content."""
        return f'''[project]
name = "{self.config.name}"
version = "0.1.0"
description = "{self.config.description}"
readme = "README.md"
requires-python = ">={self.config.python_version}"
authors = [
    {{name = "{self.config.author or "Your Name"}", email = "{self.config.email or "your.email@example.com"}"}}
]
dependencies = [
    "beartype>=0.16.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
    "ruff>=0.12.9",
    "pyright>=1.1.0",
    "pre-commit>=3.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
target-version = "py{self.config.python_version.replace(".", "")}"
line-length = 88
lint.select = [
    "E",  # pycodestyle errors
    "W",  # pycodestyle warnings
    "F",  # pyflakes
    "I",  # isort
    "B",  # flake8-bugbear
    "C4", # flake8-comprehensions
    "UP", # pyupgrade
]
lint.ignore = ["E501"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

[tool.pyright]
include = ["src"]
exclude = [
    "**/node_modules",
    "**/__pycache__",
    ".venv",
    ".git",
]
reportMissingImports = "warning"
reportMissingTypeStubs = false
pythonVersion = "{self.config.python_version}"

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "--cov=src",
    "--cov-report=term-missing",
    "--cov-report=html",
    "--cov-report=xml",
]

[tool.coverage.run]
source = ["src"]
omit = [
    "*/tests/*",
    "*/test_*",
]
'''

    def _get_gitignore_content(self) -> str:
        """Generate .gitignore content."""
        return """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# poetry
poetry.lock

# pdm
.pdm.toml

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
.idea/

# VS Code
.vscode/

# macOS
.DS_Store

# Windows
Thumbs.db
ehthumbs.db
Desktop.ini

# uv
.uv/
uv.lock
"""

    def _get_readme_content(self) -> str:
        """Generate README.md content."""
        return f"""# {self.config.name}

{self.config.description}

## Requirements

- Python {self.config.python_version}+
- uv (recommended) or pip

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd {self.config.name}
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Activate virtual environment:
   ```bash
   uv shell
   ```

## Development

### Running tests
```bash
pytest
```

### Code quality
```bash
ruff check .
ruff format .
```

### Type checking
```bash
pyright
```

### Pre-commit hooks
```bash
pre-commit install
pre-commit run --all-files
```

## Project Structure

```
{self.config.name}/
├── src/
│   └── {self.config.package_name}/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_{self.config.package_name}.py
├── .github/workflows/
├── pyproject.toml
└── .pre-commit-config.yaml
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and quality checks
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

{self.config.author or "Your Name"} - {self.config.email or "your.email@example.com"}
"""

    def _get_precommit_content(self) -> str:
        """Generate .pre-commit-config.yaml content."""
        return """repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.12.9
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
"""

    def _get_github_actions_content(self) -> str:
        """Generate GitHub Actions CI workflow content."""
        return f"""name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["{self.config.python_version}"]

    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python ${{{{ matrix.python-version }}}}
      uses: actions/setup-python@v4
      with:
        python-version: ${{{{ matrix.python-version }}}}
    
    - name: Install uv
      uses: astral-sh/setup-uv@v1
      with:
        version: latest
    
    - name: Install dependencies
      run: uv sync
    
    - name: Run linting
      run: uv run ruff check .
    
    - name: Run formatting check
      run: uv run ruff format --check .
    
    - name: Run type checking
      run: uv run pyright
    
    - name: Run tests
      run: uv run pytest --cov=src --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml
        fail_ci_if_error: false
"""

    def _get_init_content(self) -> str:
        """Generate __init__.py content."""
        return f'''"""Package {self.config.name}."""

__version__ = "0.1.0"
__author__ = "{self.config.author or "Your Name"}"
__email__ = "{self.config.email or "your.email@example.com"}"

from .main import main

__all__ = ["main"]
'''

    def _get_main_content(self) -> str:
        """Generate main.py content."""
        return f'''"""Main module for {self.config.name}."""

from beartype import beartype


@beartype
def main() -> None:
    """Main function."""
    print("Hello from {self.config.name}!")


if __name__ == "__main__":
    main()
'''

    def _get_test_content(self) -> str:
        """Generate test file content."""
        return f'''"""Tests for {self.config.name}."""

import pytest
from {self.config.package_name}.main import main


def test_main(capsys):
    """Test main function output."""
    main()
    captured = capsys.readouterr()
    assert "{self.config.name}" in captured.out


def test_main_returns_none():
    """Test main function return value."""
    result = main()
    assert result is None
'''

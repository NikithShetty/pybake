# PyBake CLI

A powerful CLI tool that creates new Python projects with modern tooling setup, including uv, pyright, ruff, beartype, pytest, pre-commit, and GitHub Actions.

## 🚀 Features

- **Modern Python Project Structure**: Creates well-organized projects with src layout
- **Dependency Management**: Configures uv for fast package management
- **Static Analysis**: Sets up pyright for comprehensive type checking
- **Code Quality**: Configures ruff for linting and formatting
- **Runtime Validation**: Integrates beartype for runtime type checking
- **Testing**: Sets up pytest with coverage reporting
- **Git Hooks**: Configures pre-commit for automated quality checks
- **CI/CD**: Creates GitHub Actions workflows for automated testing
- **Interactive Setup**: Guided project creation with prompts
- **Multiple Templates**: Support for different project types

## 📋 Requirements

- Python 3.12+
- uv (for running the tool)

## 🛠️ Installation

### Using uvx (Recommended - No Installation Required)

The easiest way to use PyBake is with `uvx`, which runs the tool directly from the repository without any installation:

```bash
# Run directly without installation
uvx pybake --help

# Create a new project
uvx pybake create my-awesome-project

# List available templates
uvx pybake list-templates

# Show tool information
uvx pybake info
```

### Alternative: Local Development Setup

If you want to contribute to PyBake or run it locally:

```bash
# Clone the repository
git clone https://github.com/NikithShetty/pybake.git
cd pybake

# Install dependencies
uv sync

# Run locally
uv run pybake --help
```

## 🎯 Usage

### Create a New Project

```bash
# Basic usage with uvx
uvx pybake create my-awesome-project

# With custom options
uvx pybake create my-awesome-project \
    --python 3.12 \
    --description "My awesome Python project" \
    --author "Your Name" \
    --email "your.email@example.com" \
    --path /path/to/projects
```

### Available Commands

```bash
# Show help
uvx pybake --help

# Create a new project
uvx pybake create <project-name> [options]

# List available templates
uvx pybake list-templates

# Show tool information
uvx pybake info
```

### Command Options

- `--path, -p`: Path where to create the project (default: current directory)
- `--python, -py`: Python version requirement (default: 3.12)
- `--description, -d`: Project description
- `--author, -a`: Project author name
- `--email, -e`: Author email address
- `--no-interactive`: Disable interactive mode

## 🏗️ Generated Project Structure

```bash
my-awesome-project/
├── src/
│   └── my_awesome_project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_my_awesome_project.py
├── docs/
│   └── README.md
├── .github/
│   └── workflows/
│       └── ci.yml
├── pyproject.toml
├── .python-version
├── .gitignore
├── README.md
└── .pre-commit-config.yaml
```

## 🛠️ Tools Included

### 1. Environment & Dependency Management
- **uv**: Fast Python package installer and resolver

### 2. Typing & Static Analysis
- **pyright**: Microsoft's static type checker for Python
- **ruff**: Extremely fast Python linter and formatter
- **beartype**: Runtime type checking decorator

### 3. Testing
- **pytest**: Testing framework with powerful features
- **pytest-cov**: Coverage reporting for pytest
- **pre-commit**: Git hooks for code quality
- **GitHub Actions**: Automated CI/CD workflows

## 🔧 Configuration Files

### pyproject.toml
- Project metadata and dependencies
- Tool configurations for ruff, pyright, pytest, and coverage
- Build system configuration with hatchling
- uv-specific configuration for development dependencies

### .pre-commit-config.yaml
- Git hooks for code quality
- Automated formatting and linting on commit

### GitHub Actions (ci.yml)
- Automated testing on push/PR
- Coverage reporting and quality checks

## 🚀 Quick Start

1. **Run the tool directly** (recommended):
   ```bash
   uvx pybake create my-project
   ```

2. **Navigate to your project**:
   ```bash
   cd my-project
   ```

3. **Initialize git and install dependencies**:
   ```bash
   git init
   uv sync
   ```

4. **Activate virtual environment and run tests**:
   ```bash
   uv shell
   pytest
   ```

## 🧪 Testing

```bash
# Run tests
pytest

# Run tests with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_my_awesome_project.py
```

## 🔍 Code Quality

```bash
# Lint code
ruff check .

# Format code
ruff format .

# Type checking
pyright

# Run all pre-commit hooks
pre-commit run --all-files
```

## 📚 Development

### Project Structure

```bash
pybake/
├── src/
│   └── pybake/
│       ├── __init__.py
│       ├── cli.py              # Main CLI application
│       ├── config.py            # Configuration classes
│       ├── project_generator.py # Project generation logic
│       ├── templates.py         # Project templates
│       └── __main__.py          # Module entry point
├── tests/                       # Test files
├── pyproject.toml              # Project configuration
├── main.py                     # Alternative entry point
└── README.md                   # This file
```

### Adding New Templates

1. Update `templates.py` with new template configuration
2. Modify `project_generator.py` to handle template-specific logic
3. Add template-specific file generation methods

### Adding New Tools

1. Update `pyproject.toml` with new dependencies
2. Add tool configuration files in `project_generator.py`
3. Update documentation and help text

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and quality checks
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [uv](https://github.com/astral-sh/uv) - Fast Python package manager
- [uvx](https://github.com/astral-sh/uvx) - Run Python packages directly from git
- [pyright](https://github.com/microsoft/pyright) - Static type checker
- [ruff](https://github.com/astral-sh/ruff) - Fast Python linter
- [beartype](https://github.com/beartype/beartype) - Runtime type checking
- [pytest](https://github.com/pytest-dev/pytest) - Testing framework
- [pre-commit](https://github.com/pre-commit/pre-commit) - Git hooks
- [Typer](https://github.com/tiangolo/typer) - CLI framework
- [Rich](https://github.com/Textualize/rich) - Rich text and formatting

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/NikithShetty/pybake/issues) page
2. Create a new issue with detailed information
3. Join our community discussions

---

**Happy coding! 🚀**

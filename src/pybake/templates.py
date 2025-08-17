"""Project templates and configurations."""

from typing import Any


def get_project_templates() -> dict[str, Any]:
    """Get available project templates."""
    return {
        "standard": {
            "name": "Standard Python Project",
            "description": "Complete Python project with all modern tools",
            "features": [
                "uv for dependency management",
                "pyright for static analysis",
                "ruff for linting and formatting",
                "beartype for runtime type checking",
                "pytest for testing",
                "pre-commit for git hooks",
                "GitHub Actions for CI/CD",
            ],
        },
        "minimal": {
            "name": "Minimal Python Project",
            "description": "Basic Python project with essential tools",
            "features": [
                "uv for dependency management",
                "ruff for linting and formatting",
                "pytest for testing",
            ],
        },
        "web": {
            "name": "Web Application",
            "description": "Python web application template",
            "features": [
                "FastAPI or Flask web framework",
                "uv for dependency management",
                "pyright for static analysis",
                "ruff for linting and formatting",
                "beartype for runtime type checking",
                "pytest for testing",
                "pre-commit for git hooks",
                "GitHub Actions for CI/CD",
            ],
        },
    }


def get_template_config(template_name: str) -> dict[str, Any]:
    """Get configuration for a specific template."""
    templates = get_project_templates()
    if template_name not in templates:
        raise ValueError(f"Unknown template: {template_name}")

    return templates[template_name]

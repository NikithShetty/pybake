"""Project configuration data classes."""

from dataclasses import dataclass


@dataclass
class ProjectConfig:
    """Configuration for a new Python project."""

    name: str
    python_version: str
    description: str
    author: str | None = None
    email: str | None = None

    def __post_init__(self) -> None:
        """Validate configuration after initialization."""
        if not self.name:
            raise ValueError("Project name cannot be empty")

        if not self.python_version:
            raise ValueError("Python version cannot be empty")

        if not self.description:
            raise ValueError("Project description cannot be empty")

    @property
    def package_name(self) -> str:
        """Get the package name (normalized for imports)."""
        return self.name.replace("-", "_").replace(" ", "_").lower()

    @property
    def class_name(self) -> str:
        """Get the class name (PascalCase)."""
        return "".join(
            word.capitalize() for word in self.name.replace("-", " ").split()
        )

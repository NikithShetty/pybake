"""CLI application for creating Python projects."""

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Confirm, Prompt
from rich.table import Table

from .config import ProjectConfig
from .project_generator import ProjectGenerator

app = typer.Typer(
    name="pybake",
    help="Create new Python projects with modern tooling setup",
    add_completion=False,
)

console = Console()


@app.command()
def create(
    project_name: str = typer.Argument(..., help="Name of the project to create"),
    path: Path | None = typer.Option(
        None, "--path", "-p", help="Path where to create the project"
    ),
    python_version: str = typer.Option(
        "3.12", "--python", "-py", help="Python version requirement"
    ),
    description: str | None = typer.Option(
        None, "--description", "-d", help="Project description"
    ),
    author: str | None = typer.Option(None, "--author", "-a", help="Project author"),
    email: str | None = typer.Option(None, "--email", "-e", help="Author email"),
    interactive: bool = typer.Option(
        True, "--no-interactive", help="Disable interactive mode"
    ),
) -> None:
    """Create a new Python project with modern tooling setup."""
    try:
        # Determine project path
        if path is None:
            path = Path.cwd()

        project_path = path / project_name

        # Check if project already exists
        if project_path.exists():
            if not Confirm.ask(f"Project '{project_name}' already exists. Overwrite?"):
                console.print("Operation cancelled.", style="yellow")
                raise typer.Exit(1)

        # Create configuration
        config = ProjectConfig(
            name=project_name,
            python_version=python_version,
            description=description or f"A Python project called {project_name}",
            author=author,
            email=email,
        )

        # Interactive mode for missing information
        if interactive:
            config = _gather_project_info(config)

        # Show project summary
        _show_project_summary(config, project_path)

        if not Confirm.ask("Proceed with project creation?"):
            console.print("Operation cancelled.", style="yellow")
            raise typer.Exit(1)

        # Create the project
        generator = ProjectGenerator(config)

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Creating project...", total=None)
            generator.create_project(project_path)
            progress.update(task, description="Project created successfully!")

        # Show success message
        _show_success_message(project_path, config)

    except Exception as e:
        console.print(f"Error: {e}", style="red")
        raise typer.Exit(1)


@app.command()
def list_templates() -> None:
    """List available project templates."""
    console.print("Available project templates:", style="bold blue")

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Template", style="cyan")
    table.add_column("Description")

    table.add_row("standard", "Standard Python project with all tools")
    table.add_row("minimal", "Minimal setup with basic tooling")
    table.add_row("web", "Web application template")

    console.print(table)


@app.command()
def info() -> None:
    """Show information about the CLI tool."""
    info_text = """
    [bold blue]PyBake CLI[/bold blue]
    
    Version: 0.1.0
    
    This tool creates new Python projects with:
    • [green]uv[/green] for dependency management
    • [green]pyright[/green] for static analysis
    • [green]ruff[/green] for linting and formatting
    • [green]beartype[/green] for runtime type checking
    • [green]pytest[/green] for testing
    • [green]pre-commit[/green] for git hooks
    • [green]GitHub Actions[/green] for CI/CD
    
    Use [cyan]pybake create <name>[/cyan] to start a new project.
    """

    console.print(Panel(info_text, title="ℹ️  Information", border_style="blue"))


def _gather_project_info(config: ProjectConfig) -> ProjectConfig:
    """Gather missing project information interactively."""
    if not config.author:
        config.author = Prompt.ask("Author name", default="Your Name")

    if not config.email:
        config.email = Prompt.ask("Author email", default="your.email@example.com")

    if (
        not config.description
        or config.description == f"A Python project called {config.name}"
    ):
        config.description = Prompt.ask(
            "Project description", default=f"A Python project called {config.name}"
        )

    return config


def _show_project_summary(config: ProjectConfig, project_path: Path) -> None:
    """Show a summary of the project to be created."""
    summary = f"""
    [bold blue]Project Summary[/bold blue]
    
    Name: [cyan]{config.name}[/cyan]
    Path: [cyan]{project_path.absolute()}[/cyan]
    Python: [cyan]{config.python_version}[/cyan]
    Description: [cyan]{config.description}[/cyan]
    Author: [cyan]{config.author}[/cyan]
    Email: [cyan]{config.email}[/cyan]
    
    [bold green]Tools to be installed:[/bold green]
    • uv (dependency management)
    • pyright (static analysis)
    • ruff (linting & formatting)
    • beartype (runtime type checking)
    • pytest (testing)
    • pre-commit (git hooks)
    • GitHub Actions (CI/CD)
    """

    console.print(Panel(summary, title="📋 Project Summary", border_style="green"))


def _show_success_message(project_path: Path, config: ProjectConfig) -> None:
    """Show success message with next steps."""
    next_steps = f"""
    [bold green]✅ Project created successfully![/bold green]
    
    [bold]Next steps:[/bold]
    
    1. Navigate to your project:
       [cyan]cd {project_path}[/cyan]
    
    2. Initialize git repository:
       [cyan]git init[/cyan]
    
    3. Install dependencies:
       [cyan]uv sync[/cyan]
    
    4. Activate virtual environment:
       [cyan]uv shell[/cyan]
    
    5. Run tests:
       [cyan]pytest[/cyan]
    
    6. Start coding in [cyan]src/{config.name}/[/cyan]
    
    [bold]Happy coding! 🚀[/bold]
    """

    console.print(Panel(next_steps, title="🎉 Success!", border_style="green"))


if __name__ == "__main__":
    app()

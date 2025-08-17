"""Tests for the PyBake CLI application."""

import pytest
from typer.testing import CliRunner

from pybake.cli import app


@pytest.fixture
def runner():
    """Create a CLI runner for testing."""
    return CliRunner()


def test_info_command(runner):
    """Test the info command."""
    result = runner.invoke(app, ["info"])
    assert result.exit_code == 0
    assert "PyBake CLI" in result.output


def test_list_templates_command(runner):
    """Test the list templates command."""
    result = runner.invoke(app, ["list-templates"])
    assert result.exit_code == 0
    assert "standard" in result.output
    assert "minimal" in result.output
    assert "web" in result.output


def test_create_command_help(runner):
    """Test the create command help."""
    result = runner.invoke(app, ["create", "--help"])
    assert result.exit_code == 0
    assert "project_name" in result.output


def test_create_command_missing_name(runner):
    """Test the create command with missing project name."""
    result = runner.invoke(app, ["create"])
    assert result.exit_code != 0

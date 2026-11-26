"""Tests for package installation and imports."""

from importlib import import_module


def test_package_import():
    """Verify that the package can be imported."""
    import_module("planar_point_patterns")

#!/usr/bin/env python
"""Django project management script."""

import os
import sys
from django.core.management import execute_from_command_line  # Move import to the top


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pydjango_ci_integration.settings')
    try:
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and available on your PYTHONPATH "
            "environment variable? Did you forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()

# Ensure a final newline exists at the end

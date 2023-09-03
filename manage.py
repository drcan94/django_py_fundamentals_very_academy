#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# python -m venv venv
# pip freeze > requirements.txt
# django-admin startproject core . # this will create a new project called core in the current directory
# django-admin startapp newapp # this will create a new app called newapp


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

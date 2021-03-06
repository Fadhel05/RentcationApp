#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
# import os
# import sys
#
#
# def main():
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'transitions.settings')
#     try:
#         from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)
#
#
# if __name__ == '__main__':
#     main()
#!/usr/bin/env python
import os
import sys
from django.core.management.commands.runserver import Command as runserver

if __name__ == '__main__':
    # port = os.environ.get("PORT", 5000)
    # runserver.default_port = port
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Rentcation.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

"""
WSGI config for pydjango_ci_integration project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pydjango_ci_integration.settings")

# Uncomment these lines to source an environment file
# from dotenv import load_dotenv
# load_dotenv('/path/to/env_file')

application = get_wsgi_application()
"""



#--
"""
WSGI config for pydjango_ci_integration project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more details, see:
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

# Set default settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pydjango_ci_integration.settings")

# Load environment variables (Optional)
from dotenv import load_dotenv
load_dotenv()  # Automatically loads .env from the project root

# WSGI application entry point
application = get_wsgi_application()

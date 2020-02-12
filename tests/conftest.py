import os
import shutil
import sys

import pytest
from django.apps import apps
from django.core.management import call_command


@pytest.yield_fixture
def cleanup_theme_app(settings):
    theme_app_dir = os.path.join(settings.BASE_DIR, 'theme')

    if os.path.isdir(theme_app_dir):
        shutil.rmtree(theme_app_dir)

    yield

    if os.path.isdir(theme_app_dir):
        shutil.rmtree(theme_app_dir)


@pytest.yield_fixture
def with_theme_app(cleanup_theme_app, settings):
    if 'theme' in sys.modules:
        del sys.modules['theme']
    if 'theme' in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS.pop()

    call_command('tailwind', 'init', 'theme')
    settings.INSTALLED_APPS += ['theme']
    apps.set_installed_apps(settings.INSTALLED_APPS)
    settings.TAILWIND_APP_NAME = 'theme'
    yield

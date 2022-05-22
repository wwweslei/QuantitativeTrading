from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage


def test_static_finder_js():
    abs_path = finders.find('core/js/main.js')
    assert abs_path is not None 

def test_static_finder_css():
    abs_path = finders.find('core/css/main.scss')
    assert abs_path is not None

def test_staticfiles_storage_js():
    abs_path = finders.find('core/js/main.js')
    assert staticfiles_storage.exists(str(abs_path))
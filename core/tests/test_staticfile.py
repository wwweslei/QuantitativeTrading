from django.contrib.staticfiles.storage import staticfiles_storage


def test_static_storage_js():
    abs_path = staticfiles_storage.path("core/js/main.js")
    assert abs_path is not None


def test_static_storage_css():
    abs_path = staticfiles_storage.path("core/css/main.scss")
    assert abs_path is not None

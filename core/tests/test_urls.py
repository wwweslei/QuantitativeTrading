import pytest
from django.test import Client


@pytest.mark.django_db()
def test_home_check(client: Client) -> None:
    """This test ensures that home check is accessible."""
    response = client.get("/")

    assert response.status_code == 200


def test_admin_unauthorized(client: Client) -> None:
    """This test ensures that admin panel requires auth."""
    response = client.get("/admin/")

    assert response.status_code == 302


def test_admin_authorized(admin_client: Client) -> None:
    """This test ensures that admin panel is accessible."""
    response = admin_client.get("/admin/")

    assert response.status_code == 200


def test_admin_docs_unauthorized(client: Client) -> None:
    """This test ensures that admin panel docs requires auth."""
    response = client.get("/admin/")

    assert response.status_code == 302


def test_admin_docs_authorized(admin_client: Client) -> None:
    """This test ensures that admin panel docs are accessible."""
    response = admin_client.get("/admin/core/")

    assert response.status_code == 200
    assert b"docutils" not in response.content  # type: ignore

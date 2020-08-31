import pytest

from django.urls import reverse

from projeto.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp


@pytest.mark.django_db
def test_status_code(resp):
    assert resp.status_code == 200


@pytest.mark.django_db
def test_title(resp):
    assert_contains(resp, '<title>Tayla Belinot</title>')



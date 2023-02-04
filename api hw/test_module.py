import pytest
import requests


def test_status_code(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru", help="URL to test")
    parser.addoption("--status_code", default=200, help="Expected status code")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")

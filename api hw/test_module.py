import requests


def test_status_code(url, status_code):
    """
    Test the status code of the response from the provided URL.

    :param url: URL to send the GET request to
    :param status_code: Expected status code of the response
    :return: None
    """
    # Send a GET request to the provided URL
    response = requests.get(url)

    # Verify that the response's status code matches the expected status code
    assert response.status_code == status_code


def pytest_addoption(parser):
    """
    Add command line options to control the URL and expected status code of the test.

    :param parser: Parser object provided by pytest
    :return: None
    """
    parser.addoption("--url", default="https://ya.ru", help="URL to test")
    parser.addoption("--status_code", default=200, help="Expected status code")

import pytest
import requests


@pytest.mark.parametrize("state", ["california", "new york", "colorado"])
def test_breweries_by_state(state):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_state={state}")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)


@pytest.mark.parametrize("type", ["micro", "regional", "brewpub"])
def test_breweries_by_type(type):
    response = requests.get(f"https://api.openbrewerydb.org/breweries?by_type={type}")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)


def test_get_all_breweries():
    response = requests.get("https://api.openbrewerydb.org/breweries")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)


def test_get_specific_brewery(brewery_id=1):
    response = requests.get(f"https://api.openbrewerydb.org/breweries/{brewery_id}")
    data = response.json()

    assert response.status_code == 200
    assert "name" in data and "id" in data


def test_search_breweries(search_term='dog'):
    response = requests.get(f"https://api.openbrewerydb.org/breweries/search?query={search_term}")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)

import jsonschema
import pytest
import requests
from examples import base_urls
from examples.schemas import brewery_schema


@pytest.mark.parametrize("state", ["california", "new york", "colorado"])
def test_breweries_by_state(state):
    response = requests.get(f"{base_urls.BASE_URL_OPENBREWERYDB}breweries?by_state={state}")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    jsonschema.validate(instance=data, schema=brewery_schema)


@pytest.mark.parametrize("type", ["micro", "regional", "brewpub"])
def test_breweries_by_type(type):
    response = requests.get(f"{base_urls.BASE_URL_OPENBREWERYDB}breweries?by_type={type}")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    jsonschema.validate(instance=data, schema=brewery_schema)


def test_get_all_breweries():
    response = requests.get(f"{base_urls.BASE_URL_OPENBREWERYDB}breweries")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    jsonschema.validate(instance=data, schema=brewery_schema)


def test_get_specific_brewery(brewery_id=1):
    response = requests.get(f"{base_urls.BASE_URL_OPENBREWERYDB}breweries/{brewery_id}")
    data = response.json()

    assert response.status_code == 200 or response.status_code == 404
    if response.status_code == 200:
        assert "name" in data and "id" in data
        jsonschema.validate(instance=data, schema=brewery_schema)


def test_search_breweries(search_term='dog'):
    response = requests.get(f"{base_urls.BASE_URL_OPENBREWERYDB}breweries/search?query={search_term}")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    jsonschema.validate(instance=data, schema=brewery_schema)

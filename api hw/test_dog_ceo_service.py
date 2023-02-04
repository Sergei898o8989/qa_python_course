import jsonschema
import pytest
import requests
from examples import base_urls
from examples.schemas import response_schema_image_random, response_schema_sub_breed, response_schema_all, \
    response_schema_list_images


@pytest.mark.parametrize("breed_name", ["husky", "poodle", "retriever"])
def test_random_image_of_breed(breed_name):
    response = requests.get(f"{base_urls.BASE_URL_DOG_CEO}/breed/{breed_name}/images/random")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=response_schema_image_random)


@pytest.mark.parametrize("breed_name,sub_breed_name", [("retriever", "golden"), ("poodle", "toy")])
def test_random_image_of_sub_breed(breed_name, sub_breed_name):
    response = requests.get(f"{base_urls.BASE_URL_DOG_CEO}/breed/{breed_name}/{sub_breed_name}/images/random")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=response_schema_sub_breed)


def test_list_all_breeds():
    response = requests.get(f"{base_urls.BASE_URL_DOG_CEO}/breeds/list/all")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=response_schema_all)


def test_list_images_of_breed():
    breed_name = "poodle"
    response = requests.get(f"{base_urls.BASE_URL_DOG_CEO}/breed/{breed_name}/images")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=response_schema_list_images)


def test_invalid_sub_breed_name():
    breed_name = "retriever"
    sub_breed_name = "not_a_real_sub_breed"
    response = requests.get(f"{base_urls.BASE_URL_DOG_CEO}/breed/{breed_name}/{sub_breed_name}/images/random")

    assert response.status_code

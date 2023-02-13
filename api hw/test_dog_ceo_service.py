import jsonschema
import pytest
import requests
from examples import base_urls
from examples.schemas import response_schema_image_random, response_schema_sub_breed, response_schema_all, \
    response_schema_list_images


@pytest.mark.parametrize("breed_name", ["husky", "poodle", "retriever"])
def test_random_image_of_breed(breed_name):
    """
    Test to get a random image of the given breed.
    The test sends a GET request to the `/breed/{breed_name}/images/random` endpoint.
    It then validates the response code to be 200 and the response data against
    the `response_schema_image_random` schema.

    :param breed_name: The name of the breed to get a random image of.
    :type breed_name: str
    :return: None
    """
    response = requests.get(f"{base_urls.BASE_URL_DOG_CEO}/breed/{breed_name}/images/random")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=response_schema_image_random)


@pytest.mark.parametrize("breed_name,sub_breed_name", [("retriever", "golden"), ("poodle", "toy")])
def test_random_image_of_sub_breed(breed_name, sub_breed_name):
    """
    Test to get a random image of the given sub-breed.
    The test sends a GET request to the `/breed/{breed_name}/{sub_breed_name}/images/random` endpoint.
    It then validates the response code to be 200 and the response data against the `response_schema_sub_breed` schema.

    :param breed_name: The name of the breed the sub-breed belongs to.
    :type breed_name: str
    :param sub_breed_name: The name of the sub-breed to get a random image of.
    :type sub_breed_name: str
    :return: None
    """
    response = requests.get(f"{base_urls.BASE_URL_DOG_CEO}/breed/{breed_name}/{sub_breed_name}/images/random")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=response_schema_sub_breed)


def test_list_all_breeds():
    """
    Test that the endpoint for retrieving all breeds returns a 200 status code and
    validates the response against the expected schema.
    """
    response = requests.get(f"{base_urls.BASE_URL_DOG_CEO}/breeds/list/all")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=response_schema_all)


def test_list_images_of_breed():
    """
    Test that the endpoint for retrieving images of a breed returns a 200 status code and
    validates the response against the expected schema.
    """
    breed_name = "poodle"
    response = requests.get(f"{base_urls.BASE_URL_DOG_CEO}/breed/{breed_name}/images")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=response_schema_list_images)


def test_invalid_sub_breed_name():
    """
    Test that the endpoint returns a 404 status code when a request is made for
    an invalid sub breed.
    """
    breed_name = "retriever"
    sub_breed_name = "not_a_real_sub_breed"
    response = requests.get(f"{base_urls.BASE_URL_DOG_CEO}/breed/{breed_name}/{sub_breed_name}/images/random")

    assert response.status_code == 404
    """
    Note: The expected status code should be 404, not the current value of response.status_code. 
    """

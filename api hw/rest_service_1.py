import pytest
import requests


@pytest.mark.parametrize("breed_name", ["husky", "poodle", "retriever"])
def test_random_image_of_breed(breed_name):
    response = requests.get(f"https://dog.ceo/api/breed/{breed_name}/images/random")
    data = response.json()

    assert response.status_code == 200
    assert "message" in data
    assert "status" in data and data["status"] == "success"


@pytest.mark.parametrize("breed_name,sub_breed_name", [("retriever", "golden"), ("poodle", "toy")])
def test_random_image_of_sub_breed(breed_name, sub_breed_name):
    response = requests.get(f"https://dog.ceo/api/breed/{breed_name}/{sub_breed_name}/images/random")
    data = response.json()

    assert response.status_code == 200
    assert "message" in data
    assert "status" in data and data["status"] == "success"


def test_list_all_breeds():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    data = response.json()

    assert response.status_code == 200
    assert "message" in data
    assert "status" in data and data["status"] == "success"


def test_list_images_of_breed():
    breed_name = "poodle"
    response = requests.get(f"https://dog.ceo/api/breed/{breed_name}/images")
    data = response.json()

    assert response.status_code == 200
    assert "message" in data
    assert "status"


def test_invalid_sub_breed_name():
    breed_name = "retriever"
    sub_breed_name = "not_a_real_sub_breed"
    response = requests.get(f"https://dog.ceo/api/breed/{breed_name}/{sub_breed_name}/images/random")

    assert response.status_code

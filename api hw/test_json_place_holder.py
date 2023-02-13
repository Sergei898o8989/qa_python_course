import jsonschema
import pytest
import requests
from examples import base_urls
from examples.schemas import specific_post_schema, comments_by_post_schema, all_users_schema, specific_user_schema, \
    user_posts_schema


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_specific_post(post_id):
    """
    Test the API endpoint to retrieve a specific post.

    :param post_id: the post id to retrieve
    """
    response = requests.get(f"{base_urls.BASE_URL_JSON_PLACE_HOLDER}/posts/{post_id}")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=specific_post_schema)


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments_by_post(post_id):
    """
    Test the API endpoint to retrieve comments for a specific post.

    :param post_id: the post id to retrieve comments for
    """
    response = requests.get(f"{base_urls.BASE_URL_JSON_PLACE_HOLDER}/comments?postId={post_id}")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=comments_by_post_schema)


def test_get_all_users():
    """
    Test the API endpoint to retrieve all users.
    """
    response = requests.get(f"{base_urls.BASE_URL_JSON_PLACE_HOLDER}/users")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=all_users_schema)


def test_get_specific_user(user_id=1):
    """
    Test the API endpoint to retrieve a specific user.

    :param user_id: the user id to retrieve
    """
    response = requests.get(f"{base_urls.BASE_URL_JSON_PLACE_HOLDER}/users/{user_id}")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=specific_user_schema)


def test_get_user_posts(user_id=1):
    """
    Test the API endpoint to retrieve all posts for a specific user.

    :param user_id: the user id to retrieve posts for
    """
    response = requests.get(f"{base_urls.BASE_URL_JSON_PLACE_HOLDER}/posts?userId={user_id}")
    data = response.json()

    assert response.status_code == 200
    jsonschema.validate(instance=data, schema=user_posts_schema)

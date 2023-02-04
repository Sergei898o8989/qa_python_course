import pytest
import requests


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_specific_post(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    data = response.json()

    assert response.status_code == 200
    assert "id" in data and "title" in data and "body" in data


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments_by_post(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/comments?postId={post_id}")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)


def test_get_all_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)


def test_get_specific_user(user_id=1):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    data = response.json()

    assert response.status_code == 200
    assert "name" in data and "id" in data


def test_get_user_posts(user_id=1):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user_id}")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)

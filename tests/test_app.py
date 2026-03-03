import pytest


def test_get_activities_returns_all_activities(client):
    # Arrange: client fixture provided by conftest

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert isinstance(data["Chess Club"]["participants"], list)


def test_root_redirects_to_index(client):
    # Arrange

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code in (301, 302, 307)
    assert response.headers["location"].endswith("/static/index.html")


def test_signup_successful(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json()["message"]
    # verify participant was added
    all_activities = client.get("/activities").json()
    assert email in all_activities[activity]["participants"]


def test_unregister_successful(client):
    # Arrange
    activity = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert "Unregistered" in response.json()["message"]
    all_activities = client.get("/activities").json()
    assert email not in all_activities[activity]["participants"]

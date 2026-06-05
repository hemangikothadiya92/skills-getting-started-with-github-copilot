import pytest
from urllib.parse import quote


@pytest.mark.asyncio
async def test_get_activities(client):
    r = await client.get("/activities")
    assert r.status_code == 200
    data = r.json()
    assert "Chess Club" in data


@pytest.mark.asyncio
async def test_signup_and_remove(client):
    activity = "Chess Club"
    email = "test.user@example.com"

    # Ensure not already signed up
    r = await client.get("/activities")
    assert email not in r.json()[activity]["participants"]

    # Sign up
    r = await client.post(f"/activities/{quote(activity)}/signup", params={"email": email})
    assert r.status_code == 200
    data = (await client.get("/activities")).json()
    assert email in data[activity]["participants"]

    # Remove participant
    r = await client.delete(f"/activities/{quote(activity)}/participants", params={"email": email})
    assert r.status_code == 200
    data = (await client.get("/activities")).json()
    assert email not in data[activity]["participants"]

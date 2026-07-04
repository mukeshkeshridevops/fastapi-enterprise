def test_users(client):
    client.post("/api/v1/users", json={"id": 1, "username": "u", "email": "u@e.com"})
    r = client.get("/api/v1/users")
    assert r.status_code == 200
    assert len(r.json()) >= 1

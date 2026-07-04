def test_login_success(client):
    r=client.post("/api/v1/auth/login",json={"username":"admin","password":"admin"})
    assert r.status_code==200
    assert "access_token" in r.json()
def test_login_fail(client):
    r=client.post("/api/v1/auth/login",json={"username":"x","password":"y"})
    assert r.status_code==401

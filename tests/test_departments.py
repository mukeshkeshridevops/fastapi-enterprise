def test_departments(client):
    client.post("/api/v1/departments",json={"id":1,"name":"IT"})
    r=client.get("/api/v1/departments")
    assert r.status_code==200
    assert len(r.json())>=1

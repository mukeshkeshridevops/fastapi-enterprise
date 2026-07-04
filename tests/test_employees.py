def test_employees(client):
    client.post("/api/v1/employees",json={"id":1,"name":"A","department_id":10,"salary":100.0})
    r=client.get("/api/v1/employees")
    assert r.status_code==200
    assert len(r.json())>=1

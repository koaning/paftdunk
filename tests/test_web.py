from starlette.testclient import TestClient

from paftdunk.web import app

client = TestClient(app)

def test_root_endpoint():
    resp = client.get("/")
    assert resp.status_code == 200

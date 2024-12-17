import json
from src.app import app

def test_predict_endpoint():
    client = app.test_client()
    response = client.post('/predict', 
                           data=json.dumps({"input": [1,2,3]}),
                           content_type='application/json')
    data = response.get_json()
    assert "result" in data
    assert response.status_code == 200

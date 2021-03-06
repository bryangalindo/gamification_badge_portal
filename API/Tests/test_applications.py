from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


test_application_dict = {
            "PartitionKey": "test4@test.com", 
            "RowKey": "6", 
            "requests": [
                {
                    "PartitionKey": "test3@test.com", "RowKey": "6", "ApplicationID": "6", 
                    "badgeID": "1", "category": "Milestone", "approved": False, "approved_by": ""
                    },
                {
                    "PartitionKey": "test7@test.com", "RowKey": "7", "ApplicationID": "6", 
                    "badgeID": "1", "category": "Milestone", "approved": False, "approved_by": ""
                    },
                ]
            }

def test_post_application():
    response = client.post("/api/v1/applications/", json=test_application_dict)
    assert response.status_code == 200
    assert response.json() == test_application_dict
    
def test_delete_application():
    response = client.delete("/api/v1/applications/6")
    assert response.status_code == 200
    assert response.json() == {"Details": "Application deleted"}


def test_read_all_applications():
    response = client.get("/api/v1/applications/")
    applications = response.json()
    assert response.status_code == 200
    assert applications[0]['PartitionKey'] == 'test1@test.com'
    assert applications[0]['RowKey'] == '1'
    assert applications[1]['PartitionKey'] == 'test2@test.com'
    assert applications[1]['RowKey'] == '2'


def test_read_application_1():
    response = client.get("/api/v1/applications/1")
    application = response.json()
    badge_requests = application['requests']
    assert response.status_code == 200
    assert application['PartitionKey'] == 'test1@test.com'
    assert application['RowKey'] == '1'
    assert badge_requests[0]['PartitionKey'] == 'test1@test.com'
    assert badge_requests[0]['RowKey'] == '1'


def test_read_application_2():
    response = client.get("/api/v1/applications/2")
    application = response.json()
    badge_requests = application['requests']
    assert response.status_code == 200
    assert application['PartitionKey'] == 'test2@test.com'
    assert application['RowKey'] == '2'
    assert badge_requests[0]['PartitionKey'] == 'test2@test.com'
    assert badge_requests[0]['RowKey'] == '3'
    
    
def test_read_nonexistent_item():
    response = client.get("/api/v1/applications/3")
    assert response.status_code == 404
    assert response.json() == {"detail": "Application not found"}

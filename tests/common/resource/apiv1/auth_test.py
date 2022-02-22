import pytest, json
from time import time

@pytest.mark.parametrize(
	("headers", "body", "status", "code"),
	[
		({}, {}, 415, 101), # Invalid media type
		({"Content-Type": "application/json"}, {"username": 1,"password": 1}, 400, 104), # Read and validate user data.(int input)
		({"Content-Type": "application/json"}, {"username": "","password": "pass1"}, 400, 105), # Empty username.
		({"Content-Type": "application/json"}, {"username": "user1","password": ""}, 400, 105), # Empty password.
#		({"Content-Type": "application/json"}, {"username": "username","password": "pass"}, 500, 102), # Database error. 
		({"Content-Type": "application/json"}, {"username": "user","password": "pass1"}, 401, 103), # user is not found.
		({"Content-Type": "application/json"}, {"username": "user1","password": "oldpass"}, 401, 111), # Invalid password
		({"Content-Type": "application/json"}, {"username": "user1","password": "pass"}, 200, 100), # Token encryption
		({"Content-Type": "application/json"}, {"username": "user2","password": "test"}, 401, 108), # user is expired. 
		({"Content-Type": "application/json"}, {"username": "user3","password": "test"}, 401, 109), # Bad user status. 
	]
)
def test_create_jwt_token(client, headers, body, status, code):
	result = client.post(
		"/api/v1/auth/tokens",
		data=json.dumps(body),
		headers=headers
	)
	
	assert result.status_code == status
	assert result.get_json()["code"] == code
	
	
	
	
@pytest.mark.parametrize(
	("headers", "body", "status", "code"),
	[
		({}, {}, 501, 107), # Not Implemented 
	]

)
def test_verify_jwt_token(client, headers, body, status, code):
	result = client.get(
		"/api/v1/auth/tokens",
		data=json.dumps(body),
		headers=headers
	)
	
	assert result.status_code == status
	assert result.get_json()["code"] == code

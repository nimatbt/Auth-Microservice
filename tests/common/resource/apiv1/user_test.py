############### 21-1 : 1.23' ############

import pytest, json


user_id = "id"
################### Test Create User ###################################
@pytest.mark.parametrize(
	("headers", "body", "status", "code"),
	[
		({}, {}, 415, 101), # Invalid media type
		({"Content-Type": "application/json"}, {"username": 1,"password": 1}, 400, 104), # Read and validate user data.(int input)
		({"Content-Type": "application/json"}, {"username": "","password": "pass"}, 400, 105), # Empty username.
		({"Content-Type": "application/json"}, {"username": "test","password": ""}, 400, 105), # Empty password.
#		({"Content-Type": "application/json"}, {"username": "username","password": "pass"}, 500, 102), # Database error. 
		({"Content-Type": "application/json"}, {"username": "test","password": "pass"}, 201, 100), # Create new user. 
		({"Content-Type": "application/json"}, {"username": "test","password": "pass"}, 409, 106), # user is already exist. 
	]
)
def test_create_user(client, headers, body, status, code):
	result = client.post(
		"/api/v1/users",
		data=json.dumps(body),
		headers=headers
	)
	assert result.status_code == status
	assert result.get_json()["code"] == code
	
	try:
		global user_id
		user_id = result.get_json()["user"]["id"]
	except:
		pass
	
	
	
##################### Test get Users ###################################
@pytest.mark.parametrize(
	("headers", "body", "status", "code"),
	[
		({}, {}, 415, 101), # Invalid media type
#		({"Content-Type": "application/json"}, {}, 500, 102), # Database error. 
		({"Content-Type": "application/json"}, {}, 200, 100), # users list. 
	]
)
def test_get_users(client, headers, body, status, code):
	result = client.get(
		"/api/v1/users",
		data=json.dumps(body),
		headers=headers
	)
	assert result.status_code == status
	assert result.get_json()["code"] == code
	
	
	
	
	
	
##################### Test get one User ################################
@pytest.mark.parametrize(
	("headers", "body", "status", "code", "userid"),
	[
		({}, {}, 415, 101, "userid"), # Invalid media type
#		({"Content-Type": "application/json"}, {}, 500, 102), # Database error. 
		({"Content-Type": "application/json"}, {}, 404, 103, "userid"), # user is not found.
		({"Content-Type": "application/json"}, {}, 200, 100, ""), # user found. 
	]
)
def test_get_user(client, headers, body, status, code, userid):
	result = client.get(
		"/api/v1/users/" + user_id + userid,
		data=json.dumps(body),
		headers=headers
	)
	assert result.status_code == status
	assert result.get_json()["code"] == code
	
	
	
	
	
	
##################### Test update User #################################
@pytest.mark.parametrize(
	("headers", "body", "status", "code", "userid"),
	[
		({}, {}, 415, 101, "userid"), # Invalid media type
		({"Content-Type": "application/json"}, {"password": 1,"oldpassword": 1}, 400, 104, ""), # Read and validate user data.(int input)
		({"Content-Type": "application/json"}, {"password": "pass"}, 400, 104, ""), # Read and validate user data.(only password)
		({"Content-Type": "application/json"}, {"password": "pass", "user": "user"}, 400, 104, ""), # Read and validate user data.(no oldpassword)
		({"Content-Type": "application/json"}, {"user": "user", "oldpassword": "oldpass"}, 400, 104, ""), # Read and validate user data.(no password)
		({"Content-Type": "application/json"}, {"password": "","oldpassword": "oldpass"}, 400, 105, ""), # Empty password.
		({"Content-Type": "application/json"}, {"password": "pass","oldpassword": ""}, 400, 105, ""), # Empty oldpassword.
#		({"Content-Type": "application/json"}, {"username": "username","password": "pass"}, 500, 102, "userid"), # Database error. 
		({"Content-Type": "application/json"}, {"password": "user","oldpassword": "pass"}, 404, 103, "userid"), # user is not found. 
		({"Content-Type": "application/json"}, {"password": "newpass","oldpassword": "oldpass"}, 403, 111, ""), # unmach oldpassword
		({"Content-Type": "application/json"}, {"password": "newpass","oldpassword": "pass"}, 200, 100, "") # update password
	]
)
def test_update_user(client, headers, body, status, code, userid):
	result = client.patch(
		"/api/v1/users/" + user_id + userid,
		data=json.dumps(body),
		headers=headers
	)
	assert result.status_code == status
	assert result.get_json()["code"] == code
	
	
	

##################### Test delete User #################################
@pytest.mark.parametrize(
	("headers", "body", "status", "code", "userid"),
	[
		({}, {}, 415, 101, "userid"), # Invalid media type
#		({"Content-Type": "application/json"}, {"username": "username","password": "pass"}, 500, 102, "userid"), # Database error. 
		({"Content-Type": "application/json"}, {}, 404, 103, "userid2"), # user is not found. 
		({"Content-Type": "application/json"}, {}, 200, 100, "") # Delete user
	]
)
def test_delete_user(client, headers, body, status, code, userid):
	result = client.delete(
		"/api/v1/users/" + user_id + userid,
		data=json.dumps(body),
		headers=headers
	)
	assert result.status_code == status
	assert result.get_json()["code"] == code
	
	

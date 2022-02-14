##### 20-1 : 49' ########

from flask import request
from jwt import encode, decode
from authz.util import jsonify, now

from authz.schema.apiv1 import UserSchema # 21-1 : 8'
from authz.model import User
from authz.config import Config
from time import time
from authz.authz import db

class AuthController:
	
	def create_jwt_token(): # 21-1 : 7'
		if request.content_type != "application/json":
			return jsonify(status=415, code=101) # Invalid media type.
		user_schema = UserSchema(only=["username", "password"])
		try:
			user_data = user_schema.load(request.get_json()) # validate user request.
		except:
			return jsonify(status=400, code=104)
		if not user_data.get("username") or not user_data.get("password"):
			return jsonify(status=400, code=105) # Empty data.
		try:
			user = User.query.filter_by(username=user_data.get("username")).first() # Find the User
		except:
			return jsonify(status=500, code=102) # Database error.
		if user is None:
			return jsonify(status=401, code=103) # user is not found.
		if user.password != user_data.get("password"):
			user.failed_auth_at = now()
			user.failed_auth_count += 1
			try:
				db.session.commit()
			except:
				db.session.rollback()
				return jsonify(status=500, code=102) # Database error.
			return jsonify(status=401, code=111) # Invalid password
		if user.expires_at < now():
			return jsonify(status=401, code=108) # user is expired.
		if user.status != Config.USER_ALL_STATUS:
			return jsonify(status=401, code=109) # Bad user status.
		current_time = time()
		try:
			user_jwt_token = encode(
				{
					"sub": user.id,
					"exp": current_time + Config.USER_DEFAULT_TOKEN_EXPIRY_TIME,
					"nbf": current_time,
					"resource": "user",
					"data": {
						"id": user.id,
						"username": user.username,
						"role": user.role,
					}
				},
				Config.SECRET_KEY,
				Config.JWT_ALGO
			).encode("utf8") # create JWT token.
		except:
			return jsonify(status=500, code=111) # Token encryption error.
		user.last_login_at = now()
		try:
			db.session.commit()
		except:
			db.session.rollback()
			return jsonify(status=500, code=102) # Database error.
		user_schema = UserSchema()
		return jsonify(
			state={"user": user_schema.dump(user)},
			headers={"X-subject-Token": user_jwt_token}
		) # Return JWT  token in addition to user info.


	def verify_jwt_token():
		return jsonify(status=501, code=107) # Not Implemented

from flask import request # 19-1 : 37'

from authz.authz import db # 19-1 : 1:07'
from authz.model import User # 18-1 : 47'
from authz.schema.apiv1 import UserSchema
from authz.util import jsonify, user_expires_at, now


class UserController:

	def get_users():
		####### positive model 19-1 : 42' #################
#		if request.content_type == "application/json": # 19-1 : 42'
#			users = User.query.all() # 19-1 :27'
#			users_schema = UserSchema(many=True) # global array
#			return jsonify(
#				{"users": users_schema.dump(users)}
#			)
#		else:
#			return jsonify(status=415, code=101)

		######### Negative model 19-1 : 47' ################
		if request.content_type != "application/json":
			return jsonify(status=415, code=101) # Invalid media type.
		try: # 19-1 : 53'
			users = User.query.all() # 19-1 :27'
		except Exception as e:
			return jsonify(status=500, code=102) # Database error.
		users_schema = UserSchema(many=True) # global array
		return jsonify(
			{"users": users_schema.dump(users)}
		)

		#return jsonify(status=501, code=107) # Not Implemented
		
	def get_user(user_id):
		##### 20-1 : 4' ########
		if request.content_type != "application/json":
			return jsonify(status=415, code=101) # Invalid media type.
		try:
			user = User.query.get(user_id) # Find the user.
		except Exception as e:
			return jsonify(status=500, code=102) # Database error.
			
		if user is None:
			return jsonify(status=404, code=103) # user is not found.
		user_schema = UserSchema()
		return jsonify({"user": user_schema.dump(user)})
			
			
			
#		return jsonify(status=501, code=107) # Not Implemented
		
	def create_user():
		##### 19-1 : 58' #######
		if request.content_type != "application/json":
			return jsonify(status=415, code=101) # Invalid media type.
		user_schema = UserSchema(only=["username", "password"])
		try:
			user_data = user_schema.load(request.get_json()) # Read and validate user data.
		except Exception as e:
			return jsonify(status=400, code=104)
		if not user_data.get("username") or not user_data.get("password"):
			return jsonify(status=400, code=105) # Empty data.
		try:
			user = User.query.filter_by(username=user_data.get("username")).first()
		except Exception as e:
			return jsonify(status=500, code=102) # Database error.
		if user is not None:
			return jsonify(status=409, code=106) # user is already exist.
		user = User(
		    username=user_data.get("username"),
		    password=user_data.get("password")
		) # Create new user.
		db.session.add(user)
		try:
			db.session.commit() # Execute INSERT command.
		except Exception as e:
			db.session.rollback()
			return jsonify(status=500, code=102) # Database error.
		
		user_schema = UserSchema()
		return jsonify({"user": user_schema.dump(user)}, status=201)
		
		
#		return jsonify(status=501, code=107) # Not Implemented
		
	def update_user(user_id):
		########## 20-1 : 8' #############
		if request.content_type != "application/json":
			return jsonify(status=415, code=101) # Invalid media type.
		user_schema = UserSchema(only=["password"], unknown="include")
		try:
			user_data = user_schema.load(request.get_json()) # Read and validate user data.
		except Exception as e:
			return jsonify(status=400, code=104)
		if len(user_data) != 2:
			return jsonify(status=400, code=104)
		if "password" not in user_data or "oldpassword" not in user_data:
			return jsonify(status=400, code=104)
		if not user_data.get("password") or not user_data.get("oldpassword"):
			return jsonify(status=400, code=105) # Empty data.
		try:
			user = User.query.get(user_id) # Find the user.
		except Exception as e:
			return jsonify(status=500, code=102) # Database error.
		if user is None:
			return jsonify(status=404, code=103) # user is not found.
		if user.password != user_data.get("oldpassword"):
			return jsonify(status=403, code=111)
		user.password = user_data.get("password") # set a new password
		user.expires_at = user_expires_at()
		user.last_change_at = now()
		user.failed_auth_at = None
		user.failed_auth_count = 0
		try:
			db.session.commit() # Execute UPDATE command.
		except Exception as e:
			db.session.rollback()
			return jsonify(status=500, code=102) # Database error.
		user_schema = UserSchema()
		return jsonify({"user": user_schema.dump(user)})
		
		
#		return jsonify(status=501, code=107) # Not Implemented
		
	def delete_user(user_id):
		##### 20-1 : 40' ###########
		if request.content_type != "application/json":
			return jsonify(status=415, code=101) # Invalid media type.
		try:
			user = User.query.get(user_id) # Find the user.
		except Exception as e:
			return jsonify(status=500, code=102) # Database error.
		if user is None:
			return jsonify(status=404, code=103) # user is not found.
		db.session.delete(user)
		try:
			db.session.commit() # Execute DELETE command.
		except Exception as e:
			db.session.rollback()
			return jsonify(status=500, code=102) # Database error.
		return jsonify() # user was deleted successfuly.
			
			
			
			
#		return jsonify(status=501, code=107) # Not Implemented

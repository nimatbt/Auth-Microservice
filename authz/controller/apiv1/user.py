from authz.model import User # 18-1 : 47'
from authz.util import jsonify

class UserController:
	
	def get_users():
		return jsonify(status=501, code=107) # Not Implemented
		
	def get_user(user_id):
		return jsonify(status=501, code=107) # Not Implemented
		
	def create_user():
		return jsonify(status=501, code=107) # Not Implemented
		
	def update_user(user_id):
		return jsonify(status=501, code=107) # Not Implemented
		
	def delete_user(user_id):
		return jsonify(status=501, code=107) # Not Implemented

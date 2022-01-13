####################### 17-1 : 52' ##############################
from uuid import uuid4
from authz.authz import db

class User(db.model):
	
	id = db.Column(db.String(64), primary_key=True, default=lambda : uuid4().hex)
	username = db.Column(db.String(128), unique=True, index=True, nullable=False)
	password = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(32), nullable=False, default="USER_DEFAULT_ROLE")
	created_at = db.Column(db.DateTime, nullable=False, default="")	
	expires_at = db.Column(db.DateTime, nullable=False, default="USER_DEFAULT_EXPIRY_TIME")
	last_login_at = db.Column(db.DateTime, nullable=True, default=None)
	last_active_at = db.Column(db.DateTime, nullable=True, default=None)	
	last_change_at = db.Column(db.DateTime, nullable=True, default=None)
	failed_auth_at = db.Column(db.DateTime, nullable=True, default=None)	
	failed_auth_count = db.Column(db.Integer, nullable=False, default=0) 
	status = db.Column(db.Integer, nullable=False, default="USER_DEFAULT_STATUS") 
	
	

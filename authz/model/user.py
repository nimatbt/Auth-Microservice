####################### 17-1 : 52' ##############################
from uuid import uuid4

from authz.authz import db
from authz.config import Config  # 18-1 :24'
from authz.util import now, user_expires_at # 18-1 : 38'

class User(db.Model):
	
	id = db.Column(db.String(64), primary_key=True, default=lambda : uuid4().hex)
	username = db.Column(db.String(128), unique=True, index=True, nullable=False)
	password = db.Column(db.String(256), nullable=False)
	role = db.Column(db.String(32), nullable=False, default=Config.USER_DEFAULT_ROLE) # 18-1 : 26'
	created_at = db.Column(db.DateTime, nullable=False, default=now) # 18-1 : 39'
	expires_at = db.Column(db.DateTime, nullable=False, default=user_expires_at) # 18-1 : 39'
	last_login_at = db.Column(db.DateTime, nullable=True, default=None)
	last_active_at = db.Column(db.DateTime, nullable=True, default=None)
	last_change_at = db.Column(db.DateTime, nullable=True, default=None)
	failed_auth_at = db.Column(db.DateTime, nullable=True, default=None)
	failed_auth_count = db.Column(db.Integer, nullable=False, default=0) 
	status = db.Column(db.Integer, nullable=False, default=Config.USER_DEFAULT_STATUS) # 18-1 : 26'

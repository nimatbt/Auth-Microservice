from os import environ

class Config:
	
	#################### Aplication Config ###########################
	
	ENV = environ.get("AMIMA_AUTHZ_ENV", "production")
	
	DEBUG = bool(int(environ.get("AMIMA_AUTHZ_DEBUG", "0")))
	
	TESTING = bool(int(environ.get("AMIMA_AUTHZ_TESTING", "0")))
	
	SECRET_KEY = environ.get("AMIMA_AUTHZ_SECRET_KEY", "SECRET-KEY")
	
	TIMEZONE = environ.get("AMIMA_AUTHZ_TIMEZONE", "Asia/Tehran") # 18-1 : 27'
	
	JWT_ALGO = environ.get("AMIMA_AUTHZ_JWT_ALGO", "HS512") # 21-1 : 22'
	
	################### Database Config ####### 17-1 : 37' ############
	
	SQLALCHEMY_DATABASE_URI = environ.get("AMIMA_AUTHZ_DATABASE_URI", None)
	
	SQLALCHEMY_ECHO = DEBUG
	
	SQLALCHEMY_RECORD_QUERIES = DEBUG
	
	SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
	
	################### User Config ####### 17-1 : 1:15' ############
	
	USER_DEFAULT_ROLE = environ.get("AMIMA_AUTHZ_USER_DEFAULT_ROLE", "member")
	
	USER_DEFAULT_EXPIRY_TIME = int(environ.get("AMIMA_AUTHZ_USER_DEFAULT_EXPIRY_TIME", "365"))
	
	USER_DEFAULT_STATUS = int(environ.get("AMIMA_AUTHZ_USER_DEFAULT_STATUS", "3"))
	
	USER_ENABLED_STATUS = 1 # 21-1 : 20'
	
	User_ACTIVATED_STATUS = 2
	
	USER_ALL_STATUS = 3
	
	USER_DEFAULT_TOKEN_EXPIRY_TIME = int(environ.get("AMIMA_AUTHZ_USER_DEFAULT_TOKEN_EXPIRY_TIME", "86400")) # 21-1 : 26'
	

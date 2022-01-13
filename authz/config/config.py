from os import environ

class Config:
	
	#################### Aplication Config ###########################
	
	ENV = environ.get("AMIMA_AUTHZ_ENV", "production")
	
	DEBUG = bool(int(environ.get("AMIMA_AUTHZ_DEBUG", "0")))
	
	TESTING = bool(int(environ.get("AMIMA_AUTHZ_TESTING", "0")))
	
	SECRET_KEY = environ.get("AMIMA_AUTHZ_SECRET_KEY", "SECRET-KEY")
	
	################### Database Config ####### 17-1 : 37' ############
	
	SQLALCHEMY_DATABASE_URI = environ.get("AMIMA_AUTHZ_DATABASE_URI", None)
	
	SQLALCHEMY_ECHO = DEBUG
	
	SQLALCHEMY_RECORD_QUERIES = DEBUG
	
	SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG

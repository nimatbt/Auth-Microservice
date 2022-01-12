from os import environ

class Config:
	
	ENV = environ.get("AMIMA_AUTHZ_ENV", "production")
	
	DEBUG = bool(int(environ.get("AMIMA_AUTHZ_DEBUG", "0")))
	
	TESTING = bool(int(environ.get("AMIMA_AUTHZ_TESTING", "0")))
	
	SECRET_KEY = environ.get("AMIMA_AUTHZ_SECRET_KEY", "secret-key")
	

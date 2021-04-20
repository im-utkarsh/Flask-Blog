import os


class Config:
    SECRET_KEY = "4948d2d8b93d58cb96200fb3d8ba4593"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")

import os


class Config:
    SECRET_KEY = "4948d2d8b93d58cb96200fb3d8ba4593"
    SQLALCHEMY_DATABASE_URI = "postgres://qoetapoefbudwg:e5c808a162fb657f8b099adf6cfdd7c9343ff59327c9f1ae2f40385d651f63a9@ec2-34-206-8-52.compute-1.amazonaws.com:5432/d553m6arlp463b"
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")

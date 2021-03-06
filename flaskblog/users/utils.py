import os
import secrets

from flask import current_app, url_for
from flask_login import current_user
from flask_mail import Message
from flaskblog import mail
from PIL import Image


def save_picture(form_picture):
    prev_picture = os.path.join(
        current_app.root_path, "static/profile_pics", current_user.image_file
    )
    if os.path.exists(prev_picture) and os.path.basename(prev_picture) != "default.jpg":
        os.remove(prev_picture)
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, "static/profile_pics", picture_fn
    )
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request", sender="noreply@demo.com", recipients=[user.email]
    )
    msg.body = f"""To reset your passsword, visit this link:
{url_for('users.reset_token', token=token, _external=True)}

If this request was not made by you, then please ignore this email.
"""
    mail.send(msg)

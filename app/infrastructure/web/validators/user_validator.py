# app/infrastructure/web/validators/user_validator.py
from wtforms import Form, StringField, validators
from wtforms.validators import ValidationError
from enum import Enum

class UserRole(Enum):
    ADMIN = 'admin'
    USER = 'user'
    GUEST = 'guest'

class UserValidator(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Email()])
    role = StringField('Role', [validators.AnyOf([role.value for role in UserRole], message="Invalid role")])

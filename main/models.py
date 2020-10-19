from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, form_data):
        errors = {}
        Email_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(form_data['f_name']) < 3:
            errors['f_name'] = "First name must be at least 3 characters!"
        if len(form_data['l_name']) < 4:
            errors['l_name'] = "Last name must be at least 5 characters!"
        if not Email_REGEX.match(form_data['email']):
            errors['email'] = "Email doesn't look right!"
        if len(form_data['email']) < 6:
            errors['email_length'] = "Email got to be 6 characters!"
        if len(form_data['password']) < 8:
            errors['password'] = "Password need to be a minimum of 8 characters"
        if form_data['password'] != form_data['confirm_password']:
            errors['confirm_password'] = "Passwords don't match! Try again!"
        return errors
    def login_validator(self, form_data):
        errors = {}
        Email_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not Email_REGEX.match(form_data['email']):
            errors['email'] = "Email doesn't look right!"
        if len(form_data['email']) < 6:
            errors['email_length'] = "Email got to be 6 characters!"
        if len(form_data['password']) < 8:
            errors['password'] = "Password need to be a minimum of 8 characters"
        return errors

class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
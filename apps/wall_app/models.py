from django.db import models
from datetime import date, time, datetime, timedelta

from ..login_app.models import User

class ValidateManager(models.Manager):
    def msgValidation(self, post_data):
        errors={}
        return errors

    def cmntValidation(self, post_data):
        errors={}
        return errors

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    message_txt = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ValidateManager()

class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE)
    comment_txt = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ValidateManager()
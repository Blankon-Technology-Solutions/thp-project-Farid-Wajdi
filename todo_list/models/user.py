from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Fields for Google SSO
    google_id = models.CharField(max_length=255, blank=True, null=True)
    google_access_token = models.CharField(max_length=255, blank=True, null=True)
    google_refresh_token = models.CharField(max_length=255, blank=True, null=True)

    # Fields for LinkedIn SSO
    linkedin_id = models.CharField(max_length=255, blank=True, null=True)
    linkedin_access_token = models.CharField(max_length=255, blank=True, null=True)
    linkedin_refresh_token = models.CharField(max_length=255, blank=True, null=True)

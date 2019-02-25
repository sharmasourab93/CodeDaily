from django.db import models
from datetime import datetime


# your models here.
class Posts(models.Model):
				title = models.CharField(max_length=30)
				body = models.TextField()
				created_at = models.DateTimeField(default=datetime.now, blank=True)

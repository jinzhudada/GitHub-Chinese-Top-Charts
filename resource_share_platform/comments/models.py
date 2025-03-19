# comments/models.py
from django.db import models
from django.contrib.auth.models import User
from resources.models import Resource  # 假设 Resource 在 resources 应用中

class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments_in_comments',  # 修改这里
    )
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        related_name='comments_in_comments',  # 修改这里
    )
    # 其他字段...
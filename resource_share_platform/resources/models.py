from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Resource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title  # 返回资源标题
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user} liked {self.resource}'

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user} favorited {self.resource}'
    

# resources/models.py
from django.db import models
from django.contrib.auth.models import User
from resources.models import Resource  # 假设 Resource 在 resources 应用中

class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments_in_resources',  # 修改这里
    )
    resource = models.ForeignKey(
        Resource,
        on_delete=models.CASCADE,
        related_name='comments_in_resources',  # 修改这里
    )
    # 其他字段...
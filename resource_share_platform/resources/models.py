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
    


# # 在 models.py 中添加以下代码
# class Comment(models.Model):
#     content = models.TextField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Comment by {self.user.username} on {self.resource.title}"
    

from django.db import models
from django.contrib.auth.models import User
from resources.models import Resource

class Comment(models.Model):
    resource = models.ForeignKey(Resource, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} commented on {self.resource}'
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    """the content of a article"""
    authors = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='用户')
    title = models.CharField(max_length=200)
    content = models.TextField()
    click_nums = models.IntegerField(default=0,verbose_name='阅读数量')
    is_deleted = models.BooleanField(default=False,verbose_name='是否删除')
    created_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'atricles'
 
    def __str__(self):
        """Return a string representation of the model."""
        return f"{self.content[:50]}..."

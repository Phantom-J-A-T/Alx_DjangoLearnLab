from django.db import models

# Create your models here.
class blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="发布日期")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="作者")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = "博客"

    def __str__(self):
        return self.title
    

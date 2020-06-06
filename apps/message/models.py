from django.db import models


class UserMessage(models.Model):
    name = models.CharField("用户名", max_length=20)
    email = models.EmailField("邮箱")
    address = models.CharField("地址", max_length=100)
    message = models.CharField("留言", max_length=200)

    class Meta:
        verbose_name = "用户留言信息"
        verbose_name_plural = verbose_name


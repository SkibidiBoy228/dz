from django.db import models
from django.contrib.auth.models import User

class AccessLog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Користувач",
        related_name="access_logs"
    )
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата та час доступу")
    status = models.IntegerField(verbose_name="Статус відповіді сервера")

    def __str__(self):
        return f"{self.timestamp} — {self.status}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
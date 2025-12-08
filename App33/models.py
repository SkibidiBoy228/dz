from django.db import models

class AccessLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Дата та час доступу")
    status = models.IntegerField(verbose_name="Статус відповіді сервера")

    def __str__(self):
        return f"{self.timestamp} — {self.status}"

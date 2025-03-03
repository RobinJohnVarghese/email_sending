from django.db import models

# Create your models here.


class Email(models.Model):
    recipient = models.EmailField(max_length=100,unique=True)
    subject = models.CharField(max_length=100)
    message = models.TextField(null=True,blank=True)
    send_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Email to {self.recipient} - {self.subject}"
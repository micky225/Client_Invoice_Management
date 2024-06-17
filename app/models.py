from django.db import models

# Create your models here.
class Invoice(models.Model):
    invoice_code = models.CharField(max_length=12, unique=True, blank=True, null=True)
    recipient = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    num_items = models.IntegerField()
    creation_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()


    def __str__(self):
        return f"{self.invoice_code} - {self.recipient}"

    class Meta:
        ordering = ['creation_date']    
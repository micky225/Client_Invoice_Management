from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Invoice
import random
import string

def generate_random_code(length=10):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


@receiver(pre_save, sender=Invoice)
def random_code(sender, instance, **kwargs):
    if not instance.invoice_code:
        instance.invoice_code = generate_random_code()
        while Invoice.objects.filter(invoice_code=instance.invoice_code).exists():
            instance.invoice_code = generate_random_code()



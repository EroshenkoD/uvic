from django.core.validators import RegexValidator
from django.db import models


class Order(models.Model):
    LIST_WEBSITE = [("eCommerce", "eCommerce"), ("Business", "Business"), ("Blog", "Blog"),
                    ("Portfolio", "Portfolio"), ("Event", "Event"), ("Personal", "Personal"),
                    ("Membership", "Membership"), ("Nonprofit", "Nonprofit"), ("Informational", "Informational"),
                    ("Online forum", "Online forum")]

    name_customer = models.CharField(max_length=100)
    phone_customer = models.CharField(
        max_length=15, unique=True,
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                   message="Phone number must be entered in the format: '+XXXXXXXXXXXX'")])
    email_customer = models.EmailField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    type_website = models.CharField(max_length=50, choices=LIST_WEBSITE, default=LIST_WEBSITE[0][0])

    def __str__(self):
        return self.title

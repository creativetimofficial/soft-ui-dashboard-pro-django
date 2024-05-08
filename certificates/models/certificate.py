from django.db import models

class Certificate(models.Model):
    LANGUAGE_CHOICES = ((("EN", "English"), ("FR", "French"), ("AR", "Arabic")))
    name = models.CharField(max_length=246)
    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    description = models.TextField(blank=True)



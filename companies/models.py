from django.db import models

# Create your models here.


class Companies(models.Model):
    STATUS=(
        ("Acquired","Acquired"),
        ("Operating","Operating"),
        ("Closed","Closed"),

    )

    company_name = models.CharField(max_length=250)
    market = models.CharField(max_length=100)
    country_code=models.CharField(max_length=10,null=True,blank=True)
    status = models.CharField(max_length=20, choices = STATUS,
        default = 'Acquired')

    def __str__(self):
        return self.company_name
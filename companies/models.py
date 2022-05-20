from django.db import models

# Create your models here.


class Companies(models.Model):
    STATUS=(
        ("1","Acquired"),
        ("0","Closed"),

    )

    company_name = models.CharField(max_length=250,default="")
    market = models.CharField(max_length=100)
    country_code=models.CharField(max_length=10,null=True,blank=True)
    status = models.CharField(max_length=2, choices = STATUS,
        default = '1')
    founding_year=models.IntegerField(default=2010)
    founding_quarter=models.IntegerField(default=1)


    def __str__(self):
        return self.company_name

class Finance(models.Model):
    name=models.CharField(max_length=250,default="")
    total_investment=models.BigIntegerField()
    seed=models.BigIntegerField()
    venture=models.BigIntegerField()
    equity_crowdfunding=models.BigIntegerField()
    undisclosed=models.BigIntegerField()

    convertible_note=models.BigIntegerField()

    debt_financing=models.BigIntegerField()

    angel=models.BigIntegerField()

    grant_given=models.BigIntegerField()

    private_equity=models.BigIntegerField()

    post_ipo_equity=models.BigIntegerField()

    post_ipo_debt=models.BigIntegerField()

    secondary_market=models.BigIntegerField()

    product_crowdfunding=models.BigIntegerField()

    round_A=models.BigIntegerField()

    round_B=models.BigIntegerField()

    round_C=models.BigIntegerField()

    round_D=models.BigIntegerField()

    round_E=models.BigIntegerField()

    round_F=models.BigIntegerField()

    round_G=models.BigIntegerField()

    round_H=models.BigIntegerField()


    def __str__(self):
        return self.name

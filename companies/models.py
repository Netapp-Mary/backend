from django.db import models

# Create your models here.


class Companies(models.Model):
    STATUS=(
        ("1","Acquired"),
        ("0","Closed"),

    )

    company_name = models.CharField(max_length=250,primary_key=True)
    market = models.CharField(max_length=100)
    country_code=models.CharField(max_length=10,null=True,blank=True)
    status = models.CharField(max_length=2, choices = STATUS,
        default = '1')
    founding_year=models.IntegerField(default=2010)
    founding_quarter=models.IntegerField(default=1)


    def __str__(self):
        return self.company_name

class Finances(models.Model):
    company_name=models.ForeignKey(Companies,on_delete=models.CASCADE)
    total_investment=models.IntegerField()
    seed=models.IntegerField()
    venture=models.IntegerField()
    equity_crowdfunding=models.IntegerField()
    undisclosed=models.IntegerField()
    convertible_note=models.IntegerField()
    debt_financing=models.IntegerField()
    angel=models.IntegerField()
    grant_given=models.IntegerField()
    private_equity=models.IntegerField()
    post_ipo_equity=models.IntegerField()
    post_ipo_debt=models.IntegerField()
    secondary_market=models.IntegerField()
    product_crowdfunding=models.IntegerField()
    round_A=models.IntegerField()
    round_B=models.IntegerField()
    round_C=models.IntegerField()
    round_D=models.IntegerField()
    round_E=models.IntegerField()
    round_F=models.IntegerField()
    round_G=models.IntegerField()
    round_H=models.IntegerField()

    def __str__(self):
        return self.name

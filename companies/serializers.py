from rest_framework import serializers
from companies.models import Companies,Finance

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('company_name', 'market', 'country_code', 'status')
class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = ('name', 'total_investment', 'seed', 'venture','equity_crowdfunding','undisclosed','convertible_note','debt_financing','angel','grant_given','private_equity','post_ipo_equity','post_ipo_debt','secondary_market','product_crowdfunding','round_A','round_B','round_C','round_D','round_E','round_F','round_G','round_H')
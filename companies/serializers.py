from rest_framework import serializers
from companies.models import Companies

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ('company_name', 'market', 'country_code', 'status')
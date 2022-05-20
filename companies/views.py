from rest_framework import generics
from rest_framework import viewsets 
from companies.models import Companies,Finance
from .serializers import CompanySerializer,FinanceSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer

class FinViewSet(viewsets.ModelViewSet):
    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
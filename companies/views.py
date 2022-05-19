from rest_framework import generics
from companies.models import Companies
from .serializers import CompanySerializer

class CompanyAPIView(generics.ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
from django.urls import path
from .views import CompanyAPIView
urlpatterns = [
    path('', CompanyAPIView.as_view()),
]
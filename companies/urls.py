from django.urls import path
from rest_framework import routers
from .views import CompanyViewSet,FinViewSet
router = routers.DefaultRouter()

router.register(r'companies', CompanyViewSet),
router.register(r'finances', FinViewSet),
urlpatterns = router.urls
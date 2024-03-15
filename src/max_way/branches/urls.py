from django.urls import path
from .views import branches

urlpatterns = [
    path("", branches, name='branches'),
]
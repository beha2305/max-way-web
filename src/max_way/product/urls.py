from django.urls import path
from .views import index, bucket

urlpatterns = [
    path("", index, name='index'),
    path("bucket/", bucket, name='bucket')
]
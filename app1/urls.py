from app1.views import app1
from django.urls import path
app_name='app1'
urlpatterns=[
    path('app1/',app1,name='app1'),
]

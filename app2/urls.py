from app2.views import app2
from django.urls import path
app_name='app2'
urlpatterns=[
    path('app2/',app2,name='app2'),
]
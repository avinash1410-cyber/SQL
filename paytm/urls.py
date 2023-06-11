from django.urls import path
from .views import *

urlpatterns = [
    path('pay/', start_payment, name="start_payment"),
    path('response/', handlepayment, name="handlepayment"),
]
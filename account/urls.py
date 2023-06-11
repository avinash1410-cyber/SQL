from django.urls import path,include
from account.views import *

urlpatterns = [
    path('',CustomerAPIView.as_view()),
    path('update/',update_trader.as_view()),
    path('logout/',logout_page),
    path('login/',login_page,name='login'),
    path('register/',register_page),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('test/', testEndPoint, name='test'),
]
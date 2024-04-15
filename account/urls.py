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
    path('buy_stock/', buyStock),
    path('sell_stock/', sellStock),
    path('my_watchlist/', myWatchlist),
    path('add_to_watchlist/', addToWatchlist),
    # path('sell_options/', sellOption),
    # path('buy_options/', buyOption),
    # path('search/<str:query>/',searchTrader),
    # path('trader/<int:pk>/',hireTrader),
    # path('trader/<int:pk>/',seeRecordOfTrader),
    # path('hires_list/',HiresList),
    # path('addBalance/<int:pk>/',addBalance),
    # path('withdrawBalance/<int:pk>/',withdrawBalance),
    # path('status',Status),
    # path('status/<int:pk>',status),
]
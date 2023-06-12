from django.urls import path
from stock.views import Home,StockAPIView,StockSearchAPIView,StockMonthlyAPIView,StockWeeklyAPIView,StockYearlyAPIView

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('weekly/',Home.as_view(),name='home'),
    path('monthly/',Home.as_view(),name='home'),
    path('yearly/',Home.as_view(),name='home'),    
    path('<int:pk>/',StockAPIView.as_view()),
    path('search/<str:query>/',StockSearchAPIView.as_view()),
]
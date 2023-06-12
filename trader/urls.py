from django.urls import path
from trader.views import TraderAPIView

urlpatterns = [
    path('',TraderAPIView.as_view()),
    path('<int:pk>/',TraderAPIView.as_view()),
    path('<int:pk>/clients',TraderAPIView.as_view()),
]
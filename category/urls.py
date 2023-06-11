from django.urls import path
from .views import CategoryAPIView,AvailableCategory

urlpatterns = [
    path('<int:pk>/',CategoryAPIView.as_view()),
    path('',CategoryAPIView.as_view()),
    path('available/',AvailableCategory.as_view()),
]
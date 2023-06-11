from django.urls import path
from .views import DesignsAPIView,DesignProductsAPIView

urlpatterns = [
    path('', DesignsAPIView.as_view()),
    path('<int:pk>/', DesignsAPIView.as_view()),
    path('<int:pk>/product/', DesignProductsAPIView.as_view()),
]
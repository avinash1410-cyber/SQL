from django.urls import path
from .views import WatchlistAPIView,AddDataAPIView

urlpatterns = [
    path('',WatchlistAPIView.as_view(),name="MyWatchlist"),
    path('<int:pk>/',WatchlistAPIView.as_view()),
    path('addData/<int:pk>/',AddDataAPIView.as_view()),
]
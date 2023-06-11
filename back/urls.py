from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
# from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenVerifyView
from .import settings


from django.views.static import serve


static_urlpatterns = [
    re_path(r"^images/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('category/', include('category.urls')),
    path('trader/', include('trader.urls')),
    path('',include('stock.urls')),
    path('watchlist/',include('watchlist.urls')),
    path('order/',include('order.urls')),
    path('design/',include('design.urls')),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("", include(static_urlpatterns)),
    path('paytm/', include('paytm.urls')),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # to import static in deployment
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from rest_framework_simplejwt.views import TokenRefreshView
from core.views import FeedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/feed/', FeedView.as_view()),
    path('api/', include('core.urls')),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
from django.urls import path, include

from common import views

urlpatterns = [
    path('login/', views.UniWikiLoginView.as_view(), name='login'),
    path('api/auth/', include('dj_rest_auth.urls')),
]

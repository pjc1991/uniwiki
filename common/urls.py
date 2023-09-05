from django.urls import path

from common import views

urlpatterns = [
    path('login/', views.UniWikiLoginView.as_view(), name='login'),
]

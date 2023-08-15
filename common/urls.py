from django.urls import path

from common import views

urlpatterns = [
    path('signup/', views.UniWikiSignupView.as_view(), name='signup'),
    path('login/', views.UniWikiLoginView.as_view(), name='login'),
]

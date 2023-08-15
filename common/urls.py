from django.urls import path

from common import views

urlpatterns = [
    path('signup/', views.UniWikiSignupView.as_view(), name='signup'),
]

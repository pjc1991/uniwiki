from django.urls import path, include

from wiki import views

urlpatterns = [
    path('', views.UniWikiListView.as_view(), name='uniwiki-list'),
    path('<int:pk>/', views.UniWikiDetailView.as_view(), name='uniwiki-detail'),
]

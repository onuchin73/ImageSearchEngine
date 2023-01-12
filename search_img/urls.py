from django.urls import path

from . import views


urlpatterns = [
    path('download/', views.search_save, name='download'),
    path('', views.SearchImageView.as_view()),
]

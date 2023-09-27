from django.urls import path

from . import views

app_name:'store'


urlpatterns = [
    path('', views.index, name="index"),
    path('member/add/', views.create_view, name='add'),
    path('member/<int:pk>/', views.update_view, name='change'),

    path('member/ajax/load_courses/', views.load_courses, name='ajax_load_courses'),
]
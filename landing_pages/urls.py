from django.contrib import admin
from django.urls import path
from landing_pages import views

urlpatterns = [
    # path('', views.AboutView.as_view(), name='about'),
    path('', views.register, name='about'),
    path('shein/', views.shein_view, name='shein'),
    path('shein-thanku-link/', views.shein_thanku_link_view, name='shein-thanku-link'),
    path('nespresso/', views.nespresso_view, name='nespresso'),
    path('nespresso-thanku-link/', views.nespresso_thanku_link_view, name='nespresso-thanku-link'),
    path('personal-trainer/', views.personal_trainer_view, name='personal-trainer'),
    path('personal-trainer-thanku-link/', views.personal_trainer_thanku_link_view, name='personal-trainer-thanku-link'),
    path('car-insurance/', views.car_insurance_view, name='car-insurance'),
    path('gym/', views.gym_view, name='gym'),
    path('money-online/', views.money_online_view, name='money-online'),
    # path('yoga_guide', views.VideoPageView.as_view(), name='all_video'),
    path('unsubscribe', views.UnsubscribeView.as_view(), name='unsubscribe'),
]

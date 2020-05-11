from django.contrib import admin
from django.urls import path
from landing_pages import views

urlpatterns = [
    # path('', views.AboutView.as_view(), name='about'),
    path('', views.register, name='about'),
    path('shein', views.shein_view, name='shein'),
    path('nespresso', views.nespresso_view, name='nespresso'),
    path('personal-trainer', views.personal_trainer_view, name='personal-trainer'),
    # path('yoga_guide', views.VideoPageView.as_view(), name='all_video'),
    # path('unsubscribe', views.UnsubscribeView.as_view(), name='unsubscribe')
]

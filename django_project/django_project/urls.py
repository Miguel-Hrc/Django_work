from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('ajouter_emprunter/', views.emprunterFormView, name='emprunter_url'),
    path('ajouter_livre/', views.livreFormView, name='livre_url'),
    path('ajouter_cd/', views.cdFormView, name='cd_url'),
    path('ajouter_dvd/', views.dvdFormView, name='dvd_url'),
    path('ajouter_game/', views.gameFormView, name='game_url'),
    path('bibliothecaire/', views.showView, name='show_url'),
    path('membre/', views.showMediaView, name='showMedia_url'),
    path('', views.View, name='home_url'),


    path('modifier/<int:f_id>/', views.updateViewEmprunter, name='updateEmprunter_url'),

    path('modifier_b/<int:f_id>/', views.updateViewBook, name='updateBook_url'),

    path('modifier_c/<int:f_id>/', views.updateViewCd, name='updateCd_url'),

    path('modifier_d/<int:f_id>/', views.updateViewDvd, name='updateDvd_url'),

    path('modifier_g/<int:f_id>/', views.updateViewGame, name='updateGame_url'),
]

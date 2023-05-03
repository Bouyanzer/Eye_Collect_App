from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.login, name='login'),
    path('login.html', views.login, name='login'),
    path('Page_Accueil.html', views.accueil, name='accueil'),
    path('Patient.html', views.patient, name='patient'),
    path('Consultation.html', views.consultation, name='consultation'),
    path('showpat/<str:nom>/<str:prenom>', views.showpat, name='showpat'),
    path('editpat/<str:nom>/<str:prenom>', views.editpat, name='editpat'),
    path('showimg/<str:nom>/<str:prenom>', views.showimg, name='showimg'),
    path('updatepat', views.updatepat, name='updatepat'),
    path('updatecons', views.updatecons, name='updatecons'),
    path('showcons/<str:nom>/<str:prenom>/<str:date>', views.showcons, name='showcons'),
    path('editconsultation/<str:nom>/<str:prenom>/<str:date>', views.editconsultation, name='editconsultation'),
    path('showimg/<str:nom>/<str:prenom>', views.showdates, name='showdates'),
    path('logout.html', views.userlogout, name="userlogout"),
    path('reset_password/', authViews.PasswordResetView.as_view(
        template_name="eyecollect/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', authViews.PasswordResetDoneView.as_view(
        template_name="eyecollect/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(
        template_name="eyecollect/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', authViews.PasswordResetCompleteView.as_view(
        template_name="eyecollect/password_reset_done.html"), name="password_reset_complete"),
    

]


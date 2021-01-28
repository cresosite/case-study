from django.urls import path
from case_study import views

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),
    ###### PATHS ADDED BY ME #######
    path('about/', views.about, name="about"),
    path('study_reponse/', views.study_reponse, name="study_reponse"),

]

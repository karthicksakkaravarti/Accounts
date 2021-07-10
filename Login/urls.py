from django.urls import path, include
from . import (views, router)

app_name = "Login"

urlpatterns = [
    path('', views.LoginView.as_view()),    # Login Root url
    path('Signin/', views.SignInView.as_view(), name='signin'),    # Login Page

]
urlpatterns += router.router.urls
from django.urls import path
from .views import SignUpView, custom_logout_view

urlpatterns = [
    path("logout/", custom_logout_view, name='logout'),
    path("signup/", SignUpView.as_view(), name="signup"),
]

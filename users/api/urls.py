from django.urls import path
from .views import CustomeUserApiView

urlpatterns = [
    path("users/",CustomeUserApiView.as_view(),name="customeuserapi")
]

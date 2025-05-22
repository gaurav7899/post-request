from django.urls import path
from bank import views
urlpatterns = [
    path("home/",views.demo,name="demo"),
    path("success/",views.reg_success,name="reg_success")
]

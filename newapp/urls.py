from django.urls import path
from newapp import views

urlpatterns = [
    path(
        "",
        view=views.home,
        name="home",
    ),
    path(
        "customer/add/",
        view=views.add_customer,
        name="add_customer",
    ),
]

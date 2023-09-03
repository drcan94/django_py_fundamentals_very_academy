from django.shortcuts import render
from django.http import HttpResponseRedirect

# import random
# from django.contrib.auth.models import User
from newapp.models import Customer
from newapp.forms import CustomerForm


def home(request):
    title = "Home Page"

    # all_users = User.objects.all()
    # for i in all_users:
    #     print(i.username)

    # Customer.objects.create(name="John",
    #                         age=random.randint(15, 25),
    #                         mobile=1234567890)

    # filtered_customers -> QuerySet for all customers with age > 20
    filtered_customers = Customer.objects.filter(age__gt=20)
    # __gt -> greater than

    # for i in filtered_customers:
    #     print(i.name, i.age)

    # queryset slicing
    # filtered_customers2 = Customer.objects.filter(age__gt=20)[0:2]
    # but negative indexing is not allowed
    # print("filtered_customers2 with slicing")
    # for i in filtered_customers2:
    #     print(i.name, i.age)
    return render(
        request,
        template_name="index.html",
        context={
            "title": title,
            "customers_gt_20": filtered_customers,
        },
    )


def add_customer(request):
    title = "Add Customer"

    if request.method == "POST":
        formset = CustomerForm(request.POST)

        if formset.is_valid():
            # name = request.POST["name"]
            # age = request.POST["age"]
            # mobile = request.POST["mobile"]

            # Customer.objects.create(name=name, age=age, mobile=mobile)

            formset.save()
            # this will save the data in the database,
            # no need to use Customer.objects.create() method

            return HttpResponseRedirect("/")

        return render(
            request,
            template_name="add_customer.html",
            context={
                "title": title,
                "formset": formset,
            },
        )
    else:
        formset = CustomerForm()

        return render(
            request,
            template_name="add_customer.html",
            context={
                "title": title,
                "formset": formset,
            },
        )

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse
from app.forms import OrderForm
from app.models import Order
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    context = {}

    return render(request, "index.html", context)


def about(request):
    context = {}

    return render(request, "about.html", context)


def contact(request):
    context = {}

    return render(request, "contact.html", context)


@login_required(login_url="/login/")
def order(request):
    order = Order.objects.filter(user=User.objects.get(id=request.user.id))
    context = {
        "order": order,
    }
    if request.method == "POST":
        form = OrderForm(request.POST)
        user = User.objects.get(id=request.user.id)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
            # save the form data to model

    context["form"] = OrderForm()

    return render(request, "order.html", context)


def delete_order(request, id):
    context = {}
    Order.objects.get(id=id).delete()

    return HttpResponseRedirect(redirect_to=reverse("order"))

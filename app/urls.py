from django.urls import path

from app.views import about, contact, index, order, delete_order

urlpatterns = [
    path("", index, name="home"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("order/", order, name="order"),
    path("order/<id>/delete", delete_order, name="order_delete"),
]

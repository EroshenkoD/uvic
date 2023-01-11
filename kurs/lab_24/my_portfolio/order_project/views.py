from django.shortcuts import render
from django.template.response import TemplateResponse

from .forms import OrderForm
from .models import Order


def index(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            comment = Order(
                name_customer=form.cleaned_data["name_customer"],
                phone_customer=form.cleaned_data["phone_customer"],
                email_customer=form.cleaned_data["email_customer"],
                title=form.cleaned_data["title"],
                body=form.cleaned_data["body"],
                type_website=form.cleaned_data["type_website"],
            )
            comment.save()
            return TemplateResponse(request, 'order_project/redirect_success.html')
    context = {"form": form}
    return render(request, "order_project/index.html", context)



from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/login/illustration-login/")
def index(request):
    options = [
        {"label": "Certificates", "url": "/certificates"},
        {"label": "Diplomas", "url": "/certificates/diploma"},
    ]
    template = "pages/dashboards/default.html"
    context = {"parent": "dashboard", "segment": "home", "options_list": options}
    return render(request, template, context=context)

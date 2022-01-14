# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
            
        segment, active_menu = get_segment( request )
        
        context['segment']     = segment
        context['active_menu'] = active_menu

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

# Helper - Extract current page name from request 
def get_segment( request ): 

    try:

        segment     = request.path.split('/')[-1]
        active_menu = None

        if segment == '' or segment == 'index.html':
            segment     = 'index'
            active_menu = 'dashboard'

        if segment.startswith('dashboards-'):
            active_menu = 'dashboard'

        if segment.startswith('account-') or segment.startswith('users-') or segment.startswith('profile-') or segment.startswith('projects-'):
            active_menu = 'pages'

        if  segment.startswith('notifications') or segment.startswith('sweet-alerts') or segment.startswith('charts.html') or segment.startswith('widgets') or segment.startswith('pricing'):
            active_menu = 'pages'            

        return segment, active_menu     

    except:
        return 'index', 'dashboard'  

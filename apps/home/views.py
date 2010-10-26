from django.shortcuts import render_to_response
from django.template import RequestContext

from beer.models import Beer


def index(request, template_name="home.html"):
    beers = Beer.objects.all().order_by('name')
    return render_to_response(template_name, {'beers': beers},
        context_instance=RequestContext(request))

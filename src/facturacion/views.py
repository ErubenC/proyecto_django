from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


def facturacion_view(request):
    return render_to_response("facturacion/base.html", context_instance=RequestContext(request))

def marca_view(request):
    return render_to_response("base.html", context_instance=RequestContext(request))






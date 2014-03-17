from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.template import RequestContext
'''´ '''
def index_view(request):
    return render_to_response('base.html', context_instance=RequestContext(request))

def login_view(request):
    return render_to_response('home/login.html', context_instance=RequestContext(request))
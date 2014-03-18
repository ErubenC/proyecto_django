from django.shortcuts import render, render_to_response
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.template import RequestContext
from home.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User, Group


def index_view(request):
    return render_to_response('base.html', context_instance=RequestContext(request))
'''
def login_view(request):
    return render_to_response('home/login.html', context_instance=RequestContext(request))
    '''

def login_view(request):
    mensaje = ""
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index')
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username,password=password)
                if usuario is not None and usuario.is_active:
                    login(request,usuario)
                    return HttpResponseRedirect('/index')
                else:
                    mensaje = "Usuario y/o password incorrecto"
        form = LoginForm()
        ctx = {'form':form,'mensaje':mensaje}
        return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        #con el request.POST obtenemos los datos que vienen del post
        #y lo almacenamos en la variable form
        form = RegisterForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_one = form.cleaned_data['password_one']
            user = User.objects.create_user(usuario, email, password_one)
            ''' esto nos servira para designar grupos a los usuarios y poder habilitar o 
            deshabilitar caracteristicas de la aplicacion 
            g = Group.objects.get(name='facturacion') 
            g.user_set.add(user)
            '''
            #guardamos el usuario en la base de datos
            user.save()
            return render_to_response('home/thanks_register.html',context_instance=RequestContext(request))
        else:
            ctx = {'form':form}
            return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
    
    ctx = {'form':form}
    return render_to_response('home/register.html',ctx,context_instance=RequestContext(request))
    
    
    
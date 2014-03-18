from django import forms
from django.contrib.auth.models import User
'''
class ContactForm(forms.Form):
    Email = forms.EmailField(widget=forms.TextInput())
    Titulo = forms.CharField(widget=forms.TextInput())
    Texto = forms.CharField(widget=forms.Textarea())
   ''' 
BIEN_SERVICIO = (('Bien', 'Bien'), ('Servicio', 'Servicio'))   
   
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))
    
class RegisterForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario',widget=forms.TextInput())
    email = forms.EmailField(label='Correo',widget=forms.TextInput())
    password_one = forms.CharField(label='Password',widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(label='Verificar password',widget=forms.PasswordInput(render_value=False))
    invoice = forms.BooleanField(label='Autorizar facturacion',initial=False,required=False)
    accounting = forms.BooleanField(label='Autorizar contabilidad',initial=False,required=False)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Nombre de usuario ya existe')
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            e = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email ya registrado')
    
    def clean_password_two(self):
        password_one = self.cleaned_data['password_one']
        password_two = self.cleaned_data['password_two']
        if password_one == password_two:
            pass
        else:
            raise forms.ValidationError('Password no coincide')
        
    def clean_invoice(self):
        invoice = self.cleaned_data['invoice']
        if invoice == None:
            pass
        else:
            return invoice

from socket import fromshare
from django import forms


class bookForm(forms.Form):
    nombre_libro = forms.CharField(max_length=75)
    review_del_Libro = forms.CharField(max_length=500)
    paginas_libro = forms.IntegerField()


class authForm(forms.Form):
    nombre_autor = forms.CharField(max_length=75)
    mail_autor = forms.EmailField()


class userForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=75)
    mail_usuario = forms.EmailField()
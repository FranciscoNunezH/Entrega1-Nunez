from django.shortcuts import render
from .models import Book, Authors, User
from django.http import HttpResponse

from bookapp.forms import bookForm, authForm, userForm

# Create your views here.
def index(request):
    return render(request, "bookapp/index.html")

# Vista Formulario de Alta de Libros.
def libros_formulario(request):
    if request.method=='POST':
        form=bookForm(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            nombre=informacion["nombre_libro"]
            review=informacion["review_del_Libro"]
            paginas=informacion["paginas_libro"]
            libro = Book(book_name=nombre, book_review=review, book_pages=paginas)
            libro.save()
            return render(request, "bookapp/index.html")
    else:
        formulario=bookForm()
        return render(request, "bookapp/libroFormulario.html", {"formulario":formulario})

# Vista Formulario de Alta de Usuarios.
def user(request):
    if request.method=='POST':
        form=userForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre_usuario"]
            mail=info["mail_usuario"]
            usuario = User(user_name=nombre, user_mail=mail)
            usuario.save()
            return render(request, "bookapp/index.html")
    else:
        formulario=userForm()
        return render(request, "bookapp/user.html", {"formulario":formulario})


# Vista Formulario de Alta de Autores.
def author(request):
    if request.method=='POST':
        form=authForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info["nombre_autor"]
            mail=info["mail_autor"]
            autor = Authors(author_name=nombre, author_mail=mail)
            autor.save()
            return render(request, "bookapp/index.html")
    else:
        formulario=authForm()
        return render(request, "bookapp/authors.html", {"formulario":formulario})


def busquedaLibro(request):
    return render(request, "bookapp/busquedaLibro.html")


def buscar(request):
    if request.GET["libro"]:
        libro=request.GET["libro"]
        libros=Book.objects.filter(book_name__icontains=libro)
        return render(request, "bookapp/resultadoBusqueda.html", {"libros":libros})
    else:
        return render(request, "bookapp/busquedaLibro.html", {"mensaje":"Ingresa Un Libro a Buscar o hay Tabla."})

    # return HttpResponse(respuesta)
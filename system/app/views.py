from django.shortcuts import render

from django.views.generic.detail import DetailView
from .models import usuario,apps,Membership
from system.multipleslug import MultiSlugMixin
from django.shortcuts import get_object_or_404


from .forms import LibroModelForm
# Create your views here.

def home(request):
    return render(request, 'index.html')

def info(request):
    return render(request, 'info.html')

def appinfo(request):
    return render(request, 'infoapp.html')

def userpag(request):
    us = usuario.objects.all()
    template = "user.html"
    contexto= {"us":us}
    return render(request, template, contexto)


class usuarioDetailView(MultiSlugMixin, DetailView):
    model = usuario

def detalle(request, object_id=None):
    #Logico de negocio alias hechizo
    user = get_object_or_404(usuario, id=object_id)
    app = get_object_or_404(apps, id=object_id)
    mem = get_object_or_404(Membership, id=object_id)
    m = "productos nuevo"
    template = "pruevas.html"
    contexto= {"user":user,
           "apps": app,
           "mem": mem }
    return render(request, template, contexto)



def agregar_info(request, object_id=None):
    form = LibroModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        print "Alta exitosa!"

    template = "agregar.html"
    context = {
        "titulo":"Crear Producto!",
        "form":form
    }

    return render(request, template, context)


def actualizar(request, object_id=None):
    #Logico de negocio alias hechizo
    libros = get_object_or_404(usuario, id=object_id)
    form = LibroModelForm(request.POST or None, instance=libros)
    if form.is_valid():
        form.save()
        print "Actualizacion exitosa!"
    template = "actualizar.html"
    contexto= {
           "libros": libros,
           "form":form,
           "titulo":"Actualizar Libro"
           }
    return render(request, template, contexto)

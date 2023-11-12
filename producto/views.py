from django.shortcuts import redirect, render
from .models import Producto, Contacto
from .forms import ProductoForm, ContactoForm
from django.contrib import messages

# Create your views here.

def inicio(request):
    return render(request, 'pages/inicio.html')

def listado_productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto/productos.html', { 'productos': productos })

def crear_producto(request):
    formulario = ProductoForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request,"Producto creado con exito.")
        return redirect('productos')        

    return render(request, 'producto/crear.html', {'formulario': formulario})

def editar_producto(request, id):
    producto = Producto.objects.get(id = id)

    formulario = ProductoForm(request.POST or None, instance = producto)
    if formulario.is_valid():
        formulario.save()
        messages.success(request,"Producto actualizado con exito.")
        return redirect('productos') 
    
    return render(request, 'producto/editar.html', {'formulario': formulario})

def eliminar_producto(request, id):
    producto = Producto.objects.get(id = id)
    producto.delete()
    return redirect('productos')

def mensaje(request):
    formularioContacto = ContactoForm(request.POST or None)

    if formularioContacto.is_valid():
        # producto = formulario.save
        formularioContacto.save()
        messages.success(request,"Mensaje enviado con exito.")
        return redirect('inicio')

    return render(request, 'Contacto/contacto.html', {'formularioContacto':formularioContacto})

def recibidos(request):
    contactos = Contacto.objects.all()
    return render(request, 'contacto/mensajes.html', {'contactos':contactos})

def eliminarMensaje(request,id):
    contacto = Contacto.objects.get(id = id)
    contacto.delete()
    messages.success(request,"Mensaje eliminado con exito.")
    return redirect('mensajes_recibidos')

def acercaDe(request):
    return render(request,'pages/acercaDe.html')

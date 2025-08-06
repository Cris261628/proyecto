from django.shortcuts import render
from .models import Alumnos
from .forms import ComentarioContactoForm
from .forms import ComentarioContacto
from django.shortcuts import get_object_or_404
import datetime
from .models import ComentarioContacto
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages


def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibidos son correctos
         form.save() #inserta
         return render(request,'registros/contacto.html')

    form = ComentarioContactoForm()
    #Si algo sale mal se reenvian al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})

def contacto(request):

        return render(request,"registros/contacto.html")

def comentarios(request):
        coments=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html",{'comentarios':coments})

def eliminarComentarioContacto(request, id,
        confirmacion='registros/confirmarEliminacion.html'):
        comentario = get_object_or_404(ComentarioContacto, id=id)
        if request.method=='POST':
                comentario.delete()
                comentarios=ComentarioContacto.objects.all()
                return render(request,"registros/comentarios.html",
                                              {'comentarios':comentarios})
        return render(request, confirmacion, {'object':comentario})

def consultar(request):
      alumnos=Alumnos.objects.filter(carrera="ti")
      return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultarr(request):
      alumnos=Alumnos.objects.filter(carrera="ti").filter(turno="mautino")
      return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultarrr(request):
      alumnos=Alumnos.objects.all().only("matricula","nombre","carrera","turno","imagen")
      return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultare(request):
      alumnos=Alumnos.objects.filter(turno__contains="vespertino")
      return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultaree(request):
      alumnos=Alumnos.objects.filter(nombre__in=["juan","ana"])
      return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar6(request):
      fechainicio = datetime.date(2025,6,1)
      fechafin = datetime.date(2025,7,13)
      alumnos=Alumnos.objects.filter(created__range=(fechainicio,fechafin))
      return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar7(request):
      alumnos=Alumnos.objects.filter(comentario__coment__contains='soy juan')
      return render(request,"registros/consultas.html",{'alumnos':alumnos})
#/////////////////

def comentarios_fecha(request):
    inicio = datetime.date(2025, 7, 8)
    fin = datetime.date(2025, 7, 9)
    comentarios = ComentarioContacto.objects.filter(created__range=(inicio, fin))
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def buscar_expresion(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains="soporte")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def comentarios_usuario(request):
    comentarios = ComentarioContacto.objects.filter(usuario="juan123")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})

def solo_mensajes():
    mensajes = ComentarioContacto.objects.values_list("mensaje", flat=True)
    return list(mensajes)

def comentarios_sin_error(request):
    comentarios = ComentarioContacto.objects.exclude(mensaje__icontains="error")
    return render(request, "registros/comentarios.html", {'comentarios': comentarios})


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})
    
def consultasSQL(request):

    alumnos = Alumnos.objects.raw('SELECT matricula, nombre, carrera, turno, imagen FROM registros_alumnos WHERE carrera="TI" ORDER BY turno DESC')
    return(
    render(request,"registros/consultas.html",
    {'alumnos':alumnos}))


def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"registros/seguridad.html",
    {'nombre':nombre})

#def seguridad(request):
 #return render(request,"registros/seguridad.html")

#Indicamos el lugar donde se renderizará el resultado de esta vista
# Create your views here.

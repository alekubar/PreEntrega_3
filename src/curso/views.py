from django.shortcuts import redirect, render
from .models import Curso, Comision, Alumno
from .forms import CursoForm
# Create your views here.
def index(request):
    return render(request, "curso/index.html")

def about(request):
    return render(request,"curso/about.html" )

def curso_list(request):
    query = Curso.objects.all()
    context = {"object_list": query}
    return render(request, "curso/curso_list.html", context)

def curso_create(request):
    if request.method == "GET":
        form = CursoForm()
        if request.method == "POST":
            form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso:")

def comision_list(request):
    query = Comision.objects.all()
    context = {"object_list": query}
    return render(request, "curso/comision_list.html", context)

def alumno_list(request):
    query = Alumno.objects.all()
    context = {"object_list": query}
    return render(request, "curso/alumno_list.html", context)

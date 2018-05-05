from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from appcrudbasico.models import Estudiante
from appcrudbasico.forms import estudianteForm
from django.contrib import messages

# Create your views here.
def estudiante(request):
    return render_to_response("estudiante.html", {"estudiantes": Estudiante.objects.all(), "messages": messages.get_messages(request)})


def add_estudiante(request):
    form = estudianteForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El estudiante ha sido guardado ha sido guardado!")
            return HttpResponseRedirect("/estudiante/list/")

    return render(request, 'forms_estudiante.html', {'form': form})


def update_estudiante(request, id):
    instance = get_object_or_404(Estudiante, id=id)
    form = estudianteForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "El estudiante ha sido actualizado!")
            return HttpResponseRedirect("/estudiante/list/")

    return render(request, 'forms_estudiante.html', {'form': form})


def delete_estudiante(request, id):
    instance = get_object_or_404(Estudiante, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "el estudiante ha sido borrado" % id)
    return HttpResponseRedirect("/estudiante/list/")
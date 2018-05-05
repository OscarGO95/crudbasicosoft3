from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from appcrudbasico.models import Materia
from appcrudbasico.forms import MateriaForm
from django.contrib import messages

# Create your views here.
def materias(request):
    return render_to_response("materias.html", {"materias": Materia.objects.all(), "messages": messages.get_messages(request)})


def add_materia(request):
    form = MateriaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The materia has been saved!")
            return HttpResponseRedirect("/materias/list/")

    return render(request, 'forms_materia.html', {'form': form})


def update_materia(request, id):
    instance = get_object_or_404(Materia, id=id)
    form = MateriaForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "The materia has been updated!")
            return HttpResponseRedirect("/materias/list/")

    return render(request, 'forms_materia.html', {'form': form})


def delete_materia(request, id):
    instance = get_object_or_404(Materia, id=id)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, "The materia with id %s has been deleted!" % id)
    return HttpResponseRedirect("/materias/list/")
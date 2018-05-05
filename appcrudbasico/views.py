from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from appcrudbasico.forms import MaestrosForm
from appcrudbasico.models import Maestros
from django.contrib import messages

class clsMaestros:

    def index(request):
        return render(request, 'index.html', {'dataServ': Maestros.objects.all()})

    def create(request):
        form = MaestrosForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Maestro Guardado")
                return HttpResponseRedirect("/")

        return render(request, 'create.html', {'form': form})

    def update(request, id):
        instance = get_object_or_404(Maestros, cedula=id)
        form = MaestrosForm(request.POST or None, instance=instance)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "El profesor ha sido actualizado!")
                return HttpResponseRedirect("/")

        return render(request, 'create.html', {'form': form})

    def delete(request, id):
        instance = get_object_or_404(Maestros, cedula=id)
        instance.delete()
        messages.add_message(request, messages.SUCCESS, "El profesor con cedula %s ha sido eliminado!" % id)
        return HttpResponseRedirect("/")
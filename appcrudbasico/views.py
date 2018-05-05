from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages

from appcrudbasico.forms import ActividadesForm
from appcrudbasico.models import Actividades



class crud:
    def index(request):
        data=Actividades.objects.all()
        return render(request, 'index.html', {'actividades':data})

    def add_actividad(request):
        form = ActividadesForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "The Activity has been saved!")
                return HttpResponseRedirect("/")

        return render(request, 'addActividad.html', {'form': form})

    def update_actividad(request, id):
        instance = get_object_or_404(Actividades, codigo=id)
        form = ActividadesForm(request.POST or None, instance=instance)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "The materia has been updated!")
                return HttpResponseRedirect("/")

        return render(request, 'addActividad.html', {'form': form})

    def delete_actividad(request, id):
        instance = get_object_or_404(Actividades, codigo=id)
        instance.delete()
        messages.add_message(request, messages.SUCCESS, "The materia with id %s has been deleted!" % id)
        return HttpResponseRedirect("/")









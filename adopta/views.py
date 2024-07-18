from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.
def index(request):

    return render(request,'adopta/index.html')


# Create your views here.
def inscribe(request):

    return render(request,'adopta/inscribe.html')

# Create your views here.
def sobre_nosotros(request):

    return render(request,'adopta/Sobre Nosotros.html')


def adopta(request):

    return render(request,'adopta/adopta.html')

def registro(request):

    return render(request,'adopta/registro.html')



class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario_list.html'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuario_detail.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('usuario_list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('usuario_list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario_list')


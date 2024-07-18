from django.shortcuts import render

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


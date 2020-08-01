from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Comments
from django.contrib import messages
# Create your views here.

def main(request):
    if request.method == 'POST':
        email = request.POST['email']
        value = request.POST['precios']
        comment = request.POST['feedback']
        #Creamos el regisrto en la base de datos

        registro = Comments.objects.create()
        registro.email = email
        registro.value = value
        registro.feedback = comment
        registro.save()

        if registro:
            url = reverse('main', messages.success(request, 'Muchas gracias por tu tiempo. Hemos registrado tu respuesta'))
            return redirect(url)

    return render(
        request = request,
        template_name='core/home.html'
    )

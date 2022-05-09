from django.shortcuts import render
from urllib import request
from .forms import Bajaderka
from .models import Bajadery

# Create your views here.


def home(response):
    return render(response, 'main/home.html', {})


def dodaj(response):

    if response.user.is_authenticated != True:
        return render(response, 'register/unauth.html', {})

    formularz = Bajaderka()
    if response.method == "POST":
        print(response.POST)
        nazwa_lokalu = response.POST['nazwa_lokalu']
        ocena = response.POST['ocena']
        adres = response.POST['adres']

        nowa_bajadera = Bajadery.objects.create(nazwa=nazwa_lokalu, ocena=ocena, adres=adres)
        nowa_bajadera.save()
        return render(response, 'main/dodaj.html', {'form': formularz, 'czy_wyslane': True})


    return render(response, 'main/dodaj.html', {'form': formularz, 'czy_wyslane': False})


def ranking(response):

    bajaderki = Bajadery.objects.all()

    data = {
        'bajaderki': bajaderki
    }

    return render(response, 'main/ranking.html', data)



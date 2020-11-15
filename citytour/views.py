from django.http import HttpResponse
from django.shortcuts import render, redirect
import re
import datetime
import requests
import json
from aboutcity.models import aboutcity
from hotels.models import hotels
from places.models import places
from streetfood.models import streetfood


def index(request):
    if request.method == "POST":
        city = request.POST.get('city', '')
        today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b5daf570427aa784d3cd32a6d5a3e514'
        r = requests.get(url.format(city)).json()
        print(r)
        print(city)
        tempf = int(r["main"]["temp"])
        tempc = (tempf-32)*(100/180)
        tempc = "{:.2f}".format(tempc)
        print(tempc)
        city_weather = {'today': today,
                        'city': city,
                        'temperature': tempc,
                        'description': r["weather"][0]["description"],
                        }
        print(city_weather)
        updates = [{'city': city}, {'today': today}, {'temperature': tempc}, {
            'description': r["weather"][0]["description"]}]
        response = json.dumps(updates, default=str)
        print(response)
        return HttpResponse(response)
    return render(request, 'index.html')


def knowmore(request):
    if request.method == "GET":
        city_name = request.GET.get('city_name', '')
        print(city_name)
        today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=b5daf570427aa784d3cd32a6d5a3e514'
        r = requests.get(url.format(city_name)).json()
        tempf = int(r["main"]["temp"])
        tempc = (tempf-32)*(100/180)
        tempc = "{:.2f}".format(tempc)
        print(tempc)
        city_weather = {'today': today,
                        'city': city_name,
                        'temperature': tempc,
                        'description': r["weather"][0]["description"],
                        }
        print(city_weather)
        inf = aboutcity.objects.filter(cityname=city_name)
        params = {'info': inf,'city': city_name, 'today': today, 'temperature': tempc,
            'description': r["weather"][0]["description"]}
        print(len(inf))
        print(params)
        return render(request, 'aboutcity.html', params)

def abouthotels(request):
    if request.method == "POST":
        city_name = request.POST.get('city_name', '')
        hotelinfo = hotels.objects.filter(cityname=city_name)
        length=len(hotelinfo)
        print(length)
        params = {'info': hotelinfo}
        return render(request, 'abouthotels.html', params)
    return render(request, 'abouthotels.html') 

def aboutplaces(request):
    if request.method == "POST":
        city_name = request.POST.get('city_name', '')
        placesinfo = places.objects.filter(cityname=city_name)
        params = {'info': placesinfo}
        return render(request, 'aboutplaces.html', params)
    return render(request, 'aboutplaces.html')    

def aboutstreetfood(request):
    if request.method == "POST":
        city_name = request.POST.get('city_name', '')
        foodinfo = places.objects.filter(cityname=city_name)
        params = {'info': foodinfo}
        return render(request, 'aboutstreetfood.html', params)
    return render(request, 'aboutstreetfood.html')    

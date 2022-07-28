from django.shortcuts import render
from .models import City
from .serializers import CitySerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
import requests

def fetchWeatherReport():
	api="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&exclude=[minutely,hourly,daily,alerts]&appid=85a469c8fb8a4afe2c13842019bb5d74"
	cities = City.objects.all()
	for city in cities:
		data =requests.get(api.format(city.name)).json()
		city.weather = data['main']
		city.save()

#pagination
class WeatherReportPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

class WeatherReport(ListAPIView):
	queryset = City.objects.all()
	serializer_class = CitySerializer
	permission_classes = [permissions.IsAuthenticated]
	pagination_class = WeatherReportPagination

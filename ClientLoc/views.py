from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def get_country(request):
    ip, x_forwarded_for = get_client_ip(request)
    g = GeoIP2()
    country = g.country(ip)
    return Response({"country": country['country_code'], "client_ip": ip, "ips": x_forwarded_for})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip, x_forwarded_for
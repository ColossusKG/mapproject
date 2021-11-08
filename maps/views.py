from django.shortcuts import render,  redirect ,  get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Q
from .models import *
import pandas as pd
import csv
import folium
import geocoder
from folium import plugins


# Create your views here.
# db 저장


#가맹점 목록 출력
def index(request):
    g = geocoder.ip('me')
    map = folium.Map(location=(37.6,126.7), zoom_start=11)

    city = request.GET.get('city','')
    page = request.GET.get('page','1') # 페이지
    kw = request.GET.get('kw','')  # 검색
    # so = request.GET.get('so','') # 정렬

    shop_list = gg03.objects.all()

    if kw:
        shop_list = shop_list.filter(
            Q(name__icontains = kw)
        ).distinct()
        for shop in shop_list:
            lat = shop.lat
            lng = shop.lng
            name = shop.name
            latlng = 'LAT ' + str(lat) + '\nLNG ' + str(lng)
            folium.Marker(location = [lat, lng], popup=latlng, tooltip=name).add_to(map)

    map = map._repr_html_()

    # 페이징 처리
    paginator = Paginator(shop_list, 10)  # 페이지당 10개 보여주기
    page_obj = paginator.get_page(page)  # 페이지 객체 생성
    content = {'shop_list': page_obj, 'page': page, 'kw': kw, 'map': map}
    return render(request,'maps/shop_list.html', content)

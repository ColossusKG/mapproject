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
def index(request):
    return render(request,'maps/main.html')

#가맹점 목록 출력
def shop_list(request):
    city = request.GET.get('city', '')
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색

    g = geocoder.ip('me')
    map = folium.Map(location=(g.latlng), zoom_start=20)
    shop_list = ''

    if city == '가평군':
        shop_list = gg01.objects.order_by()
    if city == '고양시':
        shop_list = gg02.objects.order_by()
    if city == '과천시':
        shop_list = gg03.objects.order_by()
    if city == '광명시':
        shop_list = gg04.objects.order_by()
    if city == '광주시':
        shop_list = gg05.objects.order_by()
    if city == '구리시':
        shop_list = gg06.objects.order_by()
    if city == '군포시':
        shop_list = gg07.objects.order_by()
    if city == '남양주시':
        shop_list = gg08.objects.order_by()
    if city == '동두천시':
        shop_list = gg09.objects.order_by()
    if city == '부천시':
        shop_list = gg10.objects.order_by()
    if city == '수원시':
        shop_list = gg11.objects.order_by()
    if city == '안산시':
        shop_list = gg12.objects.order_by()
    if city == '안성시':
        shop_list = gg13.objects.order_by()
    if city == '안양시':
        shop_list = gg14.objects.order_by()
    if city == '양주시':
        shop_list = gg15.objects.order_by()
    if city == '양평군':
        shop_list = gg16.objects.order_by()
    if city == '여주시':
        shop_list = gg17.objects.order_by()
    if city == '연천군':
        shop_list = gg18.objects.order_by()
    if city == '오산시':
        shop_list = gg19.objects.order_by()
    if city == '용인시':
        shop_list = gg20.objects.order_by()
    if city == '의왕시':
        shop_list = gg21.objects.order_by()
    if city == '의정부시':
        shop_list = gg22.objects.order_by()
    if city == '이천시':
        shop_list = gg23.objects.order_by()
    if city == '파주시':
        shop_list = gg24.objects.order_by()
    if city == '평택시':
        shop_list = gg25.objects.order_by()
    if city == '포천시':
        shop_list = gg26.objects.order_by()
    if city == '하남시':
        shop_list = gg27.objects.order_by()
    if city == '화성시':
        shop_list = gg28.objects.order_by()
    # if city != '':
    #     findurl = "https://maps.googleapis.com/maps/api/geocode/json?address="
    #     api_key = "AIzaSyA3mjXMzjFeFCBDwYGK5Ja-xtu7EPh-iqo"
    #     apiquery = "&key=" + api_key
    #     findmapurl = findurl + city + apiquery
    #     mapdata = request.get(findmapurl).json()
    #     mlat = mapdata['results'][0]['geometry']['location']['lat']
    #     mlng = mapdata['results'][0]['geometry']['location']['lng']
    #     map = folium.Map(location=(mlat, mlng), zoom_start=12)


    if kw:
        shop_list = shop_list.filter(
            Q(name__icontains = kw)
        )
        for shop in shop_list:
            lat = shop.lat
            lng = shop.lng
            name = shop.name
            latlng = 'LAT ' + str(lat) + '\nLNG ' + str(lng)
            folium.Marker(location = [lat, lng], popup=latlng, tooltip=name).add_to(map)


    map = map._repr_html_()

    # 페이징 처리
    paginator = Paginator(shop_list, 10) # 페이지당 10개 보여주기
    page_obj = paginator.get_page(page) # 페이지 객체 생성
    content = {'shop_list' : page_obj, 'page':page, 'kw':kw, 'map':map}
    return render(request,'maps/shop_list.html', content)

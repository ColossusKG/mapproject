import json
import urllib
import requests
import folium
import lxml
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


# Create your views here.
# db 저장
def index(request):
    return render(request,'maps/main.html')


# 가맹점 목록 출력
def shop_list(request):
    city = request.GET.get('city', '')
    area1 = request.GET.get('area1', '')
    area2 = request.GET.get('area2', '')  # 행정구역별 검색
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색
    marker = request.GET.get('marker', '')  # 지도 표시
    save = request.GET.get('save', '')  # 저장

    shop_list = data.objects.order_by().filter(
        Q(city__icontains=city)
    )
    map = folium.Map(location=(search_map(city)), zoom_start=12)

    # 행정 구역 리스트 출력
    area1_list = address.objects.order_by().filter(
        Q(city__icontains=city)
    )

    if area1:
        area2_list = address.objects.order_by().filter(
            Q(area1__icontains=area1)
        )

    else:
        area2_list = address.objects.order_by().filter(
            Q(city__icontains=city)
        )

    if area2:
        shop_list = data.objects.order_by().filter(
            Q(addr2__icontains=area2)
        )

    # 가맹점 지도 표시 코드
    if marker:
        map = map_marker(marker)

    # 가맹점 검색 코드
    if kw:
        shop_list = shop_list.filter(
            Q(name__icontains=kw)
        )
        for shop in shop_list:
            lat1 = shop.lat
            lng1 = shop.lng
            map = folium.Map(location=[lat1, lng1], zoom_start=17)
            break
        for shop in shop_list:
            lat = shop.lat
            lng = shop.lng
            name = shop.name
            latlng = 'LAT ' + str(lat) + '\nLNG ' + str(lng)
            folium.Marker(location=[lat, lng], popup=latlng, tooltip=name).add_to(map)
        # 검색 후 가맹점 지도 표시
        if marker:
            map = map_marker(marker)

    if save:  # 가맹점 저장 코드
        shop = get_object_or_404(data, pk=save)
        shop.mark.add(request.user)

    map = map._repr_html_()

    # 페이징 처리
    paginator = Paginator(shop_list, 10)  # 페이지당 10개 보여주기
    page_obj = paginator.get_page(page)  # 페이지 객체 생성
    content = {'shop_list': page_obj, 'page': page, 'kw': kw, 'map': map, 'city': city, 'area1_list': area1_list,
               'area2_list': area2_list}
    return render(request, 'maps/shop_list.html', content)


# 초기 지도 표시 코드
def search_map(search_text):
    client_id = 'aar7gausw4'  # 클라이언트 ID값
    client_secret = '8xYb96nBebbCnvZJNUFFdrW8DC1Mq0QODOc120Bt'  # 클라이언트 Secret값
    encText = urllib.parse.quote(search_text)
    url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query=' + encText
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        data = response_body.decode('utf-8')
        data = json.loads(data)
        lat_data = data['addresses'][0]['y']
        lng_data = data['addresses'][0]['x']
        return lat_data, lng_data

    else:
        print("Error Code:" + rescode)


# 가맹점 지도 표시 코드
def map_marker(marker):
    shop = get_object_or_404(data, pk=marker)
    lat = shop.lat
    lng = shop.lng
    name = shop.name
    latlng = 'LAT ' + str(lat) + '\nLNG ' + str(lng)
    map = folium.Map(location=[lat, lng], zoom_start=17)
    folium.Marker(location=[lat, lng], popup=latlng, tooltip=name).add_to(map)

    return map



#가맹점 목록 출력
# def shop_list(request):
#     city = request.GET.get('city', '')
#     area = request.GET.get('area','')# 행정구역별 검색
#     page = request.GET.get('page', '1')  # 페이지
#     kw = request.GET.get('kw', '')  # 검색
#     marker = request.GET.get('marker', '') # 지도 표시
#     save = request.GET.get('save','') #저장
#
#     shop_list = data.objects.order_by().filter(
#         Q(city__icontains=city)
#     )
#
#     area_list = address.objects.order_by().filter(
#             Q(city__icontains=city)
#         )
#
#
#     def search_map(search_text):
#         client_id = 'aar7gausw4'  # 클라이언트 ID값
#         client_secret = '8xYb96nBebbCnvZJNUFFdrW8DC1Mq0QODOc120Bt'  # 클라이언트 Secret값
#         encText = urllib.parse.quote(search_text)
#         url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query=' + encText
#         request = urllib.request.Request(url)
#         request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
#         request.add_header('X-NCP-APIGW-API-KEY', client_secret)
#         response = urllib.request.urlopen(request)
#         rescode = response.getcode()
#         if (rescode == 200):
#             response_body = response.read()
#             data = response_body.decode('utf-8')
#             data = json.loads(data)
#             lat_data = data['addresses'][0]['y']
#             lng_data = data['addresses'][0]['x']
#             return lat_data, lng_data
#
#         else:
#             print("Error Code:" + rescode)
#
#     map = folium.Map(location=(search_map(city)), zoom_start=12)
#
#     if area: # 행정구역별 표시 코드
#         shop_list = data.objects.order_by().filter(
#             Q(addr2__icontains=area)
#         )
#         map = folium.Map(location=(search_map(area)), zoom_start=12)
#
#
#
#     if marker: # 가맹점 지도 표시 코드
#         shop = get_object_or_404(data, pk=marker)
#         lat = shop.lat
#         lng = shop.lng
#         name = shop.name
#         latlng = 'LAT ' + str(lat) + '\nLNG ' + str(lng)
#         map = folium.Map(location=[lat, lng], zoom_start=17)
#         folium.Marker(location=[lat, lng], popup=latlng, tooltip=name).add_to(map)
#
#
#     if kw: # 가맹점 검색 코드
#         shop_list = shop_list.filter(
#                 Q(name__icontains = kw)
#             )
#         for shop in shop_list:
#             lat1 = shop.lat
#             lng1 = shop.lng
#             map = folium.Map(location=[lat1, lng1], zoom_start=17)
#             break
#         for shop in shop_list:
#             lat = shop.lat
#             lng = shop.lng
#             name = shop.name
#             latlng = 'LAT ' + str(lat) + '\nLNG ' + str(lng)
#             folium.Marker(location = [lat, lng], popup=latlng, tooltip=name).add_to(map)
#
#         if marker:
#             shop = get_object_or_404(data, pk=marker)
#             lat = shop.lat
#             lng = shop.lng
#             name = shop.name
#             latlng = 'LAT ' + str(lat) + '\nLNG ' + str(lng)
#             map = folium.Map(location=[lat, lng], zoom_start=17)
#             folium.Marker(location=[lat, lng], popup=latlng, tooltip=name).add_to(map)
#
#     if save: # 가맹점 저장 코드
#         shop = get_object_or_404(data, pk=save)
#         shop.mark.add(request.user)
#
#
#
#     map = map._repr_html_()
#
#     # 페이징 처리
#     paginator = Paginator(shop_list, 10) # 페이지당 10개 보여주기
#     page_obj = paginator.get_page(page) # 페이지 객체 생성
#     content = {'shop_list': page_obj, 'page':page, 'kw':kw, 'map':map, 'city':city, 'area_list':area_list}
#     return render(request,'maps/shop_list.html', content)


#가맹점 목록 출력
def shop_list(request):
    city = request.GET.get('city', '')
    area1 = request.GET.get('area1', '')
    area2 = request.GET.get('area2','') # 행정구역별 검색
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색
    marker = request.GET.get('marker', '') # 지도 표시
    save = request.GET.get('save','') #저장

    shop_list = data.objects.order_by().filter(
        Q(city__icontains=city)
    )
    map = folium.Map(location=(search_map(city)), zoom_start=12)


    # 행정 구역 리스트 출력
    area1_list = address.objects.order_by().filter(
        Q(city__icontains=city)
    )

    if area1:
        area2_list = address.objects.order_by().filter(
            Q(area1__icontains=area1)
        )

    else:
        area2_list = address.objects.order_by().filter(
            Q(city__icontains=city)
        )
        
    if area2:
        shop_list = data.objects.order_by().filter(
            Q(addr2__icontains=area2)
        )


    # 가맹점 지도 표시 코드
    if marker:
        map=map_marker(marker)

    # 가맹점 검색 코드
    if kw:
        shop_list = shop_list.filter(
            Q(name__icontains=kw)
        )
        for shop in shop_list:
            lat1 = shop.lat
            lng1 = shop.lng
            map = folium.Map(location=[lat1, lng1], zoom_start=17)
            break
        for shop in shop_list:
            lat = shop.lat
            lng = shop.lng
            name = shop.name
            latlng = 'LAT ' + str(lat) + '\nLNG ' + str(lng)
            folium.Marker(location=[lat, lng], popup=latlng, tooltip=name).add_to(map)
        # 검색 후 가맹점 지도 표시
        if marker:
            map = map_marker(marker)

    if save: # 가맹점 저장 코드
        shop = get_object_or_404(data, pk=save)
        shop.mark.add(request.user)



    map = map._repr_html_()

    # 페이징 처리
    paginator = Paginator(shop_list, 10) # 페이지당 10개 보여주기
    page_obj = paginator.get_page(page) # 페이지 객체 생성
    content = {'shop_list': page_obj, 'page':page, 'kw':kw, 'map':map, 'city':city, 'area1_list':area1_list, 'area2_list':area2_list}
    return render(request,'maps/shop_list.html', content)





# 초기 지도 표시 코드
def search_map(search_text):
    client_id = 'aar7gausw4'  # 클라이언트 ID값
    client_secret = '8xYb96nBebbCnvZJNUFFdrW8DC1Mq0QODOc120Bt'  # 클라이언트 Secret값
    encText = urllib.parse.quote(search_text)
    url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query=' + encText
    request = urllib.request.Request(url)
    request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
    request.add_header('X-NCP-APIGW-API-KEY', client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        data = response_body.decode('utf-8')
        data = json.loads(data)
        lat_data = data['addresses'][0]['y']
        lng_data = data['addresses'][0]['x']
        return lat_data, lng_data

    else:
        print("Error Code:" + rescode)




# 가맹점 지도 표시 코드
def map_marker(marker):
    shop = get_object_or_404(data, pk=marker)
    lat = shop.lat
    lng = shop.lng
    name = shop.name
    latlng = 'LAT ' + str(lat) + '\nLNG ' + str(lng)
    map = folium.Map(location=[lat, lng], zoom_start=17)
    folium.Marker(location=[lat, lng], popup=latlng, tooltip=name).add_to(map)

    return map



def naver(request, id):
    shop = get_object_or_404(data, pk=id)
    findurl = 'https://search.naver.com/search.naver?query='
    findurl = findurl + shop.addr2
    findurl = requests.get(findurl).text
    bs = BeautifulSoup(findurl, 'lxml')
    bsfind = bs.find_all('a', {'class': '_3g_0T'})
    a = 'https://map.naver.com/v5/search/' + shop.name
    for bs in bsfind:
        if bs.get_text() == shop.name:
            a = bs['href']

    return redirect(a)
    # return render(request,'maps/shop_list.html', {'next':next})

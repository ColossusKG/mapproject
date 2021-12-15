import json
import urllib
import requests
import folium
import lxml
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from django.db.models import Q,Count
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import *


# Create your views here.
# db 저장
def index(request):
    return render(request,'maps/main.html')

#가맹점 목록 출력
def shop_list(request):
    city = request.GET.get('city','경기도') # 시/군
    area1 = request.GET.get('area1','') # 구
    area2 = request.GET.get('area2','') # 읍/면/동
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색
    marker = request.GET.get('marker', '') # 지도 표시
    save = request.GET.get('save','') #저장
    so = request.GET.get('so','')

    if city == "김포/성남/시흥":
        map = folium.Map(location=(search_map('김포시')), zoom_start=12)
        map = map._repr_html_()
        content = {'city': city, 'map': map}
    else:
        shop_list = data.objects.order_by('name').filter(
            Q(city__icontains=city)
        )
        map = folium.Map(location=(search_map(city)), zoom_start=12)


        # 행정 구역 리스트 출력
        area1_list = district.objects.order_by().filter(
            Q(city__icontains=city)
        )
         # 추천순으로 배열
        if so == '추천순':
            shop_list = data.objects.order_by('-mark').filter(
                Q(city__icontains=city)
            )

            if not area1:
                area1_list = district.objects.order_by().filter(
                    Q(city__icontains=city)
                )
            if area1 and not area2:
                area1_list = district.objects.order_by().filter(
                    Q(city__icontains=city) and Q(addr1__icontains=area1)
                )
                shop_list = data.objects.order_by('-mark').filter(
                    Q(city__icontains=city) and Q(addr2__icontains=area1)
                )
                map = folium.Map(location=(search_map(city + ' ' + area1)), zoom_start=16)
            elif area1 and area2:
                area1_list = district.objects.order_by().filter(
                    Q(city__icontains=city) and Q(addr1__icontains=area1)
                )
                shop_list = data.objects.order_by('-mark').filter(
                    Q(city__icontains=city) and Q(addr2__icontains=area1 + ' ' + area2)
                )
                if city != area2:
                    map = folium.Map(location=(search_map(city + ' ' + area2)), zoom_start=16)

            elif not area1 and area2:
                area1_list = district.objects.order_by().filter(
                    Q(city__icontains=city)
                )
                shop_list = data.objects.order_by('-mark').filter(
                    Q(city__icontains=city) and Q(addr2__icontains=area2)
                )
                if city != area2:
                    map = folium.Map(location=(search_map(city + ' ' + area2)), zoom_start=16)

        # 이름순으로 배열
        else:
            if not area1:
                area1_list = district.objects.order_by().filter(
                    Q(city__icontains=city)
                )
            if area1 and not area2:
                area1_list = district.objects.order_by().filter(
                    Q(city__icontains=city) and Q(addr1__icontains=area1)
                )
                shop_list = data.objects.order_by('name').filter(
                    Q(city__icontains=city) and Q(addr2__icontains=area1)
                )
                map = folium.Map(location=(search_map(city + ' ' + area1)), zoom_start=16)
            elif area1 and area2:
                area1_list = district.objects.order_by().filter(
                    Q(city__icontains=city) and Q(addr1__icontains=area1)
                )
                shop_list = data.objects.order_by('name').filter(
                    Q(city__icontains=city) and Q(addr2__icontains=area1 + ' ' + area2)
                )
                if city != area2:
                    map = folium.Map(location=(search_map(city + ' ' + area2)), zoom_start=16)
            elif not area1 and area2:
                area1_list = district.objects.order_by().filter(
                    Q(city__icontains=city)
                )
                shop_list = data.objects.order_by('-mark').filter(
                    Q(city__icontains=city) and Q(addr2__icontains=area2)
                )
                if city != area2:
                    map = folium.Map(location=(search_map(city + ' ' + area2)), zoom_start=16)



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
                folium.Marker(location=[lat, lng], tooltip=name).add_to(map)


        # 가맹점 지도 표시 코드
        if marker:
            map = map_marker(marker)

        # 가맹점 저장 코드
        if save:
            shop = get_object_or_404(data, pk=save)
            if request.user in shop.mark.all():
                messages.error(request,'(상호명: '+shop.name+') 이미 추천한 가맹점입니다.')
            else:
                shop.mark.add(request.user)
                print('추천 완료')

        map = map._repr_html_()

        # 페이징 처리
        paginator = Paginator(shop_list, 10)  # 페이지당 10개 보여주기
        page_obj = paginator.get_page(page)  # 페이지 객체 생성
        content = {'shop_list': page_obj, 'page': page, 'kw': kw, 'map': map, 'city': city, 'area1_list': area1_list,
                'area1':area1, 'area2':area2, 'so':so, 'marker':marker}

    return render(request, 'maps/shop_list2.html', content)





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
    folium.Marker(location=[lat, lng], tooltip=name).add_to(map)

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
    # return render(request,'map
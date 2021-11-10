# for i in range(1,28):
#     a = 'admin.site.register(gg'+str(i)+')'
#     print(a)
import requests

city = '고양시'
findurl = "https://maps.googleapis.com/maps/api/geocode/json?address="
api_key = "AIzaSyA3mjXMzjFeFCBDwYGK5Ja-xtu7EPh-iqo"
apiquery = "&key=" + api_key
findmapurl = findurl + city + apiquery
mapdata = requests.get(findmapurl).json()
mlat = mapdata['results'][0]['geometry']['location']['lat']
mlng = mapdata['results'][0]['geometry']['location']['lng']

print(mlat,mlng)
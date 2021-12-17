# manage.py 경로에 db_uploader.py
import os
import fnmatch
import django
import csv
import sys
import glob
#from maps import models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from maps.models import *  # django.setup() 이후에 임포트해야 오류가 나지 않음
sdir = 'C:/Users/BIT/OneDrive/pyProject/csv/'
for fname in os.listdir('C:/Users/BIT/OneDrive/pyProject/csv/'):
    if fnmatch.fnmatch(fname, '*.csv'):
        gname = 'gg'+fname[0:2]
        gname = getattr(sys.modules[__name__],gname)
        dir = 'C:/Users/BIT/OneDrive/pyProject/csv/' + fname
        print(gname)
        with open(dir,encoding='utf8') as in_file:
            data_reader = csv.reader(in_file)
            next(data_reader, None) # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
            for row in data_reader:
                gname.objects.create(city=row[1], name=row[2], type=row[3], addr1=row[4], addr2=row[5], lat=row[7], lng=row[8])
# CSV_PATH_PRODUCTS='C:/Users/BIT/OneDrive/pyProject/03*'
#
# with open(CSV_PATH_PRODUCTS,encoding='utf8') as in_file:
#         data_reader = csv.reader(in_file)
#         next(data_reader, None) # 출력시 함께 출력되는 맨첫줄을 제외하고 출력하기 위함
#         for row in data_reader:
#             print(row[0][2])
#             gg03.objects.create(city=row[1], name=row[2], type=row[3], addr1=row[4], addr2=row[5], lat=row[7], lng=row[8])
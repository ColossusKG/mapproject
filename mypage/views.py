from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from pybo.models import Question, Answer
from maps.models import *
from board.models import *

# Create your views here.

# 자신의 질문목록출력
@login_required(login_url="common:login")
def index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    so = request.GET.get('so', 'question_list')  # 정렬기준
    user = request.user

    list = Question.objects.order_by('create_date')


    # 정렬
    if so == 'question_list':
        list = Question.objects.order_by('-create_date')



        list = list.filter(
            Q(author__username__icontains=user)
        )

    elif so == 'mark_list':
        mark_list = data.objects.filter(mark=user.id)
        list = mark_list

    elif so == 'comment_list':
        comment_list = ShopComment.objects.order_by('-create_date').filter(
            Q(author__username__icontains=user)
        )
        list = comment_list


    # 페이징처리
    paginator = Paginator(list, 9)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'list': page_obj, 'page': page, 'so': so}
    return render(request, 'mypage/mypage.html', context)




# 저장 목록 삭제
def save_delete(request, data_id):
    page = request.GET.get('page', '')

    shop = get_object_or_404(data, pk=data_id)
    user = request.user
    shop.mark.remove(user)

    list = data.objects.filter(mark=user.id)

    paginator = Paginator(list, 9)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request, 'mypage/mypage.html',{'so': 'mark_list','list':page_obj})
from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q, Count
from pybo.models import Question, Answer
from maps.models import *

# Create your views here.

# 자신의 질문목록출력
def index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준
    user = request.user

    list = Question.objects.order_by('create_date')
    list2 = gg01.objects.filter(mark=user.id)

    # 정렬
    if so == 'question_list':
        list = Question.objects.order_by('create_date')



        list = list.filter(
            Q(author__username__icontains=request.user)
        )

        # 조회
        if kw:
            list = list.filter(
                Q(subject__icontains=kw) |  # 제목검색
                Q(content__icontains=kw) |  # 내용검색
                Q(author__username__icontains=kw) |  # 질문 글쓴이검색
                Q(answer__author__username__icontains=kw) |  # 답변 글쓴이검색
                Q(answer__content__icontains=kw)  # 답변 내용검색
            ).distinct()


    elif so == 'mark_list':
        list = list2

    # 페이징처리
    paginator = Paginator(list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'mypage/mypage.html', context)




# 저장 목록 삭제
def save_delete(request, shop_id):
    page = request.GET.get('page', '')

    shop = get_object_or_404(gg01, pk=shop_id)
    user =request.user
    shop.mark.remove(user)

    list = gg01.objects.filter(mark=user.id)

    paginator = Paginator(list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request, 'mypage/mypage.html',{'so': 'mark_list','list':page_obj})
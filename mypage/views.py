from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from pybo.models import Question, Answer

# Create your views here.

# 자신의 질문목록출력
def index(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    list = Question.objects.order_by('create_date')

    # 정렬
    if so == 'question':
        list = Question.objects.order_by('create_date')
    #elif so == 'answer':
    #   list = Answer.objects.order_by('create_date')


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

    # 페이징처리
    paginator = Paginator(list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'mypage/mypage.html', context)
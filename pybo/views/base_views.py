from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Question
from datetime import date, datetime, timedelta


def index(request):
    """
    pybo 목록 출력
    """
    # 입력 파라미터
    # global question_list # 임시
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'popular':
        question_list = Question.objects.annotate(num_answer=Count('hit')).order_by('-hit', '-create_date')
    elif so == 'recent':
        question_list = Question.objects.order_by('-create_date')
    elif so == 'old':
        question_list = Question.objects.order_by('create_date')

    # 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)  # 제목검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 내용 출력
    """
    login_session = request.session.get('login_session', '')
    context = { 'login_session': login_session}

    question = get_object_or_404(Question, pk=question_id)
    context['question'] = question

    response = render(request, 'pybo/question_detail.html', context)

    expire_date, now = datetime.now(), datetime.now()
    expire_date += timedelta(days=1)
    expire_date = expire_date.replace(hour=0, minute=0, second=0, microsecond=0)
    expire_date -= now
    max_age = expire_date.total_seconds()

    cookie_value = request.COOKIES.get('hitboard', '_')

    if f'_{question_id}_' not in cookie_value:
        cookie_value += f'{question_id}_'
        response.set_cookie('hitboard', value=cookie_value, max_age=max_age, httponly=True)
        question.hit += 1
        question.save()
    return response

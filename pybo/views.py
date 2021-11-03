from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.template import loader
from .models import Question#, Answer
from .forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    ''' pybo 목록 출력 '''

    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    # context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def map(request):
    return render(request, 'pybo/cctvmapfindroad.html')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    ''' pybo 답변등록 '''
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    #
    # # answer = Answer(question=question, content=request.POST.get('content'), create_date=timezone.now())
    # # answer.save()
    #
    # return redirect('pybo:detail', question_id=question.id)


def question_create(request):
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)



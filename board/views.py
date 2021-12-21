import os
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.core.paginator import Paginator
from uuid import uuid4
from .models import ShopComment
from .forms import *
from maps.models import *

# Create your views here.


def index(request):
    shop_name = request.GET.get('shop_name','')
    address = request.GET.get('address','')
    page = request.GET.get('page','1')

    if shop_name or address:
        shop_list = data.objects.order_by().filter(
            Q(addr2__icontains=address) & Q(name__icontains=shop_name)
        )

        if not shop_list:
            messages.error(request,'일치하는 가맹점이 없습니다.')
            return redirect('board:index')

        paginator = Paginator(shop_list, 10)
        page_obj = paginator.get_page(page)
        content={'shop_list':page_obj,'page':page,'shop_name':shop_name,'address':address}
        return render(request,'board/board.html',content)
    else:
        return render(request,'board/board.html')


def shop_comment(request, id):
    page = request.GET.get('page','1')

    shop = get_object_or_404(data, pk=id)

    comment_list = ShopComment.objects.order_by('-create_date').filter(
         Q(shop__id__icontains=id)
    )

    paginator = Paginator(comment_list,9)
    page_obj = paginator.get_page(page)
    content = {'comment_list':page_obj,'shop_name':shop.name,'shop_id':shop.id,'shop_addr2':shop.addr2,'comment':comment_list}
    return render(request,'board/board_comment.html',content)



@login_required(login_url="common:login")
def shop_comment_create(request, id):
    shop = get_object_or_404(data,pk=id)
    if request.method == "POST":
        form = ShopCommentForm(request.POST)
        if form.is_valid():
            shop_comment = form.save(commit=False)
            try:
                shop_comment.image = request.FILES['filename']
            except:
                messages.error(request,'후기를 등록하려면 인증사진을 첨부하셔야합니다.')
                return redirect('board:comment_create', id=shop.id)
            shop_comment.author = request.user
            shop_comment.create_date = timezone.now()
            shop_comment.shop = shop
            shop_comment.save()
            return redirect('board:shop_comment', id=shop.id)
    else:
        form = ShopCommentForm()
    content = {'form':form,'shop_name':shop.name}
    return render(request,'board/board_form.html',content)


def shop_comment_modify(request,id):
    page = request.GET.get('page', '1')
    shop_comment = get_object_or_404(ShopComment, pk=id)

    if request.method == "POST":
        form = ShopCommentForm(request.POST, instance=shop_comment)
        if form.is_valid():
            shop_comment = form.save(commit=False)
            if request.POST.get('filename',True):
                shop_comment.image = request.FILES['filename']
            shop_comment.author = request.user
            shop_comment.save()
            list = ShopComment.objects.order_by('-create_date').filter(author =request.user)
            paginator = Paginator(list, 10)  # 페이지당 10개씩 보여주기
            page_obj = paginator.get_page(page)
            return render(request,'mypage/mypage.html',{'so':'comment_list','list':page_obj})
    else:
        form = ShopCommentForm(instance=shop_comment)
    content = {'form':form,'shop_name':shop_comment.shop.name,'image':shop_comment.image}
    return render(request,'board/board_form.html',content)


def shop_comment_delete(request,id):
    page = request.GET.get('page', '1')
    shop_comment = get_object_or_404(ShopComment, pk=id)

    shop_comment.delete()
    list = ShopComment.objects.order_by('-create_date').filter(author=request.user)
    paginator = Paginator(list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    return render(request, 'mypage/mypage.html', {'so': 'comment_list', 'list': page_obj})






from django import forms

from board.models import *


class ShopCommentForm(forms.ModelForm):
    class Meta:
        model = ShopComment
        fields = ['content']
        labels = {
            'content':'내용',
        }
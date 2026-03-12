from django import forms
from .models import Board, BoardList


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description', 'background_color']


class BoardListForm(forms.ModelForm):
    class Meta:
        model = BoardList
        fields = ['name', 'color']

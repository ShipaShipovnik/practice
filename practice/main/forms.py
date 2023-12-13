from .models import Position
from django.forms import ModelForm, TextInput,Textarea


class PosForm(ModelForm):
    class Meta:
        model = Position
        fields = ["name", "type", "gramm", "sostav", "price"]
        widgets = {
            "name": TextInput(attrs={'placeholder': 'Название'}),
            "type": TextInput(attrs={'placeholder': 'Тип'}),
            "gramm": TextInput(attrs={'placeholder': 'Граммы'}),
            "sostav":Textarea(attrs={'placeholder': 'Описание'}),
            "price": TextInput(attrs={'placeholder': 'Цена в руб.'}),
        }

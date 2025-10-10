from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'price', 'original_price', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-2 px-4 rounded-xl border'}),
            'category': forms.Select(attrs={'class': 'w-full py-2 px-4 rounded-xl border'}),
            'price': forms.NumberInput(attrs={'class': 'w-full py-2 px-4 rounded-xl border'}),
            'original_price': forms.NumberInput(attrs={'class': 'w-full py-2 px-4 rounded-xl border'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-2 px-4 rounded-xl border', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full py-2 px-4 rounded-xl border'}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category', 'price', 'original_price', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-2 px-4 rounded-xl border'}),
            'category': forms.Select(attrs={'class': 'w-full py-2 px-4 rounded-xl border'}),
            'price': forms.NumberInput(attrs={'class': 'w-full py-2 px-4 rounded-xl border'}),
            'original_price': forms.NumberInput(attrs={'class': 'w-full py-2 px-4 rounded-xl border'}),
            'description': forms.Textarea(attrs={'class': 'w-full py-2 px-4 rounded-xl border', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'w-full py-2 px-4 rounded-xl border'}),
        }

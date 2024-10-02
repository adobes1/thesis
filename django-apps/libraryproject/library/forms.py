from django import forms
from library.models import Book


class BookForm(forms.ModelForm):
    publication_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d'),
        input_formats=['%d.%m.%Y'],
        required=False
    )

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'pages', 'status']

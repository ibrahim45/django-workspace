from django import forms
# from django.forms.models import inlineformset_factory
from polls.models import Author, Book
from django.forms import  formset_factory


class ArticleForm(forms.Form):
	title = forms.CharField(max_length=100)

# book_form_set = inlineformset_factory(Author, Book, exclude=['author'], can_delete=True)

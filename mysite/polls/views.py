from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Choice, Question, Book, Rating, Author
from polls.forms import ArticleForm
from django.forms import formset_factory, inlineformset_factory


def test(request):
    art_form_set = formset_factory(ArticleForm, can_delete=True, extra=2)
    form_set = art_form_set(request.POST or None)
    if form_set.is_valid() and request.method == 'POST':
        print "cool+code"
    context = {
        'form': form_set,
    }
    return render(request, 'test.html', context)


def test1(request):
    author = Author.objects.get(id=1)
    rate = Rating.objects.get(id=1)
    book_inlineform_set = inlineformset_factory(Author, Book, fk_name='author', fields=('title',))
    if request.method == 'POST':
        form_set = book_inlineform_set(request.POST)
        if form_set.is_valid():
            for f in form_set:
                Book.objects.create(
                    author=author,
                    title=f.cleaned_data['title'],
                    rate_book=rate
                )
                print "cool+code"
    context = {
            'form': book_inlineform_set,
    }
    return render(request, 'sample.html', context)


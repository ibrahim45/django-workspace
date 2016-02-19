from django.core.urlresolvers import reverse
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from registration_app.models import Author, Book, Album
from registration_app.forms import AuthorForm, BookForm
from django.contrib import messages


def index(request):
    author_form = AuthorForm(request.POST or None)
    book_form = BookForm(request.POST or None)
    if request.method == 'POST' and author_form.is_valid() and book_form.is_valid():
        print "stay hungry"
    context = {
        'author_form': author_form,
        'book_form': book_form,

    }
    return render(request, 'registration/test.html', context)


def manage_albums(request):
    AlbumFormSet = modelformset_factory(Album, can_order=True, can_delete=True,
                                        fields=['artist', 'name', 'release', ])
    if request.method == 'POST':
        formset = AlbumFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset.ordered_forms:
                form.instance.order = form.cleaned_data['ORDER']
            formset.save()
            messages.success(request, u"Formset edited successfully.")
            return HttpResponseRedirect(reverse('formsets'))
        else:
            messages.error(request, u"Please correct the errors below.")

    else:
        formset = AlbumFormSet(queryset=Album.objects.order_by('order'))
    return render(request, 'manage_albums.html', {'formset': formset})

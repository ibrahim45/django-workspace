from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
# from django.template.context import RequestContext
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


def save_profile(user, backend, response, details, strategy, social, *args, **kwargs):
    if backend.name == 'facebook':
        import ipdb;ipdb.set_trace();
        user = User.objects.get(id=user.id)
        user.username = details['email']
        user.first_name = details['first_name']
        user.last_name = details['last_name']
        user.email = details['email']
        user.save()
    else:
        import ipdb;ipdb.set_trace();
        print backend.name  # google-oauth2

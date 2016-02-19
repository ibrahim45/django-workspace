from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# from login_app.forms import SignupForm
# from login_app.models import Signup
# from backend.backends import MyAuth
#
#
# def signup(request):
#     form = SignupForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         user = User.objects.create(
#             first_name=form.cleaned_data['first_name'],
#             last_name=form.cleaned_data['last_name'],
#             email=form.cleaned_data['email'],
#             password=form.cleaned_data['password']
#         )
#         signup_value = Signup(user=user)
#         signup_value.save()
#         return HttpResponse('cool its works')
#     return render(request, 'signup.html', {'form': form})
#
#
# def auth(request):
#     c = MyAuth()
#     email = 'kibrahimsha4@gmail.com'
#     password = 'kibrahimsha4'
#     test_value = c.authenticate(email, password)
#     print test_value
#     return HttpResponse('authenticated')



from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


class LoginView(LoginRequiredMixin, View):
    login_url = '/Signin/'

@method_decorator(csrf_exempt, name='dispatch')
class SignInView(TemplateView):
    template_name = "index.html"

    def post(self, request, *args, **kwargs):
        error = None
        try:
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                 login(request, user)
                 return HttpResponseRedirect(reverse('Login:home_page'))
            else:
                error = 'Username or Password Incorrect'
        # No backend authenticated the credential
        except Exception as e:
            error = str(e)

        return HttpResponseRedirect(reverse('Login:signin')+'?login=failed')


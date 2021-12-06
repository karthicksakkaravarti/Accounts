from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView


class LandingView(LoginRequiredMixin, TemplateView):
    login_url = '/Signin/'
    template_name = "index.html"


@method_decorator(csrf_exempt, name='dispatch')
class SignInView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if (request.user.is_authenticated):
            return HttpResponseRedirect(reverse('Login:home_page'))
        else:
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        error = None

        try:
            req = HttpResponseRedirect(reverse('Login:home_page'))
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                 login(request, user)
                 req.set_cookie('login', True, max_age=None)
                 return req
            else:
                error = 'Username or Password Incorrect'
        # No backend authenticated the credential
        except Exception as e:
            print("Exception", str(e))
            error = str(e)

        return HttpResponseRedirect(reverse('Login:signin')+'?login=failed')


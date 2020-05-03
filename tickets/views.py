from django.views import View
from django.shortcuts import render


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'welcome.html')


def menu(request):
    return render(request, 'menu.html')

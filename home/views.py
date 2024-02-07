from django.shortcuts import render
from django.views import View


class GoHome(View):
    def get(self, request):
        return render(request, 'index/index.html')

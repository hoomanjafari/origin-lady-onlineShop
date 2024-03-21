from django.shortcuts import (render, redirect)
from django.views import View


class AboutUsView(View):
    def get(self, request):
        return render(request, 'about_us/about-us.html')

from django.shortcuts import render
from django.views import View
from shop.models import AllClothes


class SearchView(View):
    def get(self, request):
        result = AllClothes.objects.all()
        searched = request.GET.get('search')
        if request.GET.get('search'):
            result = result.filter(item_name__contains=request.GET['search'])
        return render(request, 'shop/search_result.html', {'result': result, 'searched': searched})

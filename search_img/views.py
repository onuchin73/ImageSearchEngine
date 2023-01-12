from asgiref.sync import sync_to_async
from django.shortcuts import render
from django.views import View

from .forms import SearchForm
from .services import search_image


class SearchImageView(View):
    async def get(self, request):
        return await sync_to_async(render)(request, 'search_img/index.html', {'form': SearchForm()})

    async def post(self, request):
        form = SearchForm(request.POST)
        images = []
        if form.is_valid():
            images = await search_image(form.cleaned_data['image_type'], form.cleaned_data['count'])
        return await sync_to_async(render)(request, 'search_img/index.html', {'form': SearchForm(), 'images': images})

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Image

IMAGES_PER_PAGE = 5

def image_list(request):
    object_list = Image.objects.all()
    paginator = Paginator(object_list, IMAGES_PER_PAGE)
    page = request.GET.get('page') # current page number
    try:
        images = paginator.page(page) # objects for current page
    except PageNotAnInteger: # if number is weird, then give the first
        images = paginator.page(1)
    except EmptyPage: # if it exceeds the max, then set the last one
        images = paginator.page(paginator.num_pages)
    return render(request, 
                 'image_handler/list.html', 
                 {'images': images,})

def image_detail(request, id):
    img = get_object_or_404(Image, pk=id)
    return render(request,
                'image_handler/detail.html',
                {'image': img,})

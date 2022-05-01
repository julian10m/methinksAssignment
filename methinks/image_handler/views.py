from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
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
    comments = img.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.image = img
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render(request,
                'image_handler/detail.html',
                {'image': img,
                 'comments': comments,
                 'new_comment': new_comment,
                 'comment_form': comment_form,
                 })

from django.shortcuts import render, get_object_or_404
from django.utils import datetime
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now()).order_by('published_date')
    return render(request, 'blogengine/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogengine/post_detail.html', {'post': post})

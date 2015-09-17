from django.shortcuts import render, get_object_or_404
import datetime
from .models import Post
from .forms import ContactForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now()).order_by('published_date')
    return render(request, 'blogengine/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogengine/post_detail.html', {'post': post})

def contact_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'blogengine/contact.html', {'form': form})
def about(request):
    return render(request, 'blogengine/about.html')

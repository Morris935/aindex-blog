from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# create a view to display published posts
def post_list(request):
    post_list = Post.published.all()
    
    # pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver first page of the result
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of the results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html',{'posts':posts})

# create a view to display details of individual post
def post_details(request, year, month, day, post):
    post = get_object_or_404(Post, 
                             status=Post.Status.PUBLISHED, 
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post':post})
    
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No post found")
    
    # return render(request, 'blog/post/detail.html',{'post':post}) 


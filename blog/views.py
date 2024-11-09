from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    # return HttpResponse(f"List of posts: {posts}")
    return render(request, 'blog/post_list.html', {'posts': posts})

from django.shortcuts import render,get_object_or_404
from blog.models import Post

def blog_view(request):
    x1 = Post.objects.all()
    x2 = {'x1':x1}
    return render (request,'blog/blog-home.html',x2)
def blog_single(request,pid):
    y1 = get_object_or_404(Post,pk=pid)
    y2 = {'y1':y1}
    return render (request,'blog/blog-single.html',y2)
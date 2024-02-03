from django.shortcuts import render

def blog(request):
    return render(request, 'blog/blog.html')

def post_detail(request):
    return render(request, 'blog/blog_single.html')

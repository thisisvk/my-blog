from django.shortcuts import render
from .models import Post
from posts.forms import PostForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})
def upload(request):
    upload = PostForm()
    if request.method == 'POST':
        upload = PostForm(request.POST)
        if upload.is_valid():
            upload.save()
            return HttpResponseRedirect('/')
    return render(request , 'upload.html',{'form':upload})
def delete_view(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/')
def update_view(request,id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    return render(request,'update.html',{'post':post})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate,login,logout
from . forms import PostForm, UserForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.db.models import Q


@login_required(login_url='posts:user_login')
def index(request):
    posts = Post.objects.all()

    query = request.GET.get("q")
    if query:
        posts = posts.filter(
            Q(title__icontains=query)
        ).distinct()
        return render(request, 'posts/index.html', {'posts': posts})
    else:
        return render(request, 'posts/index.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})


def addpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.image = request.FILES['image']
            post.save()
            return redirect('/')
    else:
        form = PostForm
        return render(request, 'posts/addpost.html', {'form': form})


def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('/')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user= authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
    return render(request, 'posts/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'posts/login.html', {'error_message': 'Account Inactive'})

        else:
            return render(request, 'posts/login.html', {'error_message': 'Invalid login!!'})
    else:
        return render(request, 'posts/login.html')


def user_logout(request):
    logout(request)
    form = UserForm(request.POST or None)
    return render(request, 'posts/login.html',{'form': form})


def favorite(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.is_favorite:
        post.is_favorite = False

    else:
        post.is_favorite = True
    post.save()
    return redirect('/favorites')


def favorites(request):
    user = request.user
    posts = Post.objects.filter(is_favorite=True)
    return render(request, 'posts/favorites.html', {'posts': posts, 'user': user})




from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, PostImage, About
from .forms import PostForm, PostImageFormSet
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        formset = PostImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for image_form in formset.cleaned_data:
                if image_form and image_form.get('image'):
                    PostImage.objects.create(post=post, image=image_form['image'])
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        formset = PostImageFormSet(queryset=PostImage.objects.none())
    return render(request, 'blog/post_create.html', {'form': form, 'formset': formset})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('public_post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def about(request):
    about_obj = About.objects.first()
    return render(request, 'blog/about.html', {'about': about_obj})
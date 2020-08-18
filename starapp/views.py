from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from . forms import UserRegisterForm,PostForm,UpdateUserProfileForm,RatingsForm
from . models import Profile,Post,Rating

def home(request):
    posts = Post.all_posts().order_by('-pub_date')
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
    else:
        form = PostForm()
    return render(request, 'home.html', {'posts':posts})

def project_by_id(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'project.html',{'posts':post})

def profile(request):
    return render(request, 'profile.html')

@login_required(login_url="login")
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            proj_post = form.save(commit=False)
            proj_post.profile = current_user
            proj_post.save()
        return redirect('star-home')
    else:
        form = PostForm()
    return render(request,'new_post.html',{"form": form})

def search_results(request):
    pass

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            new_user = User.objects.create_user(username = username,email = email)
            new_user.save()
            new_user.set_password(password)
            new_user.save()
            messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html',{'form': form})

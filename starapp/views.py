from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from . forms import UserRegisterForm,PostForm,UpdateUserProfileForm,RatingsForm
from . models import Profile,Post,Rating
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from . serializers import PostsSerializer,ProfileSerializer
from rest_framework import status

class PostsList(APIView):
    def get(self, request, format=None):
        all_posts = Post.objects.all()
        serializers = PostsSerializer(all_posts, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_posts = Profile.objects.all()
        serializers = ProfileSerializer(all_posts, many=True)
        return Response(serializers.data)

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

@login_required(login_url="login")
def project(request,id):
    post = Post.objects.get(id=id)
    ratings = Rating.objects.filter(profile=request.user, post=id).first()
    rating_status = None
    if ratings is None:
        rating_status = False
    else:
        rating_status = True
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = request.user
            rate.post = post
            rate.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = RatingsForm()
    return render(request, 'project.html',{'post': post,'form': form,'rating_status': rating_status})

def profile(request,id):
    user = User.objects.get(id=id)
    posts = Post.objects.filter(profile=user)
    return render(request, 'profile.html',{'posts':posts,'user':user})

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
    if 'search' in request.GET and request.GET['search']:
        name = request.GET.get("search")
        results = Post.search_project(name)
        message = f'{name}'
        return render(request, 'search.html', {'results':results,'message':message})
    else:
        message = f"No results for{name}"
        return render(request, 'search.html', {'message': message})


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

from django.conf import settings
from django.contrib.auth.models import User
from .models import Follow
from django.shortcuts import redirect, render
from .forms import SignupForm, FollowModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

def my_log(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        pass

def signup(request):
    if request.method == 'POST':
        login_form = SignupForm(request.POST)
        if login_form.is_valid():
            login_form.save()
            return redirect(settings.LOGIN_URL)
    else:
        login_form = SignupForm()
    return render(request, 'signup_form.html', {
        'login_form': login_form,
        })

def index(request):
    user = User.objects.all()
    return render(request, 'accounts/index.html', {
        'user':user,
        })

@login_required
def follow(request):
    if request.method == 'POST':
        follow_form = FollowModelForm(request.POST)
        if follow_form.is_valid():
            follow = follow_form.save(commit=False)
            follow.from_user = request.user
            follow.save()
            return redirect('/accounts/follow/')
    else:
        follow_form = FollowModelForm()
    return render(request, 'accounts/follow_form.html', {
        'follow_form': follow_form,
        })

@login_required
def request_list(request):
    follow_list = Follow.objects.filter(to_user=request.user)
    return render(request, 'accounts/follow_list.html',{
        'follow_list':follow_list,
        })

@login_required
def friend_list(request):
    follower_list = Follow.objects.filter(to_user=request.user).filter(is_approved=True)
    following_list = Follow.objects.filter(from_user=request.user).filter(is_approved=True)
    return render(request, 'accounts/friend_list.html', {
        'follower_list':follower_list,
        'following_list':following_list,
        })

@login_required
def aprv_request_list(request, pk):
    try:
        follow_request = Follow.objects.get(pk=pk)
    except follow_request.DoesNotExist:
        return redirect('accounts:request_list')
    else:
        follow_request.is_approved = True
        follow_request.save()
        return redirect('accounts:request_list')

@login_required
def del_request_list(request, pk):
    try:
        follow_request = Follow.objects.get(pk=pk)
    except follow_request.DoesNotExist:
        return redirect('accounts:request_list')
    else:
        follow_request.delete()
    return redirect('accounts:request_list')
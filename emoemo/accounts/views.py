from django.conf import settings
from django.contrib.auth.models import User
from .models import Follow
from django.shortcuts import redirect, render
from .forms import SignupForm, FollowModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.db.models import Count, Q
from django.views.decorators.http import require_POST
from django.http import JsonResponse


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
        sign_up_form = SignupForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
            return redirect(settings.LOGIN_URL)
    else:
        sign_up_form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'sign_up_form': sign_up_form,
        })

def index(request):
    user = User.objects.all()
    return render(request, 'accounts/index.html', {
        'user':user,
        })

@login_required
def follow(request):
    user_list = User.objects.all()
    follow_list = Follow.objects.filter(is_approved=False).filter(to_user=request.user)
    follower_list = Follow.objects.filter(is_approved=True).filter(Q(to_user=request.user) | Q(from_user=request.user))
    friend_set = set()
    for follow in follower_list:
        friend_set.add(follow.to_user)
        friend_set.add(follow.from_user)
    if request.user in friend_set:
        friend_set.discard(request.user)
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
        'form' : follow_form,
        'user_list': user_list,
        'follow_list' : follow_list,
        'friend_set' : friend_set,
        })

@login_required
def request_list(request):
    follow_list = Follow.objects.filter(to_user=request.user)
    return render(request, 'accounts/follow_list.html',{
        'follow_list':follow_list,
        })

@login_required
def friend_list(request):
    follower_list = Follow.objects.filter(is_approved=True).filter(Q(to_user=request.user) | Q(from_user=request.user))
    friend_set = set()
    for follow in follower_list:
        friend_set.add(follow.to_user)
        friend_set.add(follow.from_user)
    if request.user in friend_set:
        friend_set.discard(request.user)
    return redirect('accounts:friend_list')


@login_required
@require_POST
def aprv_request_list(request, pk):
    try:
        follow_request = Follow.objects.get(pk=pk)
    except follow_request.DoesNotExist:
        return JsonResponse({"ok": False}, safe=False)
    else:
        follow_request.is_approved = True
        follow_request.save()
        return JsonResponse({"ok": True, "from_user_name": follow_request.from_user.username, "to_user_name": follow_request.to_user.username}, safe=False)


@login_required
def del_request_list(request, pk):
    try:
        follow_request = Follow.objects.get(pk=pk)
    except follow_request.DoesNotExist:
        return redirect('accounts:request_list')
    else:
        follow_request.delete()
    return redirect('accounts:request_list')

def search_follow(request):
    if request.method=="POST":
        form = FollowModelForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.from_user = request.user
            form.save()
    return redirect('accounts:follow')
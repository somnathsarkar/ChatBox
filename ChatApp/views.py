from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import User,Message,Friendship
import datetime
from django.utils import timezone
from .forms import SignUpForm
from django.core import serializers
from django.db.models import Q

def home(request):
    if request.user.is_authenticated():
        friends = Friendship.objects.filter(user_A = request.user.username)
        return render(request,'account.html',{'user':request.user,'msgs':Message.objects.all(), 'friends' : friends})
    else:
        return render(request, 'home.html')

def account(request,parameter):
    friends = Friendship.objects.filter(user_A = request.user.username)
    recipient = None
    try:
        recipient = User.objects.get(username=parameter)
    except:
        pass
    msgs = Message.objects.filter((Q(creator_id=request.user.username)&Q(recipient_id=recipient.username))|(Q(creator_id=parameter)&Q(recipient_id=request.user.username))).order_by('create_date')
    return render(request,'account.html',{'user':request.user,'recipient':recipient,'msgs':msgs, 'friends' : friends})

@login_required
def addfriends(request):
        return render(request,'addfriends.html')

def mssgs(request):
    if request.method == 'POST':
        search_username = request.POST.get('username',None)
        search_string = request.POST.get('string',None)
        umssgs = Message.objects.all()
        if(len(search_username)>0 and len(search_string)==0):
             umssgs = Message.objects.filter(creator_id = search_username)
        elif(len(search_username)==0 and len(search_string)>0):
            umssgs = Message.objects.filter(message_body__icontains = search_string)
        return render(request,'mssgsresults.html',{'mssgs':umssgs})
    else:
        return render(request,'mssgs.html')

@login_required
def addfriendsresults(request):
    if request.method == 'POST':
        search_id = request.POST.get('username',None)
        del_id = request.POST.get('del_username',None)
        u1 = get_object_or_404(User, username = request.user.username)
        if(len(search_id)>0):
            u2 = get_object_or_404(User, username = search_id)
            f = Friendship(user_A = u1, user_B = u2)
            f.save()
            f = Friendship(user_A = u2, user_B = u1)
            f.save()
            return render(request,'addfriendsresults.html',{'friend':u2})
        else:
            u2 = get_object_or_404(User, username = del_id)
            Friendship.objects.filter(user_A = u1, user_B = u2).delete()
            Friendship.objects.filter(user_A = u2, user_B = u1).delete()
            return home(request)

@login_required
def searchfriends(request):
    return render(request,'searchfriends.html')

@login_required
def searchfriendsresults(request):
    if request.method == 'POST':
        search_id = request.POST.get('username',None)
        user = get_object_or_404(User, username = search_id)
        return render(request,'searchfriendsresults.html',{'searched_result':user})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            uname = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            f_name = form.cleaned_data.get('first_name')
            l_name = form.cleaned_data.get('last_name')
            user = authenticate(username=uname, password=raw_password)
            login(request, user)
            u = User(username = uname, first_name = f_name, last_name = l_name, create_date = timezone.now(),is_active = request.user.is_active)
            u.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User #Friends
from django.shortcuts import render, HttpResponseRedirect, redirect, reverse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'board/index.html')

def friends(request):
    context = {
        'recent': Review.objects.recent_and_not()[0],
        'more': Review.objects.recent_and_not()[1]
    }
    return render(request, 'board/friends.html', context)

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return HttpResponseRedirect(reverse("board:index"))

def logout(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')

def register(request):
    result = User.objects.validate_registration(request.POST)
    print result, type(result)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return HttpResponseRedirect(reverse("board:index"))

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'board/success.html', context)

def show(request, user_id):
    user = User.objects.get(id=user_id)
    unique_ids = user.friends_left.all().values("friends").distinct()
    #unique_friends = []
    for friends in friend_list:
        unique_friends.append(Friend.objects.get(id=friend['friend']))
    context = {
        'user': user,
        'unique_friends': unique_friends
    }
    return render(request, 'board/show.html', context)

def add(request):
    context = {
        "friends": friends.objects.all()
    }
    return render(request, 'board/add.html', context)

#def other_users(request):

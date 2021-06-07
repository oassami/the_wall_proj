from django.shortcuts import render, redirect
from .models import Message, Comment
from django.contrib import messages
from ..login_app.models import User
from datetime import date, time, datetime, timedelta, timezone

def get_day_ordinal(d):
    sDay = '%dth'
    if d.day <= 10 or d.day >= 21:
        sDay = '%dst' if d.day % 10 == 1 else sDay
        sDay = '%dnd' if d.day % 10 == 2 else sDay
        sDay = '%drd' if d.day % 10 == 3 else sDay
    new_date_format = d.strftime("%B ") + sDay % d.day + d.strftime(" %Y") 
    return new_date_format

def index(request):
    context={
        'all_messages': Message.objects.all(),
        'all_comments': Comment.objects.all(),
    }
    for k in context:
        for v in context[k]:
            time_now = datetime.now(timezone.utc)
            delta = v.created_at + timedelta(minutes=30)
            if time_now > delta:
                v.user.id = ''
            v.created_at = get_day_ordinal(v.created_at)
    return render(request, 'wall.html', context)

def msg_create(request):
    this_user = User.objects.get(id=request.session['user_id'])
    my_message = Message.objects.create(message_txt=request.POST['msg_text'], user=this_user)
    return redirect('/wall')

def cmnt_create(request):
    this_user = User.objects.get(id=request.session['user_id'])
    this_msg = Message.objects.get(id=request.POST['msg_id'])
    my_comment = Comment.objects.create(comment_txt=request.POST['cmnt_text'], user=this_user, message=this_msg)
    return redirect('/wall')

def msg_delete(request, msg_id):
    msg = Message.objects.get(id=msg_id)
    msg.delete()
    return redirect('/wall')

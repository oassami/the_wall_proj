from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import date, time, datetime
from .models import *
import bcrypt


def index(request):
    if 'user_id' in request.session:
        # del request.session['logged_user']
        request.session.clear()
    return render(request, 'index.html')

def user_register(request):
    request.session.clear()
    request.session['first_name']= request.POST['first_name']
    request.session['last_name']= request.POST['last_name']
    request.session['email']= request.POST['email']
    request.session['birthday']= request.POST['birthday']
    request.session['action']= 'register'
    errors = User.objects.addValidation(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
    user = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'], 
        email = request.POST['email'], 
        birthday = request.POST['birthday'], 
        password = pw_hash
    )

    # ****** This is good to have if you didn't auto logged in the user after registaring ******

    # messages.info(request, "You have created an account! Please log in...")
    # request.session['logged-in'] = "logged-in"
    request.session['user_id'] = user.id

    # request.session['create_at'] = 

    # return redirect(f'/wall/{user.id}')
    return redirect('/wall')

def user_login(request):
    request.session.clear()
    request.session['login_email'] = request.POST['email']
    request.session['action'] = 'login'
    errors = User.objects.loginValidation(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')

    # ****** This is good programming, however, below is a better way of doing it with TRY and EXCEPT. *******
    # user = User.objects.filter(email=post_data['email'])
    # if not user:
    #     errors['user'] = 'This user does NOT exist in the database!'
    # else:
    #     user = User.objects.get(email=post_data['email'])
    #     if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
    #         errors['password'] = 'WRONG Password!!!'
    try:
        user = User.objects.get(email = request.POST['email'])
        if not bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            messages.error(request, 'Incorrect email address or password.')
            return redirect('/')
    except:
        messages.error(request, 'Incorrect email address or password.')
        return redirect('/')
    request.session['user_id'] = user.id
    request.session['first_name'] = user.first_name
    request.session['last_name'] = user.last_name
    # request.session['email']= user.email
    # request.session['birthday']= request.POST['birthday']
    # request.session['action']= 'register'
    # request.session['logged-in'] = "logged-in"
    # return redirect(f'/wall/{user.id}')
    return redirect('/wall')


# ****** No need for this in this assignment because on successful 
#        login I'll redirect to the other app (wall_app)   *******
# def user_success(request):
#     if 'logged-in' not in request.session:
#         return redirect('/clear_all')
#     context = {
#         'user_id': request.session['user_id'],
#         'first_name': request.session['first_name'],
#         'action': request.session['action'],
#     }
#     request.session.clear()
#     return render(request, 'success.html', context')

def clear_forms(request):
    request.session.clear()
    return redirect('/')

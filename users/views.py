import json

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from users.models import User, Calendar


def index(request):
    msg = 'My Message'
    user_id = request.session.get('user_id')
    if user_id:

        if request.method == "POST":
            print(123)
            title = request.POST['resv_title']
            user_name = User.objects.filter(id=user_id)[0].User_name
            body = request.POST['resv_body']
            time = request.POST['time']
            Calendar.objects.create(title=title, body=body, event_date=time, user_name=user_name, is_active=True)
            print(Calendar.objects.all())
        user = User.objects.get(id=user_id)
        messages.success(request, user.User_name)
      
        return render(request, "home/home.html", {"user": user.First_name})
        # return render(request, 'calendar/calendar.html')
    return render(request, 'index.html')

def home(View):
  def get(self, request):
    user = request.session["User_name"]
    return render(request, "home/home.html", {"user": user})
    

def cal(request):
    # model = Calendar
    # template_name = 'cal/calenda=r.html'

    # context = super().get_context_data(**kwargs)

    # use today's date for the calendar

    # Instantiate our calendar class with today's year and date
    # cal = Calendar(d.year, d.month)

    # Call the formatmonth method, which returns our calendar as a table
    # html_cal = cal.formatmonth(withyear=True)
    # context['calendar'] = mark_safe(html_cal)
    return render(request, 'calendar/calendar.html')


def logout_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        request.session["user_id"] = None
        return redirect('/')

def profile_view(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        messages.success(request, user.User_name)
        return render(request, 'users/profile.html', {})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['firstname']
        # middle_name = request.POST['middlename']
        last_name = request.POST['lastname']
        # gender = request.POST['gender']
        # date_of_birth = request.POST['birthday']

        user = User.objects.filter(User_name=username)
        if user:
            messages.warning(request, "Sign-Up Failed")
        else:
            User.objects.create(First_name=first_name, Last_name=last_name, User_name=username, password=password)
            messages.warning(request, "Membership Was Successful")
            HttpResponseRedirect("/")
    return render(request, 'users/signUp.html', {})

def signin_view(request):
    if request.session.get('user_id'):
        messages.warning(request, "already logged in")
        return redirect("/")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.filter(User_name=username, password=password)
        if user:
            request.session["user_id"] = user[0].id
            return redirect("/")

            # HttpResponseRedirect("/")
        else:
            messages.warning(request, "fail")
    return render(request, 'users/signIn.html',{})

def files(request):
  return render(request, 'home/importantFiles.html')

def applications(request):
  return render(request, 'home/processOfApp.html')
  
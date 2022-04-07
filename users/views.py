import json
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from users.models import User, Calendar, Document
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django import forms
from users.forms import DocumentForm

#
# currently working on uploading a file w/ https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
#
#




def app_org(request):
  return render(request, 'users/appOrg.html')

#########################################################
def ajax_resv_list(request):
    # POST 요청일 때
    if request.method == 'POST':
        data = json.loads(request.body)
        resv_list = list(Calendar.objects.filter(event_date__icontains=data).values())
        context = {
            'resv_list' : resv_list
        }
        return JsonResponse(context)


def index(request):
    msg = 'My Message'
    user_id = request.session.get('user_id')
    if user_id:

        if request.method == "POST":
            print(123)
            title = request.POST['resv_title']
            user_name = User.objects.filter(id=user_id)[0].User_name
            body = request.POST['resv_body']
            time = request.POST['onlydatetime']
            if title and user_name and body and time :
                cal = Calendar(title=title,
                         body = body,
                         event_date=time,
                         user_name=user_name,
                         is_active=True)
                cal.save()
                return redirect('/')
            #Calendar.objects.create(title=title, body=body, event_date=time, user_name=user_name, is_active=True)
            #print(Calendar.objects.all())
        #user = User.objects.get(id=user_id)
        #messages.success(request, user.User_name)
        context = {
            'cal_list': Calendar.objects.all(),
        }


        return render(request, "home/home.html", context)

        #return render(request, 'calendar/calendar.html')
    return render(request, 'index.html')
#########################################################

def home(View):
  def get(self, request):
    user = request.session["User_name"]
    return render(request, "home/home.html", {"user": user})

def cal(request):
    # model = Calendar
    #template_name = 'cal/calendar.html'

    # context = super().get_context_data(**kwargs)
    user_id = request.session.get('user_id')
    if user_id:

        if request.method == "POST":
            title = request.POST['resv_title']
            user_name = User.objects.filter(id=user_id)[0].User_name
            body = request.POST['resv_body']
            time = request.POST['onlydatetime']
            if title and user_name and body and time:
                cal = Calendar(title=title,
                               body=body,
                               event_date=time,
                               user_name=user_name,
                               is_active=True)
                cal.save()
                return redirect('/cal')
        context = {
            'cal_list': Calendar.objects.all(),
        }

        return render(request, "calendar/calendar.html", context)
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
        if username and password :
            print(request.POST['username'], request.POST['password'])
            user = User.objects.filter(User_name=username, password=password).first()
            print(user)
            if user:
                request.session["user_id"] = user.id
                request.session["user"] = User.objects.filter(User_name=username, password=password).values()[0]
            return redirect("/")

            # HttpResponseRedirect("/")
        else:
            messages.warning(request, "fail")
    return render(request, 'users/signIn.html',{})

def files(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'home/importantFiles.html', {
        'uploads': Document.objects.all()
    })
    else:
        form = DocumentForm()
    return render(request, 'home/importantFiles.html', {
        'form': form,
        'uploads': Document.objects.all()
    })

def applications(request):
  return render(request, 'home/processOfApp.html')
  
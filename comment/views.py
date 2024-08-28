from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
import re
from .models import *

# Create your views here.


def index(request):
    context = {
        'po': Post.objects.all(),
    }
    return render(request, 'pages/index.html', context)


def userdata(request):
    if request.method == 'POST' and 'btncreate' in request.POST:
        username = None
        email = None
        password = None
        is_added = None

        if 'username' in request.POST: username = request.POST['username']
        else:
            messages.error(request, '   يوجد خطأ في اسم المستخدم  ')

        if 'pass' in request.POST: password = request.POST['pass']
        else:
            messages.error(request, '   يوجد خطأ في كلمة المرور  ')

        if 'usermail' in request.POST: email = request.POST['usermail']
        else:
            messages.error(request, '  يوجد خطأ في البريد الالكتروني  ')

        if username and password and email:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'مستخدم موجود ')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'ايميل موجود')
                else:
                    patt = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                    if re.match(patt, email):

                        user = User.objects.create_user(username=username,
                                                        password=password,
                                                        email=email)
                        messages.success(request, 'مرحبا عميلنا العزيز ')
                        user.save()
                        return redirect('userdata')

                        # username = ''
                        # password = ''
                        # email = ''
                        # is_added = True

                    else:
                        messages.error(request,
                                       ' هناك خطأ في البريد الالكتروني')
        else:
            messages.error(request, 'تحقق من الحقول المدخلة')

        return render(request, 'pages/userdata.html', {
            'user': username,
            'pass': '',
            'email': email,
            'is_added': is_added
        })
    else:
        return render(request, 'pages/userdata.html')


def login(request):
    if request.method == 'POST' and 'btnlogin' in request.POST:

        username = request.POST['username']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'مرحبا عميلنا العزيز ')
        else:
            messages.error(request,
                           ' هناك خطأ في كلمة اسم المستخدم أو كلمة المرور')

        return redirect('index')
    else:
        return render(request, 'pages/login.html')


def logout(request):

    if request.user.is_authenticated:
        auth.logout(request)

    return redirect('index')


def pro(request):
    context = {
        'po': Post.objects.all(),
    }

    po = Post()

    if request.method == 'POST':
        po.user = request.user
        po.title = request.POST.get('title')
        po.dis = request.POST.get('dis')
        if len(request.FILES) != 0:
            po.file = request.FILES['file']
        po.save()
        messages.success(request, "تم إضافة الطلب بنجاح!")
        return redirect('index')
    return render(request, 'pages/pro.html', context)


def pro_s(request, id):
    p = Products.objects.get(id=id)

    context = {
        'p': p,
        'c': Comments.objects.all(),
    }
    p = Products()
    c = Comments()

    if request.method == 'POST':
        c.comment = request.POST.get('comment')
        c.rating = request.POST.get('rating')
        c.save()
        messages.success(request, "تم إضافة طلبك بنجاح!")
        return redirect('pro')
    return render(request, 'pages/pro_s.html', context)


def comment(request):
    return render(request)


def edit(request, id):
    po = Post.objects.get(id=id)

    if request.method == "POST":
        po.title = request.POST.get('title')
        po.dis = request.POST.get('dis')
        if len(request.FILES) != 0:
            if len(po.file) > 0:
                os.remove(po.file.path)
            po.file = request.FILES['file']
        po.save()
        messages.warning(request, "تم تعديل الطلب بنجاح!")
        return redirect('index')
    context = {
        'po': po,
    }
    return render(request, 'pages/edit.html', context)


def delete(request, id):
    po = Post.objects.get(id=id)
    po.delete()
    messages.error(request, "تم حذف الطلب بنجاح!")
    return redirect('index')
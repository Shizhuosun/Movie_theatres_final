
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings

from login import models, forms
import hashlib
import datetime

# Create your views here.


def logindex(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/logindex.html')


def login(request):
    if request.session.get('is_login', None):
        return redirect('/logindex/')
    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "Please double check your input！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            try:
                user = models.User.objects.get(name=username)
            except:
                message = "The user does not exist."
                return render(request, 'login/login.html', locals())

            if not user.has_confirmed:
                message = 'The user does not confirme.'
                return render(request, 'login/login.html', locals())


            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/logindex/')
            else:
                message = "Incorrect password!"
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
        if request.session.get('is_login', None):
            return redirect("/logindex/")

        if request.method == "POST":
            register_form = forms.RegisterForm(request.POST)
            message = "Please double check your input！"
            if register_form.is_valid():  # 获取数据
                username = register_form.cleaned_data['username']
                password1 = register_form.cleaned_data['password1']
                password2 = register_form.cleaned_data['password2']
                email = register_form.cleaned_data['email']
                sex = register_form.cleaned_data['sex']

                if password1 != password2:  # 判断两次密码是否相同
                    message = "The passwords are different!"
                    return render(request, 'login/register.html', locals())
                else:
                    same_name_user = models.User.objects.filter(name=username)
                    if same_name_user:  # 用户名唯一
                        message = 'This username already exists, please select a new one!'
                        return render(request, 'login/register.html', locals())
                    same_email_user = models.User.objects.filter(email=email)
                    if same_email_user:  # 邮箱地址唯一
                        message = 'This email address has been registered, please use another!'
                        return render(request, 'login/register.html', locals())

                    # 当一切都OK的情况下，创建新用户

                    new_user = models.User()
                    new_user.name = username
                    new_user.password = hash_code(password1)
                    new_user.email = email
                    new_user.sex = sex
                    new_user.save()

                    code = make_confirm_string(new_user)
                    send_email(email, code)

                    message = 'Please confirm by email！'
                    return render(request, 'login/confirm.html', locals())
            else:
                return render(request, 'login/register.html', locals())
        register_form = forms.RegisterForm()
        return render(request, 'login/register.html', locals())


def logout(request):
        if not request.session.get('is_login', None):
            # 如果本来就未登录，也就没有登出一说
            return redirect("/login/")
        request.session.flush()
        return redirect("/login/")



def hash_code(s, salt='theatres'):# 加点盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()



def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user,)
    return code

def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = 'Registration confirmation email'

    text_content = '''Your email server does not provide HTML links, please contact the administrator!'''

    html_content = '''
                    <p>Thank you for registering<a href="http://{}/confirm/?code={}" target=blank>https://luminus.nus.edu.sg/</a></p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    return code

def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = 'Invalid confirmation request!'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = 'Your mail has expired! Please re-register!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = 'Thank you for your confirmation. Please log in using your account！'
        return render(request, 'login/confirm.html', locals())

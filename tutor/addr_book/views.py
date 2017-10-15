from addr_book.models import *
from string import atoi
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.mail import EmailMultiAlternatives #, send_mail

subjects = ['yuwen', 'shuxue', 'yingyu', 'wuli', 'huaxue', 'shengwu', 'zhengzhi', 'lishi', 'dili']
day_time = list()
for i in xrange(1, 8):
    day_time.append("day"+str(i)+"_mor")
    day_time.append("day"+str(i)+"_aft")
    day_time.append("day"+str(i)+"_nig")

def total(list):    #Done
    counter = 0
    for temp in list:
        counter = counter + 1
    return counter
    
def getuser(request):   #Done
    user = User.objects.get(username = request.session['user_id'])
    return user

def updatepassword(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        if request.POST:
            post = request.POST
            user = getuser(request)
            if post['first_input'] == post['second_input']:
                user.password = post['first_input']
                user.save()
                return HttpResponseRedirect('/')
        return render_to_response('updatepassword.html')
    except KeyError:
        return HttpResponseRedirect('/')

def send_email(user):
    email = user.email
    if isinstance(email, unicode):
        email = email.encode('utf-8')
    content = render_to_response('send_email.html', Context({'user':user,}))
    subject,from_email,to = 'Get your password','13159877501@163.com',email
    text_content = user.password
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(content, 'text/html')
    msg.send()
    return HttpResponse('Please check your email to get the password!!')

def getpassword(request):   #Done
    if request.POST:
        post = request.POST
        user = User.objects.filter(username=post['username'])
        if total(user) > 0:
            user = User.objects.get(username=post['username'])
            if user.email == post['email']:
                send_email(user)
#                send_mail('Subject here', user.password, '13159877501@163.com', [user.email], fail_silently=False)
        return HttpResponse('The username or the password you input is incorrect!!')
    return render_to_response('getpassword.html')

def AboutUs(request):   #Done
    return render_to_response('AboutUs.html')

def ContactUs(request): #Done
    return render_to_response('ContactUs.html')

def login(request): #Done
    users_list = User.objects.all()
    c = Context({"users_list": users_list,})
    if request.POST:
        post = request.POST
        try:
            user = User.objects.get(username=post['username'])
            if user.password == post['password']:
                request.session['user_id'] = user.username
                return HttpResponseRedirect('/lookthrough_teacher')
            return render_to_response('login.html', c)
        except User.DoesNotExist:
            pass
    return render_to_response('login.html', c)

def register(request):  #Done
    if request.POST:
        post = request.POST
        if post['password'] == post['makesure']:
            new_user = User(
                    username = post['username'],
                    email = post['email'],
                    password = post['password'])
            teacher = Teacher()
            teacher.name = ''
            teacher.age = 21
            teacher.sex = True
            teacher.college = ''
            teacher.major = ''
            teacher.tel = 045000000000
            teacher.email = 'hfl@sina.cn'
            teacher.address = ''
            teacher.save()
            new_user.teacher = teacher
            new_user.save()
            request.session['user_id'] = new_user.username
            return HttpResponseRedirect('/lookthrough_teacher')
        return HttpResponseRedirect('/register')
    return render_to_response('register.html')

def logout(request):    #Done
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponseRedirect('/')

def passer_teacher(request):    #Done
    try:
        if request.session['user_id'] > 0:
            return HttpResponseRedirect('/lookthrough_student')
    except KeyError:
        pass
    student_list = Student.objects.all()
    c = Context({"students_list": student_list,})
    if total(student_list) > 0:
        return render_to_response('passer_teacher.html', c)
    return render_to_response('passer_teacher.html')

def passer_student(request):    #Done
    try:
        if request.session['user_id'] > 0:
            return HttpResponseRedirect('/lookthrough_teacher')
    except KeyError:
        pass
    teacher_list = Teacher.objects.all()
    c = Context({"teachers_list": teacher_list,})
    if total(teacher_list) > 0:
        return render_to_response('passer_student.html', c)
    return render_to_response('passer_student.html')

#for teacher
def newcontent_teacher(post):   #Done
    print "In the newcontent_teacher!"
    temp_subjects = ""
    temp_time = ""

    new_content_teacher = content_teacher()

    if post['wenli'] == 'False':
        new_content_teacher.wenli = False
        
    for j in xrange(8):
        try:
            if post[ subjects[j] ]:
                pass
            temp_subjects = temp_subjects + "1,"
        except KeyError:
            temp_subjects = temp_subjects + "0,"
    try:
        if post[ subjects[8] ]:
            pass
        temp_subjects = temp_subjects + "1"
    except KeyError:
        temp_subjects = temp_subjects + "0"
    new_content_teacher.subjects = temp_subjects
    
    for j in xrange(20):
        try:
            if post[ day_time[j] ]:
                pass
            temp_time = temp_time + "1,"
        except KeyError:
            temp_time = temp_time + "0,"
    try:
        if post[ day_time[20] ]:
            pass
        temp_time = temp_time + "1"
    except KeyError:
        temp_time = temp_time + "0"
    new_content_teacher.timeforteaching = temp_time
    new_content_teacher.getperhour = post['getperhour']
    new_content_teacher.save()
    return new_content_teacher

#to get the room for the new class
def updateteacher(teacher, post):   #Done
    try:
        teacher.name = post['name']
    except KeyError:
        teacher.name = ''
    try:
        teacher.sex = post['sex']
    except KeyError:
        teacher.sex = True
    try:
        teacher.age = post['age']
    except KeyError:
        teacher.age = True
    try:
        teacher.college = post['college']
    except KeyError:
        teacher.college = ''
    try:
        teacher.major = post['major']
    except KeyError:
        teacher.major = ''
    try:
        teacher.tel = post['tel']
    except KeyError:
        teacher.tel = ''
    try:
        teacher.email = post['email']
    except KeyError:
        teacher.email = '****@**.**'
    try:
        teacher.address = post['address']
    except KeyError:
        teacher.address = ''
    teacher.content.add( newcontent_teacher(post) )
    teacher.save()
    print "You are right!"

def lookone_teacher(request):   #Done
    student = Student.objects.get(id=request.GET['student_id'])
    content = content_student.objects.get(id=request.GET['content_id'])
    c = Context({"student":student,"content":content,'user':getuser(request),})
    return render_to_response('lookone_teacher.html', c)

def lookthrough_teacher(request):   #Done
    try:
        if request.session['user_id'] > 0:
            pass
        student_list = Student.objects.all()
        c = Context({"students_list": student_list, 'user':getuser(request),})
        if total(student_list) > 0:
            return render_to_response('lookthrough_teacher.html', c)
        return render_to_response('lookthrough_teacher.html')
    except KeyError:
        return HttpResponseRedirect('/')

def delete_teacher(request):    #Done
    get = request.GET
    content_teacher.objects.filter(id=get['part_id']).delete()
    return HttpResponseRedirect('/historypublish_teacher')

def newpublish_teacher(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        user = getuser(request)
        if request.POST:
            post = request.POST
            teacher = user.teacher
            teacher.content.add( newcontent_teacher(post) )
            teacher.save()
            user.save()
            return HttpResponseRedirect('/lookthrough_student')
        c = Context({"teacher": user.teacher, 'user':getuser(request),})
        return render_to_response('newpublish_teacher.html', c)
    except KeyError:
        return HttpResponseRedirect('/')

def historypublish_teacher(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        teacher = getuser(request).teacher
        c = Context({"teacher": teacher, 'user':getuser(request),})
        return render_to_response('historypublish_teacher.html', c)
    except KeyError:
        return HttpResponseRedirect('/')

def historyget_teacher(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        user = getuser(request)
        content_list = user.teacher.content.all()
        c = Context({"contents_list": content_list, 'user':getuser(request),})
        if total(content_list) > 0:
            return render_to_response('historyget_teacher.html', c)
        return render_to_response('historyget_teacher.html')
    except KeyError:
        return HttpResponseRedirect('/')

def praise_teacher(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        teacher = getuser(request).teacher
        c = Context({"teacher": teacher, 'user':getuser(request),})
        return render_to_response('praise_teacher.html', c)
    except KeyError:
        return HttpResponseRedirect('/')

def info_teacher(request):      #Done
    try:
        if request.session['user_id'] > 0:
            pass
        teacher = getuser(request).teacher
        c = Context({"teacher": teacher, 'user':getuser(request),})
        return render_to_response('info_teacher.html', c)
    except KeyError:
        return HttpResponseRedirect('/')

def search_teacher(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        if request.POST:
            post = request.POST
            costperhour = post['costperhour']
            wenli = post['wenli']
            content_list = content_student.objects.all()
            temp_list = list()
            for content in content_list:
                if content.freestate == False:
                    if atoi(costperhour) > 0:
                        if content.costperhour == atoi(costperhour):
                            if wenli == 'True':
                                if content.wenli == True:
                                    temp_list.append(content)
                            elif wenli == 'False':
                                if content.wenli == False:
                                    temp_list.append(content)
                            else:
                                temp_list.append(content)
                    else:
                        if wenli == 'True':
                            if content.wenli == True:
                                temp_list.append(content)
                        elif wenli == 'False':
                            if content.wenli == False:
                                temp_list.append(content)
                        else:
                            temp_list.append(content)
            c = Context({"contents_list": temp_list,'user':getuser(request),})
            return render_to_response('search_teacher.html', c)
        return render_to_response('search_teacher.html', Context({'user':getuser(request),}))
    except KeyError:
        return HttpResponseRedirect('/')

def updateinfo_teacher(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        teacher = getuser(request).teacher
        c = Context({"teacher": teacher, 'user':getuser(request),})
        if request.POST:
            post = request.POST
            teacher.name = post['name']
            teacher.sex = post['sex']
            teacher.age = post['age']
            teacher.college = post['college']
            teacher.major = post['major']
            teacher.tel = post['tel']
            teacher.address = post['address']
            teacher.email = post['email']
            teacher.save()
            return HttpResponseRedirect('/info_teacher')
        return render_to_response('updateinfo_teacher.html', c)
    except KeyError:
        return HttpResponseRedirect('/')


#for student
def newcontent_student(post):   #Done
    print "In the newcontent_student!"
    temp_subjects = ""
    temp_time = ""

    new_content_student = content_student()

    if post['wenli'] == 'False':
        new_content_student.wenli = False
        
    for j in xrange(8):
        try:
            if post[ subjects[j] ]:
                pass
            temp_subjects = temp_subjects + "1,"
        except KeyError:
            temp_subjects = temp_subjects + "0,"
    try:
        if post[ subjects[8] ]:
            pass
        temp_subjects = temp_subjects + "1"
    except KeyError:
        temp_subjects = temp_subjects + "0"
    new_content_student.subjects = temp_subjects
    
    for j in xrange(20):
        try:
            if post[ day_time[j] ]:
                pass
            temp_time = temp_time + "1,"
        except KeyError:
            temp_time = temp_time + "0,"
    try:
        if post[ day_time[20] ]:
            pass
        temp_time = temp_time + "1"
    except KeyError:
        temp_time = temp_time + "0"
    new_content_student.timerequest = temp_time
    new_content_student.sexrequest = post['sexrequest']
    print 'I am here'
    new_content_student.school = post['school']
    new_content_student.grade = post['grade']
    new_content_student.costperhour = post['costperhour']
    new_content_student.star = 0
    new_content_student.save()
    return new_content_student

def updatestudent(student, post):   #Done
    try:
        student.name = post['name']
    except KeyError:
        pass
    try:
        student.sex = post['sex']
    except KeyError:
        pass
    try:
        student.age = post['age']
    except KeyError:
        pass
    try:
        student.tel = post['tel']
    except KeyError:
        pass
    try:
        student.email = post['email']
    except KeyError:
        pass
    try:
        student.address = post['address']
    except KeyError:
        pass
    student.content.add( newcontent_student(post) )
    student.save()

def newstudent(student, post):   #Done
    try:
        student.name = post['name']
    except KeyError:
        student.name = ''
    try:
        student.sex = post['sex']
    except KeyError:
        student.sex = True
    try:
        student.age = post['age']
    except KeyError:
        student.age = True
    try:
        student.tel = post['tel']
    except KeyError:
        student.tel = ''
    try:
        student.email = post['email']
    except KeyError:
        student.email = '****@**.**'
    try:
        student.address = post['address']
    except KeyError:
        student.address = ''
    student.content.add( newcontent_student(post) )
    student.save()
    print 'YOU ARE RIGHT.'

def lookone_student(request):   #Done
    teacher = Teacher.objects.get(id=request.GET['teacher_id'])
    content = content_teacher.objects.get(id=request.GET['content_id'])
    c = Context({"teacher":teacher, "content":content, 'user':getuser(request),})
    return render_to_response('lookone_student.html', c)

def lookthrough_student(request):   #Done
    try:
        if request.session['user_id'] > 0:
            pass
        teacher_list = Teacher.objects.all()
        c = Context({"teachers_list": teacher_list,'user':getuser(request),})
        if total(teacher_list) > 0:
            return render_to_response('lookthrough_student.html', c)
        return render_to_response('lookthrough_student.html')
    except KeyError:
        return HttpResponseRedirect('/')

def add_student(request):   #Done
    try:
        if request.session['user_id'] > 0:
            pass
        if request.POST:
            post = request.POST
            student = Student()
            student.age = 0
            student.save()
            newstudent(student, post)
            user = getuser(request)
            user.student.add(student)
            user.save()
            return HttpResponseRedirect('/lookthrough_teacher')
        return render_to_response('newpublish_student.html')
    except KeyError:
        return HttpResponseRedirect('/')

def newone_student(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        student = Student.objects.get(id=request.GET['id'])
        c = Context({"student": student, 'user':getuser(request),})
        if request.POST:
            post = request.POST
            updatestudent(student, post)
            return HttpResponseRedirect('/lookthrough_teacher')
        return render_to_response('newpublish_student1.html', c)
    except KeyError:
        return HttpResponseRedirect('/')

def get0_content(content_list): #Done
    i = 0
    temp = 0
    for content in content_list:
        if i > 0:
            break
        temp = content.id
        i = i + 1
    print temp
    return temp

def newpublishone_student(request):     #Done
    student = Student.objects.get(id=request.GET['student_id'])
    content = content_student.objects.get(id=get0_content(student.content.all()))
    c = Context({"student": student, "content": content,'user':getuser(request),})
    if request.POST:
        post = request.POST
        updatestudent(student, post)
        return HttpResponseRedirect('/lookthrough_teacher')
    return render_to_response('newpublishone_student.html', c)

def deletecontent_student(request):     #Done
    content_student.objects.filter(id=request.GET['content_id']).delete()
    return HttpResponseRedirect('/historypublish_student')

def newpublish_student(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        user = getuser(request)
        student_list = user.student.all()
        if total(student_list) == 0:
            return render_to_response('newpublish_student0.html')
        c = Context({"students_list": student_list,'user':getuser(request),})
        return render_to_response('newpublish_student_all.html', c)
    except KeyError:
        return HttpResponseRedirect('/')

def historypublish_student(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        student_list = getuser(request).student.all()
        c = Context({"students_list": student_list, 'user':getuser(request),})
        if total(student_list):
            return render_to_response('historypublish_student.html', c)
        return render_to_response('historypublish_student.html')
    except KeyError:
        return HttpResponseRedirect('/')

def historyget_student(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        student_list = getuser(request).student.all()
        c = Context({"students_list": student_list,'user':getuser(request), })
        if total(student_list) > 0:
            return render_to_response('historyget_student.html', c)
        return render_to_response('historyget_student.html')
    except KeyError:
        return HttpResponseRedirect('/')

def praise_student(request):
    try:
        if request.session['user_id'] > 0:
            pass
        get = request.GET
        teacher_id = get['teacher_id']
        content_student_id = get['content_student_id']
        teacher = Teacher.objects.get(id=teacher_id)
        student_content = content_student.objects.get(id=content_student_id)
        c = Context({'teacher': teacher,'user':getuser(request),})
        if request.POST:
            post = request.POST
            student_content.star = post['star']
            student_content.evaluation = post['evaluation']
            student_content.save()
            return HttpResponseRedirect('/praise_one_student')
        return render_to_response('praise_student.html', c)
    except KeyError:
        return HttpResponseRedirect('/')

def praise_one_student(request):
    try:
        if request.session['user_id'] > 0:
            pass
        student_list = getuser(request).student.all()
        c = Context({"students_list": student_list, 'user':getuser(request),})
        if total(student_list):
            return render_to_response('praise_one_student.html', c)
        return render_to_response('praise_one_student.html')
    except KeyError:
        return HttpResponseRedirect('/')

def search_student(request):    #Done
    try:
        if request.session['user_id'] > 0:
            pass
        if request.POST:
            post = request.POST
            getperhour = post['getperhour']
            wenli = post['wenli']
            content_list = content_teacher.objects.all()
            temp_list = list()
            for content in content_list:
                if content.freestate == False:
                    if atoi(getperhour) > 0:
                        if content.getperhour == atoi(getperhour):
                            if wenli == 'True':
                                if content.wenli == True:
                                    temp_list.append(content)
                            elif wenli == 'False':
                                if content.wenli == False:
                                    temp_list.append(content)
                            else:
                                temp_list.append(content)
                    else:
                        if wenli == 'True':
                            if content.wenli == True:
                                temp_list.append(content)
                        elif wenli == 'False':
                            if content.wenli == False:
                                temp_list.append(content)
                        else:
                            temp_list.append(content)
            c = Context({"contents_list": temp_list,'user':getuser(request),})
            return render_to_response('search_student.html', c)
        return render_to_response('search_student.html',Context({'user':getuser(request),}))
    except KeyError:
        return HttpResponseRedirect('/')

def getorder_teacher(request):  #Done
    try:
        if request.session['user_id'] > 0:
            pass
        get = request.GET
        content_student_id = get['content_student_id']
        teacher_list = getuser(request).teacher
        c = Context({"teacher": teacher_list,'user':getuser(request),})
        if request.POST:
            post = request.POST
            teacher = content_teacher.objects.get(id=post['selection_id'])
            student = content_student.objects.get(id=content_student_id)

            teacher.content_stu.add(student)
            teacher.freestate = True
            teacher.save()

            student.freestate = True
            student.save()
            return HttpResponseRedirect('/historyget_teacher')
        return render_to_response('get_one_teacher.html', c)
    except KeyError:
        return HttpResponseRedirect('/')

def getorder_student(request):  #Done
    try:
        if request.session['user_id'] > 0:
            pass
        get = request.GET
        content_teacher_id = get['content_teacher_id']
        student_list = getuser(request).student.all()
        c = Context({"students_list": student_list,'user':getuser(request),})
        if request.POST:
            post = request.POST
            student = content_student.objects.get(id=post['selection_id'])
            teacher = content_teacher.objects.get(id=content_teacher_id)
            
            teacher.content_stu.add(student)
            teacher.freestate = True
            teacher.save()
            
            student.freestate = True
            student.save()
            return HttpResponseRedirect('/historyget_student')
        return render_to_response('get_one_student.html', c)
    except KeyError:
        return HttpResponseRedirect('/')

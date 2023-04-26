
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . models import Mentor,Student,Group
from .forms import  CreateMentorForm,CreateStudentForm,CreateUserForm
# Create your views here.

@login_required(login_url='login_user')
def testpage(request):
    return render(request,'mainapp/base.html')


def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('login_user')
    
    context = {
        'form':form,
    }
    return render(request,'mainapp/registrations.html',context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username') 
            password = request.POST.get('password') 

            user = authenticate(request, username=username, password=password) 

            if user is not None: 
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request, "Username or password was incorrect")
            
        context = {

        }

        return render(request, 'mainapp/login.html')

# @login_required(login_url='login_user') 
# def user_profile(request):

#     # profiles = UserProfile.all()
#     # context = {
#     #     'username':request.user,
#     #     'profiles':profiles
#     # }
#     return render(request,'mainapp/user_profile.html')

# @login_required(login_url='login_user') 
def logoutUser(request):
    logout(request)
    return redirect('login_user')




@login_required(login_url='login_user')
def dashboard(request):
    groups = Group.objects.all()
    mentors = Mentor.objects.all()
    students = Student.objects.all()
    contex = {
        'groups': groups,
        'mentors': mentors,
        'students':students,
    }
    
    return render(request,'mainapp/dashboard.html',contex)

# @login_required(login_url='login_user') 
# def grouptable(request):
#         groups = Group.objects.all()
#         contex = {
#             'groups': groups
#         }
#         return render(request,'mainapp/group.html',contex)

@login_required(login_url='login_user') 
def mentortable(request):
    if request.method == "POST":
        search_q = request.POST.get("m")
        mentors = Mentor.objects.filter(full_name__contains=search_q)
    else:
        mentors = Mentor.objects.all()
        contex = {
            'mentors': mentors
        }
        return render(request,'mainapp/mentor-table.html',contex)

@login_required(login_url='login_user') 
def createMentor(request):
    if request.user.is_superuser or request.user.is_staff:
        form = CreateMentorForm()
        if request.method == "POST":
            form = CreateMentorForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('mentor')
            else:
                form = CreateMentorForm()

        context = {
            'form':form
        }
        return render(request, 'mainapp/m_create.html', context)
    else:
        return redirect('mentor')

@login_required(login_url='login_user') 
def updateMentor(request,pk):
    if request.user.is_superuser or request.user.is_staff:
        mentor = Mentor.objects.get(id=pk)
        form = CreateMentorForm(instance=mentor)
        if request.method == "POST":
            form = CreateMentorForm(request.POST,instance = mentor)
            if form.is_valid():
                form.save()
                return redirect('mentor')

        context = {
            'form': form
        }

        return render(request, 'mainapp/m_create.html', context)

    else:
        return redirect('mentor')

@login_required(login_url='login_user') 
def deleteMentor(request,pk):
    if request.user.is_superuser:
        mentor = Mentor.objects.get(id=pk)
        if request.method == "POST":
            mentor.delete()
            return redirect('mentor')
        context = {
            'mentor':mentor
        }
        return render(request, 'mainapp/m_delete.html', context)
    else:
        return redirect('mentor')
    
        
@login_required(login_url='login_user') 
def student_table(request):
    students = Student.objects.all()
    contex = {
        'students': students
    }
    return render(request,'mainapp/student-table.html',contex)


@login_required(login_url='login_user') 
def CreateStudent(request):
    if request.user.is_superuser or request.user.is_staff:
        form = CreateMentorForm()
        if request.method == "POST":
            form = CreateStudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student_table')
            else:
                form = CreateStudentForm()

        context = {
            'form':form
        }
        return render(request, 'mainapp/s_create.html', context)
    else:
        return redirect('student_table')

@login_required(login_url='login_user') 
def updateStudent(request,pk):
    if request.user.is_superuser or request.user.is_staff:
        student = Student.objects.get(id=pk)
        form = CreateStudentForm(instance=student)
        if request.method == "POST":
            form = CreateStudentForm(request.POST,instance = student)
            if form.is_valid():
                form.save()
                return redirect('student_table')

        context = {
            'form': form
        }

        return render(request, 'mainapp/s_create.html', context)
    else:
        return redirect('student_table')

@login_required(login_url='login_user') 
def deleteStudent(request,pk):
    if request.user.is_superuser:
        student = Student.objects.get(id=pk)
        if request.method == "POST":
            student.delete()
            return redirect('student_table')
        context = {
            'student':student
        }
        return render(request, 'mainapp/s_delete.html', context)
    else:
        return redirect('student_table')


@login_required(login_url='login_user') 
def error_500(request):
    return render(request,'mainapp/samples/error-500.html')

@login_required(login_url='login_user') 
def error_404(request):
    return render(request,'mainapp/samples/error-404.html')


# def mainPage(request):
#     return render(request,'mainapp/forms/basic_elements.html')


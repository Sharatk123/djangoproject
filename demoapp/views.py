from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from .models import Employee,Book,Student
from .forms import StudentForm,BookForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
import csv

# Create your views here.

def home(request):
    if request.method=='POST' and request.FILES['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        url=fs.url(myfile)
        print('save')
    # dictionary code
    #dic = {'name': 'Django', 'id': 105}
    return render(request,'index.html')

def test(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print('saved')
        else:
            form=StudentForm()
    else:
        form=StudentForm()
            
    return render(request,'test.html',{'form':form})

def contact(request):
    if request.method== "POST":
        uname=request.POST['ename']
        uemail=request.POST['Email']

        con=Employee(name=uname,email=uemail)
        con.save()
        print('save sucessfully')
    records=Employee.objects.all()
    d={'records':records}
    return render(request,'contact.html',d)

def add(request):
    a=int(request.POST['num1'])
    b=int(request.POST['num2'])

    c=a+b
    return render(request,'result.html',{'sum':c})


def upload_book(request):
    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid:
            form.save()
            print('save')
            return redirect('book_list')
    else:
        form=BookForm()
    return render(request,'upload_book.html',{'book':form})

def book_list(request):
    b=Book.objects.all()
    return render(request,'book_list.html',{'book':b})


def delete_book(request,pk):
    if request.method=="POST":
        book=Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


def send_email(request):
    if request.method=="POST":
        message=request.POST['message']
        send_mail('testing',message,settings.EMAIL_HOST_USER,['sarathkettavan407@gmail.com'],fail_silently=False)

    return render(request,'send_email.html')



def ssession(request):
    request.session['sname']='Sharat'
    request.session['email']='sarath@gmail.com'
    return HttpResponse("Session are set")

def gsession(request):
    s=request.session['sname']
    e=request.session['email']
    return HttpResponse(s)

def scookies(request):
    response=HttpResponse("cookies are set")
    response.set_cookie("key","sharatkumar")
    return response

def gcookies(request):
    name=request.COOKIES['key']
    return HttpResponse(name)


def csvs(request):
    response=HttpResponse(content_type='text/csv')
    response['content-Disposition']='attachment; filename="sharat.csv"'
    st=Student.objects.all()
    writer=csv.writer(response)
    for s in st:
        writer.writerow([s.name,s.email,s.mobile])
    return response



    #return HttpResponse("<h1 align='center'><font color= 'blue' face='algerian'> Welcome To Django</font></h1>")
    #return HttpResponse("<script>alert('Welcome Python Developer');</script>")
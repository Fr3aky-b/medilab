from django.shortcuts import render, redirect


from medapp.models import *
# Create your views here.
def home(request):
  return render(request,'index.html')

def starter(request):
  return render(request,'starter-page.html')

def about(request):
  return render(request,'about.html')

def service(request):
  return render(request,'services.html')

def dep(request):
  return render(request,'departments.html')


def doc(request):
  return render(request,'doctors.html')

def appointment(request):
  if request.method=='POST':
    myappointment=Appointment(
      name=request.POST['name'],
      email=request.POST['email'],
      message=request.POST['message'],
      subject=request.POST['subject']
    )


    myappointment.save()
    return redirect('/appointment')
  else:
    return render(request,'appointments.html')

def contact(request):
  return render(request,'contact.html')








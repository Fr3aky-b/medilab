from django.shortcuts import render, redirect,get_object_or_404


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
    myappointment=Appointment1(
      name=request.POST['name'],
      email=request.POST['email'],
      subject=request.POST['subject'],
      message=request.POST['message']

    )


    myappointment.save()
    return redirect('/show')
  else:
    return render(request,'appointments.html')

def contact(request):
  return render(request,'contact.html')










def show(request):
  all=Appointment1.objects.all()
  return render(request,'Show.html',{'all':all})

def delete(request,id):
  deleteappointment=Appointment1.objects.get(id=id)
  deleteappointment.delete()
  return redirect('/show')

def edit(request,id):
  appointment=get_object_or_404(Appointment1,id=id)
  if request.method=='POST':
    appointment.name=request.POST.get('name')
    appointment.email=request.POST.get('email')
    appointment.subject=request.POST.get('subject')
    appointment.message=request.POST.get('message')
    appointment.save()
    return redirect('/show')
  else:
    return render(request,'edit.html',{'appointment':appointment})

#register
def register(request):
  return render(request,'register.html')

#login
def login_view(request):
  return render(request,'login.html')







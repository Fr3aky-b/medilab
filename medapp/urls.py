
from django.contrib import admin
from django.urls import path
from medapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home,name='home'),
    path('starter',views.starter,name='starter'),
    path('about',views.about,name='about'),
    path('services',views.service,name='services'),
    path('department',views.dep,name='department'),
    path('doctors',views.doc,name='doctors'),
    path('appointment',views.appointment,name='appointment'),
    path('contact',views.contact,name='contact'),
    path('show',views.show,name='show'),
    path('',views.register,name='register'),
    path('login',views.login_view,name='login'),



    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit,name='edit'),

    #mpesa API

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),

]



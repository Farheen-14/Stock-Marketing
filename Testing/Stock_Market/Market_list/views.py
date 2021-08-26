from django.http.response import HttpResponse
from pandas.core.indexes.base import Index
from Market_list.models import stock_items
from django.contrib.auth.models import User,auth
from django.http import request
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import stock_items,enquiry

# email sending
from django.conf import settings
from django.core.mail import send_mail

# need to work onbelow for excel
import numpy as np
import pandas as pd

# Create your views here.

def download(request):
    stok = stock_items.objects.filter(user=request.user).values()
    df = pd.DataFrame(data=stok)
    xlwriterDF = pd.ExcelWriter('stock.xlsx')
    df.to_excel(
        excel_writer=xlwriterDF,
        sheet_name='stock',
        na_rep='Missing',
        columns=['title','description','video_url'],
        index=False,
        index_label=['Row 1'],
        header=True,
        startrow=0,
        startcol=0,
        freeze_panes= (1,4) 
    )
    xlwriterDF.close()
    print("process closed")
    messages.info(request,'Data Successfully Downloaded In Your Folder')
    return render(request,'upload_items.html')


def navbar(request):
    return render(request,'navbar.html')

def search(request):
    search_query = request.GET['query'] #what we want to search 
    if len(search_query)>78:
        data = stock_items.objects.none()
    else:
        datatitle = stock_items.objects.filter(user=request.user,title__icontains=search_query)
        datadescription = stock_items.objects.filter(user=request.user,description__icontains=search_query)
        data = datatitle.union(datadescription)
    if data.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params = {'data' : data, 'query': search_query}
    return render(request,'search.html',params)

def home(request):
    return render(request,'home.html')

def stock(request):
    data = stock_items.objects.filter(user=request.user)
    return render(request,'stock.html',{"message":data})

def upload_items(request):
    data = stock_items.objects.filter(user=request.user)
    if request.method == 'POST':
        ttl = request.POST['title']
        desc = request.POST['description']
        vdourl = request.POST['video_url']
        entry = stock_items(user=request.user,title=ttl, description=desc,video_url=vdourl)
        entry.save(); 
        print("data saved in database")
        messages.success(request,'Uploaded Successfully, Go-To Stock-Items')
        return render(request,'upload_items.html')
    return render(request,'upload_items.html')

def signin(request):
    if request.method=='POST':
        user_name=request.POST['username']
        pass_word = request.POST['password']
        user=auth.authenticate(username=user_name, password=pass_word)
        if user is not None:
            auth.login(request,user)
            print("User authenticated")
            return redirect('stock')
        else:
            messages.warning(request,"Invalid Username or password! Please try again.")
            return redirect('signin')
    else:
        return render(request,'signin.html')

def signup(request):
    if request.method == 'POST':
        usrr = request.POST['username']
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        emid = request.POST['email']
        pwd = request.POST['password']
        user = User.objects.create_user(username=usrr, first_name=fname, last_name=lname, email=emid, password=pwd) #to be continue..
        user.save(); 
        messages.success(request,'User Created, Please LogIn')
        return redirect('signin')
    return render(request,'signup.html')

def query(request):
    enqry = enquiry.objects.all()
    if request.method == 'POST': 
        user_name = request.POST['name']
        user_mail = request.POST['email']
        user_number = request.POST['contact']
        user_msg = request.POST['message']
        enq = enquiry(name=user_name,email=user_mail, contact= user_number,message=user_msg)
        enq.save()
        # the below code for email sending
        subject = 'Enquiry from Stock-Marketing'
        message = f'Hi Admin,\n{enq.message} from {enq.email}.\n{enq.name}\nMobile : {enq.contact}.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail( subject, message, email_from, recipient_list)
        messages.success(request,'Successfully! Enquiry Sent To The Admin...')
        return render(request,'query.html',{"message": enqry}) 
    return render(request,'query.html')


def logout(request): 
    auth.logout(request)
    messages.success(request,'Successfully logout..you want to login again?')
    return redirect('signin')


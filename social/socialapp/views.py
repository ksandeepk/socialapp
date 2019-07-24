from django.shortcuts import render
from django.http import HttpResponse
from .forms import create
from .models import udata
from django.db.models import Q
from django.core.mail import send_mail
name=''
email=''

# Create your views here.
def reg(request):
    form=create()
    if request.method=='POST':
        global email
        form=create(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            status=form.cleaned_data['status']
            gender=form.cleaned_data['gender']
            marital_status=form.cleaned_data['marital_status']
            interest_in=form.cleaned_data['interest_in']
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            address=form.cleaned_data['address']
            profile_picture=request.POST['pic']
            cp=udata(name=name,status=status,gender=gender,marital_status=marital_status,
                    interest_in=interest_in,email=email,username=username,password=password,
                    address=address,profile_picture=profile_picture)
            cp.save()
            form=create()
            #send_mail('hello',"registration sucess",'ksandeepk94@gmail.com',['email'],fail_silently=False) 
            return render(request,'reg.html',{'form':form})
    return render(request, 'reg.html',{'form':form})        

def log(request):
    if request.method=='POST':
        username=request.POST['uname']
        password=request.POST['pwd']
        lp=udata.objects.get(username=username,password=password)
        if lp:
            return render(request,'friends.html',{'name':lp.name,'status':lp.status,'gender':lp.gender,'marital_status':lp.marital_status,
                        'interest_in':lp.interest_in,'email':lp.email,'address':lp.address,'profile_picture':lp.profile_picture})
        else:
            return HttpResponse('login faild') 
    return render(request,'login.html')

def fnds(request):
    return render(request,'friends.html')

def findf(request):
    if request.method=='POST':
        global name
        name=request.POST['name']
        user=udata.objects.get(name=name)
        if user:
            return render(request,'findl.html',{'name':user.name,})
        else:
            return HttpResponse('no user')
    return render(request,'find.html') 

def prf(request):
    fp=udata.objects.get(name=name)
    return render(request,'profile.html',{'name':fp.name,'status':fp.status,'gender':fp.gender,'marital_status':fp.marital_status,
                        'interest_in':fp.interest_in,'email':fp.email,'address':fp.address,'profile_picture':fp.profile_picture})
    

def req(request):
    return HttpResponse('friend request sent sucessfully')


def flist(request):
    data=udata.objects.filter()
    return render(request,'flist.html',{'data':data})

def frqst(user):
    data= udata.objects.requests(user)
    return render(request,'frqs.html')
       


        


 
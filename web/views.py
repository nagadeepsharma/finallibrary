from django.shortcuts import render
from .models import Memo,All
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .forms import Toorder
from .models import Cart
from .models import Cse,Mech,Civil,Ece,Eee
from django.core.mail import send_mail
from django.utils import timezone

# Create your views here.




# Create your views here.
def index(request):
    if request.method=='POST':
        user=authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'web/index.html',{'form':AuthenticationForm(),'error':'invalid-credentials'})


    else:
        return render(request,'web/index.html',{'form':AuthenticationForm()})
def createuser(request):
    
    import random
    a=[0,1,2,3,4,5,7,8,9]
    otp=''
    for i in range(0,6):
        otp+=str(random.choice(a))
    global finalotp
    global finaluser
    finalotp=otp

    


    if request.method=='POST':
        email=request.POST['email']
        if request.POST['password1']==request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'],password=request.POST['password2'])
                finaluser=user
                send_mail('Your Otp is:',otp,'nagadeep.33@gmail.com',[email],fail_silently=False)
                return redirect('conformation')
            except IntegrityError:
                return render(request,'web/signup.html',{'form':UserCreationForm(),'error':'Username already taken!'})
        

        else:
            return render(request,'web/signup.html',{'form':UserCreationForm(),'error':'passwords did not match!'})

    else:
        form=UserCreationForm()
        return render(request,'web/signup.html',{'form':form})
def conformation(request):
    if request.method=='POST':
        otp1=request.POST['otp']
        if otp1==finalotp:
            
            
            finaluser.save()
            login(request,finaluser)
            return redirect('home')
        else:
            return render(request,'web/conformation.html',{'error':'Otp  Incorrect'})
    else:
        return render(request,'web/conformation.html')
    
        
@login_required(login_url='web/index.html')
def home(request):
    memo=Memo.objects.all()
    al=All.objects.all()
    return render(request,'web/home.html',{'memo':memo,'al':al })
@login_required(login_url='web/index.html')
def cse(request):
    form=Cse.objects.all()
    return render(request,'web/cse.html',{'form':form})
def logoutuser(request):
    if request.method=="POST":
        pass  
    logout(request)
    return redirect('index')
@login_required(login_url='web/index.html')
def abt(request):
    return render(request,"myuser/abt.html")

@login_required(login_url='web/index.html')
def cart(request):
    if request.method=='POST':
        bb=request.POST['branch']
        if bb=='Cse':
            data=get_object_or_404(Cse,pk=request.POST['bookid'])
        if bb=='Ece':
            data=get_object_or_404(Ece,pk=request.POST['bookid'])
        if bb=='Eee':
            data=get_object_or_404(Eee,pk=request.POST['bookid'])
        if bb=='Civil':
            data=get_object_or_404(Civil,pk=request.POST['bookid'])
        if bb=='Mech':
            data=get_object_or_404(Mech,pk=request.POST['bookid'])

        newcart=Cart(name=data.name,bookid=data.id,img=data.img,clgid=request.POST['clgid'])

        newcart.user=request.user
        newcart.save()
        return redirect('home')
        

    else:

        return render(request,'web/cart.html',{'form':Toorder()})
@login_required(login_url='web/index.html')
def ece(request):
    form=Ece.objects.all()
    return render(request,'web/ece.html',{'form':form})
@login_required(login_url='web/index.html')
def civil(request):
    form=Civil.objects.all()
    return render(request,'web/civil.html',{'form':form})
@login_required(login_url='web/index.html')
def eee(request):
    form=Eee.objects.all()
    return render(request,'web/eee.html',{'form':form})
@login_required(login_url='web/index.html')
def mech(request):
    form=Mech.objects.all()
    return render(request,'web/mech.html',{'form':form})
@login_required(login_url='web/index.html')
def mycart(request):
    new=Cart.objects.filter(user=request.user,datecompleted__isnull=True)
    return render(request,'web/mycart.html',{'data':new})
@login_required(login_url='web/index.html')
def returned(request,my_id):
    su=get_object_or_404(Cart,user=request.user,pk=my_id)
    su.datecompleted=timezone.now()
    su.save()
    return redirect('home')
@login_required(login_url='web/index.html')
def delete(request,my_id):
    su=get_object_or_404(Cart,user=request.user,pk=my_id)
    su.delete()
    return redirect('home')
@login_required(login_url='web/index.html')
def past(request):
    new=Cart.objects.filter(user=request.user,datecompleted__isnull=False)
    return render(request,'web/returned.html',{'data':new})




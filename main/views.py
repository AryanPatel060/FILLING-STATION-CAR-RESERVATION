from django.shortcuts import render,HttpResponse,redirect
import main.models as model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout



def index(request):
    if request.user.is_anonymous:
        return redirect("loginuser")
    fuelstationdata= model.Fuelstations.objects.all()
    data = {
        'fuelstationdata':fuelstationdata
    }

    return render(request,'index.html',data)

def loginuser(request):
       if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.get(email=email).username
        user_id = User.objects.get(email=email).id
        data = {
            'username':username,
            'eamil':email,
            'user_id':user_id,
        }
        request.session['userdata'] = data
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return redirect('signupuser')
        
       if request.user.is_authenticated:
           return redirect("index")
       return render(request,'loginuser.html')


def signupuser(request):
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword =request.POST.get('cpassword')
        username = request.POST.get('uname')
        # user = authenticate(email = email,password =password)
        if password == cpassword:
            user = User.objects.create_user(username, email, password)
            message ='signup successfully'
            return redirect('loginuser')

        else:
            message='Passwords do not match'
            return redirect('signupuser')
    if request.user.is_authenticated:
        return redirect("index")
    return render(request,'signupuser.html')

def logoutuser(request):
    logout(request)
    return redirect('loginuser')


def bookslot(request,station_id):
    Tdata= model.Fuelstations.objects.get(id=station_id)    
    slotdata = model.Bookedslot.objects.filter(Fuelstations_id= station_id)
    list = {}
    for x in range(12):
        list[x+1]='success'

    for x in slotdata:
        print(x.slot_number)
        list[x.slot_number]="danger"
    print(list) 
    data = {
        'fuelstationdata':Tdata,
        'slotlist':list,
    }
    return render(request,'bookslot.html',data)
        
def slotbook(request):
    if request.method == "POST":
        slot_number = request.POST.get('slotnumber') 
        Fuelstation_id = request.POST.get('fuelstationid')
        contactno = request.POST.get('contactno')      
        username = request.POST.get('uname')      
        email = request.POST.get('email')    
        # user_id = request.session['userdata'].user_id
        date='2023-08-14'
        user_id=request.user.id

        data=model.Bookedslot(slot_number=slot_number,Fuelstations_id=Fuelstation_id,user_id=user_id,date=date)
        data.save()
        # print(slot_number)
        
        fsdata=model.Fuelstations.objects.get(id=Fuelstation_id)
        
        data={
          'fsdata' : fsdata,
          'slotnumber':slot_number,
          'name':username,
          'eamil':email,
          'contactno':contactno,
        }
        
    return render(request,'slotreciepe.html',data)

def profile(request):
    return render(request,'profile.html')

def slotrecipe(request):
    return render(request,'slotreciepe.html')
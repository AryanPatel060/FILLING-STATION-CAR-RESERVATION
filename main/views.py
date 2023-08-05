from django.shortcuts import render,HttpResponse,redirect
import main.models as model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from datetime import date
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 
from django.template.loader import render_to_string


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
    today = date.today()
    slotdata = model.Bookedslot.objects.filter(Fuelstations_id= station_id,date=today)
    list = {}
    for x in range(12):
        list[x+1]='success'

    for x in slotdata:
        print(x.slot_number)
        list[x.slot_number]="danger"

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
        user_id=request.user.id
        today=date.today()
        data=model.Bookedslot(slot_number=slot_number,Fuelstations_id=Fuelstation_id,user_id=user_id,date=today)
        data.save()
        # print(slot_number)
        
        fsdata=model.Fuelstations.objects.get(id=Fuelstation_id)
        global dataofpdf
        dataofpdf={
          'fsdata' : fsdata,
          'slotnumber':slot_number,
          'name':username,
          'email':email,
          'contactno':contactno,
          'date':today,
        }
        # open('temp.html', "w").write(render_to_string('slotreciepe.html',dataofpdf))
        # # getting the template
        # pdf = html_to_pdf('temp.html',dataofpdf)
         
        #  # rendering the template
        # return HttpResponse(pdf, content_type='application/pdf')
    return render(request,'slotreciepe.html',dataofpdf)

def profile(request):
    return render(request,'profile.html')

def slotrecipe(request):
    return render(request,'slotreciepe.html')






# below class is use for making pdf of slip of slot booking

#Creating a class based view
class GeneratePdf(View):
     
     def get(self, request, *args, **kwargs):
        # data = model.Bookedslot.objects.all()
        global dataofpdf
        print(dataofpdf)
        open('temp.html', "w").write(render_to_string('slotreciepe.html',dataofpdf))
        # getting the template
        pdf = html_to_pdf('temp.html',dataofpdf)
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
from django.contrib import admin
from main.models import User,Fuelstations,Bookedslot
# Register your models here.
class Mainadmin(admin.ModelAdmin):
    list_display = ('name', 'email','password')

class Fuelstationadmin(admin.ModelAdmin):
    list_display =('station_name','city','state')

class SlotAdmin(admin.ModelAdmin):
    list_display=('Fuelstations_id','user_id','slot_number','date')

admin.site.register(User,Mainadmin)    
admin.site.register(Fuelstations,Fuelstationadmin)
admin.site.register(Bookedslot,SlotAdmin)

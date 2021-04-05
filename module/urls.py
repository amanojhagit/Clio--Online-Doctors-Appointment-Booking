from django.urls import path
from . import views

urlpatterns = [
    #------------ PATIENT URLS-----------------------
    path('patient/',views.patients),
    path('patient/book',views.book),
    path('patient/timeslot/<int:id>',views.timeslot),


    #---------------DOCTOR URLS ---------------
    path('doctor',views.doctors),
    path('schedule',views.docSchedule),
    path('addSchedule/<int:id>',views.addSchedule),
    path('updateSchedule/<int:id>',views.updateSchedule),




    #------------RECEPTIONIST URLS-----------------
    path('receptionist',views.receptionist)
]
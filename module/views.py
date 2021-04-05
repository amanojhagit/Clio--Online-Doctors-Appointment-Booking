from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import * 
import datetime as dt
# Create your views here.




def patients(request):
    return render(request,'patientDashboard.html')

def book(request):
    if request.method == 'POST':
        a = request.POST['email']
        gender = request.POST['gender']
        slot_date = request.POST['date']
        doctor_name=request.POST['doc_name']
        request.session['doctor_name']=doctor_name
        request.session['slot_date']=slot_date
        datetimeobject= datetime.strptime(slot_date,'%d-%m-%Y')
        slot_date = datetimeobject.strftime('%Y-%m-%d')
        c_date = dt.datetime.now().strftime('%d-%m-%Y')
        c_date= datetime.strptime(c_date,'%d-%m-%Y')
        now = datetime.now()

        if gender in ['m','f','M','F'] and datetimeobject>=c_date:
            slot_date = datetimeobject.strftime('%Y-%m-%d')
            c_date = dt.datetime.now().strftime('%Y-%m-%d')
            db=appointments(
                doctor=doctor.objects.get(name=doctor_name),
                patient = patient.objects.get(email=a),
                slot_date=slot_date,
                createdAt=c_date,
                updatedAt=c_date,
                status="pending")
            print("migration")
            db.save()
            print("db saved")
                
            return redirect("timeslot/50",{'doc':doctor_name})
                        #counter=0

            #send_mail=(subject,message,from_email,to_list,fail_silently=True)
        else:
            docs= doctor.objects.all()   
            print(docs) 
            messages.info(request , "invalid credentials")
            return render(request,'booking.html' , {'docs':docs})
      
    else:   
        docs= doctor.objects.all()   
        print(docs)  
        return render(request,'booking.html', {'docs' : docs})

#  def timeslot(request,id):
#     print(id)
#     docs = request.session.get('doctor_name')
#     da = request.session.get('slot_date')
#     id1 = request.session.get('patient_appointment_id')
#     print("id1",id1)
#     datetimeobject= datetime.strptime(da,'%d-%m-%Y')
#     da = datetimeobject.strftime('%Y-%m-%d')

#     apptime = DaySchedule.objects.filter(doctor_name=docs)
#     doc = doctors.objects.filter(name=docs)
#     for i in doc:
#         x = i.id
#     time1 = dt.time(11,00,00)
#     time = dt.time(2,00,00)
#     time.strftime("%H-%M-%S")
#     u = request.user.username
#     print("u",u)
#     print("ferg",appointments.objects.filter(doctor_id=x,slot_date=da,slot_time=time1))
#     if id:
#         if id==1:
#             time = dt.time(9,1,00)
#             time = time.strftime("%H:%M:%S")
#             print(time)
#             print(time,type(time))
#             if appointments.objects.filter(doctor_id=x,slot_date=da,slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 print("user",u)
#                 if patient.objects.filter(patinet_id=u):
#                     return redirect('/patient')
#                 elif receptionist.objects.filter(recep_id=u):
#                     return redirect('/receptionist')
#                 else:
#                     return redirect('/')
#         elif id==2:
#             time = dt.time(9, 15, 00)
#             time.strftime("%H-%M-%S")
#             print(time)
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u):
#                     return redirect('/patient')
                    
#                 else:
#                    return redirect('/receptionist')
#         elif id==3:
#             time = dt.time(9,30,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 print("entry Done")
#                 if patient.objects.filter(patient_id=u):
#                     return redirect('/patient')
#                 else:
#                     return redirect('/receptionist')
#         elif id==4:
#             time = dt.time(9,45,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==5:
#             time = dt.time(10,00,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==6:
#             time = dt.time(10,15,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==7:
#             time = dt.time(10,30,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da,slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==8:
#             time = dt.time(10,45,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==9:
#             time = dt.time(11,00,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da,slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==10:
#             time = dt.time(11,15,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==11:
#             time = dt.time(11,30,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da,slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==12:
#             time = dt.time(11,45,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==13:
#             time = dt.time(13,30,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==14:
#             time = dt.time(13,45,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==15:
#             time = dt.time(14,00,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==16:
#             time = dt.time(14,15,00)
#             time.strftime("%H-%M-%S")
#             print(time)

#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==17:
#             time = dt.time(14,30,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==18:
#             time = dt.time(14,45,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id == 19:
#             time = dt.time(15,00,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 print("if")
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 print("esle")
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==20:
#             time = dt.time(15,15,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==21:
#             time = dt.time(15,30,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==22:
#             time = dt.time(15,45,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==23:
#             time = dt.time(17,00,00)
#             time.strftime("%H-%M-%S")
#             print("time",time)
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==24:
#             time = dt.time(17,15,00)
#             time.strftime("%H-%M-%S")
#             print(time)
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id ==25:
#             time = dt.time(17,30,00)
#             time.strftime("%H-%M-%S")
#             print(time)
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==26:
#             time = dt.time(17,45,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==27:
#             time = dt.time(18,00,00)
#             time.strftime("%H-%M-%S")
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==28:
#             time = dt.time(19,15,00)
#             time.strftime("%H-%M-%S")
#             time = time.strftime("%H-%M-%S")
#             print(time)
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         elif id==29:
#             time = dt.time(19,30,00)
#             time.strftime("%H-%M-%S")
#             print(time)
#             if appointments.objects.filter(doctor_id=x,slot_date=da , slot_time=time).exists():
#                 messages.info(request,'time is already taken')
#                 return redirect("/patient/timeslot/50")
#             else:
#                 appointments.objects.filter(patient_appointment_id = id1).update(slot_time=time,status="pending")
#                 if patient.objects.filter(patient_id=u).exists():
#                     return redirect('/patient')
             
#                 else:
#                     return redirect('/receptionist')
#         else:
#             return render(request,'timeslot.html')

def docSchedule(request):
    # add option for day+ date to check in DB  
    docs = timeslot.objects.filter(doctor=doctor.objects.get(email=request.user)) 
    return render(request,'schedule.html',{'apps':docs})
def addSchedule(request,id):
    # write code for adding schedule to the DB
    '''
    steps:
        step 1: extract time-ID input from the front end
        step 2: create a datetime object of the start time and end time specified by the time-ID
        step 3 : Add the data object into the Database according to the schema.
        step 4 : redirect to "/module/doctor/schedule".
    '''
    time = timeslotGeneral.objects.get(id = id)    
    obj = timeslotDetails(
        doctor = request.user,
        timeslot = time,
        isActive=True
    )
    obj.save()
    return redirect('/module/doctor/schedule')
    

def updateSchedule(request,id):
    #write code for updating existing Schedule in the DB
    '''
    steps:
        step 1: extract data-ID from the URL
        step 2: query in DB for the exact data with the id extracted above
        step 3 : once data is fetched, use the "update()" model function of django to update data(Turn isActive Field to False) into the DB.
        step 4 : redirect to  "/module/doctor/schedule" with Updatation successfull Messsage. 
    '''
    timeslot.objects.filter(id=id).update(isActive=False)
    off=doctor.objects.filter(email=request.user)
    return redirect('/module/schedule',{'apps':off})


def doctors(request):
    return render(request,'doctorDashboard.html')
def receptionist(request):
    return render(request,'receptionistDashboard.html')
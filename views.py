
from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as mylogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from math import *
from .forms import ImageForm

# Create your views here.


def login(request):

    if request.user.is_authenticated:
        return redirect('Page_Accueil.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                mylogin(request, user)
                return redirect('Page_Accueil.html')
            else:
                messages.error(request, 'Username OR password is incorrect')

    return render(request, 'eyecollect/login.html')


def updatepat(request):

    if request.method == 'POST':
        CIN = request.POST.get('CIN')
        nom = request.POST.get('nom')
        prenom = request.POST.get('Prenom')
        dateNaissance = request.POST.get('Date')
        genre = request.POST.get('Genre')
        situationFamiliale = request.POST.get('situ_faml')
        poids = request.POST.get('Poids')
        taille = request.POST.get('Taille')
        type_diabete = request.POST.get('Type_db')

        pat = Patient.objects.get(nom=nom, prenom=prenom)
        pat.CIN = CIN
        pat.nom = nom
        pat.prenom = prenom
        pat.dateNaissance = dateNaissance
        pat.genre = genre
        pat.situationFamiliale = situationFamiliale
        pat.poids = poids
        pat.taille = taille
        pat.type_diabete = type_diabete
        pat.save()
        return redirect('Patient.html')

    return render(request, "eyecollect/Patient.html")


def editpat(request, nom, prenom):
    pat = Patient.objects.filter(nom=nom, prenom=prenom)
    context = {
        'pat': pat
    }
    return render(request, "eyecollect/editpat.html", context)


def userlogout(request):
    logout(request)
    return redirect('login.html')


def password_reset(request):
    return redirect('password_reset/')


@login_required(login_url='login.html')
def patient(request):
    if 'CIN_S' in request.POST:
        search = request.POST.get('CIN_S')
        displaypatients = Patient.objects.filter(CIN__startswith=search)
    else:
        displaypatients = Patient.objects.all()
    return render(request, "eyecollect/Patient.html", {"displaypatients": displaypatients})


@login_required(login_url='login.html')
def accueil(request):

    if request.method == 'POST' :
        
            
        CIN = request.POST.get('CIN')
        
        if Patient.objects.filter(CIN=CIN).exists():
                    pat = Patient.objects.get(CIN=CIN)
                    
                    form = ImageForm(request.POST, request.FILES)
                    if form.is_valid():
                        form.save()
                        # Get the current instance object to display in the template
                        img_obj = form.instance
                    
                    type_cons = "Control"
                    region = Region.objects.get(region="Oriental")
                    ville = Ville.objects.get(region=region)
                    etab = Etablissement_sante.objects.get(ville=ville)
                    medecin = Medecin.objects.get(nom=request.user.first_name,
                                    prenom=request.user.last_name, etablissement_sante=etab)
                
                    consultation = Consultations(
                        patient=pat, oeil=img_obj, medecin=medecin, type_consultation=type_cons)
                    consultation.save()
                    return redirect ('Consultation.html')
        else:
            
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    # Get the current instance object to display in the template
                    img_obj = form.instance
                
                type_cons = "Première visite"
                nom = request.POST.get('nom')
                prenom = request.POST.get('Prenom')
                dateNaissance = request.POST.get('Date')
                genre = request.POST.get('Genre')
                situationFamiliale = request.POST.get('situ_faml')
                poids = request.POST.get('Poids')
                taille = request.POST.get('Taille')
                type_diabete = request.POST.get('Type_db')

                patient = Patient(CIN=CIN, nom=nom, prenom=prenom, dateNaissance=dateNaissance, genre=genre,
                                situationFamiliale=situationFamiliale, poids=poids, taille=taille, type_diabete=type_diabete)
                patient.save()
                
                region = Region.objects.get(region="Oriental")
                ville = Ville.objects.get(ville="Oujda")
                etab = Etablissement_sante.objects.get(ville=ville)
                medecin = Medecin.objects.get(nom=request.user.first_name,
                                    prenom=request.user.lasst_name, etablissement_sante=etab)
                
                consultation = Consultations(
                    patient=patient, oeil=img_obj, medecin=medecin, type_consultation=type_cons)
                consultation.save()
                return redirect('Consultation.html')

    return render(request, "eyecollect/Page_Accueil.html")


@login_required(login_url='login.html')
def consultation(request):
   
        if request.method=='POST':
            fromdate=request.POST.get('fromdate')
            todate=request.POST.get('todate')
            displayconsultations=Consultations.objects.filter(date__range=(fromdate, todate))
            return render(request,"eyecollect/Consultation.html" ,{"displayconsultations": displayconsultations.order_by('-date')})
        else :
            
            displayconsultations = Consultations.objects.all()
    
        return render(request, "eyecollect/Consultation.html", {"displayconsultations": displayconsultations.order_by('-date')})
    
    

def showpat(request, nom, prenom):
    pat = Patient.objects.filter(nom=nom, prenom=prenom)
    context = {
        'pat': pat,

    }
    return render(request, "eyecollect/showpat.html", context)


def showcons(request, nom,prenom,date):

        pat = Patient.objects.get(nom=nom,prenom=prenom)
    
        con = Consultations.objects.filter(patient_id=pat.CIN,date=date)
        
        if len(con) > 1:
            for con in con:
                con = Consultations.objects.get(id=con.id)
                context = {
                            'con': con
                        }
        else:
            for con in con:
                context = {
                            'con': con
                        }
        
        
        return render(request, "eyecollect/showcons.html", context)

def editconsultation(request, nom,prenom,date):
    
        pat = Patient.objects.get(nom=nom,prenom=prenom)
        
        con = Consultations.objects.filter(patient_id=pat.CIN,date=date)
            
        if len(con) > 1:
                for con in con:
                    con = Consultations.objects.get(id=con.id)
                    context = {
                                'con': con
                            }
        else:
                for con in con:
                    context = {
                                'con': con
                            }
            
            
        return render(request, "eyecollect/editcons.html", context)


def updatecons(request):
    
    if request.method == 'POST':
        date = request.POST.get('Date')
        #CIN = request.POST.get('CIN')
        desc = request.POST.get('Description')
                
        con = Consultations.objects.get(date=date)
        
        con.description = desc
        con.save()
        return redirect('Consultation.html')

    return render(request, "eyecollect/Consultation.html")

def showdates(request,nom,prenom):
    pat = Patient.objects.get(nom=nom,prenom=prenom)
    
    con = Consultations.objects.filter(patient_id=pat.CIN)
    for con in con:
        cont = Consultations.objects.get(id=con.id)
        context = {
                'cont': cont
            }
    return render(request, "eyecollect/showdates.html", context)





def showimg(request, nom,prenom):
    pat = Patient.objects.get(nom=nom,prenom=prenom)
    
    con = Consultations.objects.filter(patient_id=pat.CIN)
    
            
    context = {
                        'con': con
                    }
    
    return render(request, "eyecollect/showimg.html", context)


def editcons(request, nom):
    return render(request, "eyecollect/showcons.html", context)







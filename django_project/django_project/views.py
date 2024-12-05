from django.shortcuts import redirect, render
from .forms import EmprunterForm
from .forms import JeuDePlateauForm
from .forms import LivreForm
from .forms import CdForm
from .forms import DvdForm
from .models import Emprunter
from .models import JeuDePlateau
from .models import Media
from .models import Livre
from .models import Cd
from .models import Dvd
from django.db.models import Count
from django.db.models import BooleanField, ExpressionWrapper, Q
from django.utils import timezone
from django.db.models import (OuterRef, Subquery)

def showView(request):
    EmprunterObj = Emprunter.objects.all()
    LivreObj = Livre.objects.all()
    CdObj = Cd.objects.all()
    DvdObj = Dvd.objects.all()
    GameObj = JeuDePlateau.objects.all()
    EmprunterObj = Emprunter.objects.annotate(nb_Emprunt=Count("emprunter"))
    LivreObj = Livre.objects.annotate(nb_EmpruntLivre=Count("emprunter_id"))
    CdObj = Cd.objects.annotate(nb_EmpruntCd=Count("emprunter_id"))
    DvdObj = Dvd.objects.annotate(nb_EmpruntDvd=Count("emprunter_id"))
    MediaObj = Media.objects.update(bloque=Subquery(Media.objects.filter(id=OuterRef('id')).annotate(bloquer=ExpressionWrapper(Q(dateBack__lt=timezone.now()),output_field=BooleanField())).values("bloquer")[:1])) 
    BloqueObj = Emprunter.objects.update(bloque=Subquery(Media.objects.filter(emprunter_id=OuterRef('id')).order_by().values('bloque')[:1]))
    template_name = 'showBibliothecaire.html'
    context = {'EmprunterObj': EmprunterObj,'LivreObj': LivreObj,'MediaObj': MediaObj,'BloqueObj': BloqueObj,'CdObj': CdObj ,'DvdObj': DvdObj,'GameObj': GameObj}
    return render(request, template_name, context)

def showMediaView(request):
    LivreObj = Livre.objects.all()
    CdObj = Cd.objects.all()
    DvdObj = Dvd.objects.all()
    GameObj = JeuDePlateau.objects.all()
    LivreObj = Livre.objects.annotate(nb_EmpruntLivre=Count("emprunter_id"))
    CdObj = Cd.objects.annotate(nb_EmpruntCd=Count("emprunter_id"))
    DvdObj = Dvd.objects.annotate(nb_EmpruntDvd=Count("emprunter_id"))
    template_name = 'showMembre.html'
    context = {'LivreObj': LivreObj,'CdObj': CdObj ,'DvdObj': DvdObj,'GameObj': GameObj}
    return render(request, template_name, context)

def View(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)

def emprunterFormView(request):
    form = EmprunterForm()
    if request.method == 'POST':
        form = EmprunterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'form_emprunter.html'
    context = {'form': form}
    return render(request, template_name, context )

def updateViewEmprunter(request, f_id):
    EmprunterObj = Emprunter.objects.get(id=f_id)
    form = EmprunterForm(instance=EmprunterObj)
    if request.method == 'POST':
        form = EmprunterForm(request.POST, instance=EmprunterObj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    template_name = 'form_emprunter.html'
    context = {'form': form}
    return render(request, template_name, context)

def livreFormView(request):
    formLivre = LivreForm()
    if request.method == 'POST':
        formLivre = LivreForm(request.POST)
        if formLivre.is_valid():
            formLivre.save()
            return redirect('show_url')
    template_name = 'form_livre.html'
    context = {'formLivre': formLivre}
    return render(request, template_name, context)


def updateViewBook(request, f_id):
    LivreObj = Livre.objects.get(id=f_id)
    formLivre = LivreForm(instance=LivreObj)
    if request.method == 'POST':
        formLivre = LivreForm(request.POST, instance=LivreObj)
        if formLivre.is_valid():
            formLivre.save()
            return redirect('show_url')
    template_name = 'form_livre.html'
    context = {'formLivre': formLivre}
    return render(request, template_name, context)

def cdFormView(request):
    formCd = CdForm()
    if request.method == 'POST':
        formCd = CdForm(request.POST)
        if formCd.is_valid():
            formCd.save()
            return redirect('show_url')
    template_name = 'form_cd.html'
    context = {'formCd': formCd}
    return render(request, template_name, context)


def updateViewCd(request, f_id):
    CdObj = Cd.objects.get(id=f_id)
    formCd= CdForm(instance=CdObj)
    if request.method == 'POST':
        formCd = CdForm(request.POST, instance=CdObj)
        if formCd.is_valid():
            formCd.save()
            return redirect('show_url')
    template_name = 'form_cd.html'
    context = {'formCd': formCd}
    return render(request, template_name, context)

def dvdFormView(request):
    formDvd = DvdForm()
    if request.method == 'POST':
        formDvd = DvdForm(request.POST)
        if formDvd.is_valid():
            formDvd.save()
            return redirect('show_url')
    template_name = 'form_dvd.html'
    context = {'formDvd': formDvd}
    return render(request, template_name, context)


def updateViewDvd(request, f_id):
    DvdObj = Dvd.objects.get(id=f_id)
    formDvd= DvdForm(instance=DvdObj)
    if request.method == 'POST':
        formDvd = DvdForm(request.POST, instance=DvdObj)
        if formDvd.is_valid():
            formDvd.save()
            return redirect('show_url')
    template_name = 'form_dvd.html'
    context = {'formDvd': formDvd}
    return render(request, template_name, context)

def gameFormView(request):
    formGame = JeuDePlateauForm()
    if request.method == 'POST':
        formGame = JeuDePlateauForm(request.POST)
        if formGame.is_valid():
            formGame.save()
            return redirect('show_url')
    template_name = 'form_game.html'
    context = {'formGame': formGame}
    return render(request, template_name, context )

def updateViewGame(request, f_id):
    GameObj = JeuDePlateau.objects.get(id=f_id)
    formGame= JeuDePlateauForm(instance=GameObj)
    if request.method == 'POST':
        formGame = JeuDePlateauForm(request.POST, instance=GameObj)
        if formGame.is_valid():
            formGame.save()
            return redirect('show_url')
    template_name = 'form_game.html'
    context = {'formGame': formGame}
    return render(request, template_name, context)
from django import forms
from .models import Emprunter
from .models import Livre
from .models import Cd
from .models import Dvd
from .models import JeuDePlateau


    
class EmprunterForm(forms.ModelForm):
    class Meta:
        model = Emprunter
        fields = '__all__'
        labels = {
            'name' : "Nom de l'emprunter",
        }
        widgets  = {
            'name' : forms.TextInput(attrs={'placeholder': 'eg. Jhon'}),
        }
    bloque = forms.BooleanField (
        label = 'Bloqué',
        initial=False,
        disabled=True,
        required=False,
        widget = forms.CheckboxInput
    )

class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = '__all__'
        labels = {
            'name' : 'Nom du livre',
            'auteur': "Nom de l'auteur",
        }
        widgets  = {
            'name' : forms.TextInput(attrs={'placeholder': 'eg. Dune'}),
            'auteur': forms.TextInput(attrs={'placeholder': 'eg. Frank Herbert'}),
        }
    emprunter = forms.ModelChoiceField(
        queryset=Emprunter.objects.all(),
        empty_label="Nothing",
        label="Emprunter du media",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    disponible = forms.BooleanField(
        label='Disponible',
        initial=True,
        disabled=True,
        required=False,
    )  
    dateEmprunt = forms.DateTimeField(
        label="Date de l'emprunt",
        disabled=True,
        required=False,
    )
    dateBack = forms.DateTimeField(
        label='Date de retour sur emprunt attendu',
        disabled=True,
        required=False,
    )
    bloque = forms.BooleanField (
        label = 'Bloqué',
        initial=False,
        disabled=True,
        required=False,
    )

class CdForm(forms.ModelForm):
    class Meta:
        model = Cd
        fields = '__all__'
        labels = {
            'emprunter': 'Emprunter du media',
            'name' : 'Nom du cd',
            'artiste': "Nom de l'artiste",
        }
        widgets  = {
            'name' : forms.TextInput(attrs={'placeholder': 'eg. Feu'}),
            'artiste': forms.TextInput(attrs={'placeholder': 'eg. Nekfeu'}),
        }
    emprunter = forms.ModelChoiceField(
        queryset=Emprunter.objects.all(),
        empty_label="Nothing",
        label="Emprunter du media",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    disponible = forms.BooleanField(
        label='Disponible',
        initial=True,
        disabled=True,
        required=False,
    )
    dateEmprunt = forms.DateTimeField(
        label="Date de l'emprunt",
        disabled=True,
        required=False,
    )
    dateBack = forms.DateTimeField(
        label='Date de retour sur emprunt attendu',
        disabled=True,
        required=False,
    )
    bloque = forms.BooleanField (
        label = 'Bloqué',
        initial=False,
        disabled=True,
        required=False,
    )

class DvdForm(forms.ModelForm):
    class Meta:
        model = Dvd
        fields = '__all__'
        labels = {
            'emprunter': 'Emprunter du media',
            'name' : 'Nom du dvd',
            'realisateur': 'Nom du realisateur',
        }
        widgets  ={
            'name' : forms.TextInput(attrs={'placeholder': 'eg. Dune'}),
            'realisateur': forms.TextInput(attrs={'placeholder': 'eg. Denis Villeneuve'}),
        }
    emprunter = forms.ModelChoiceField(
        queryset=Emprunter.objects.all(),
        empty_label="Nothing",
        label="Emprunter du media",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    disponible = forms.BooleanField(
        label='Disponible',
        initial=True,
        disabled=True,
        required=False,
        )
    dateEmprunt = forms.DateTimeField(
        label="Date de l'emprunt",
        disabled=True,
        required=False,
    )
    dateBack = forms.DateTimeField(
        label='Date de retour sur emprunt attendu',
        disabled=True,
        required=False,
    )
    bloque = forms.BooleanField (
        label = 'Bloqué',
        initial=False,
        disabled=True,
        required=False,
    )    

class JeuDePlateauForm(forms.ModelForm):
    class Meta:
        model = JeuDePlateau
        fields = '__all__'
        labels = {
            'name' : 'Nom du jeu de plateau',
            'createur': 'Nom du createur',
        }
        widgets  ={
            'name' : forms.TextInput(attrs={'placeholder': 'eg. Krosmaster'}),
            'createur': forms.TextInput(attrs={'placeholder': 'eg. Tot et Jérôme Peschard'}),
        }
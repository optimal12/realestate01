from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Property ,Surfer, City, Neighborhood
from django.views import generic
class HomeValueForm(forms.Form):
    #Estimation of property value class
    #city=forms.CharField(max_length=35,help_text=" Enter city",required=False)
    #neighborhood=forms.CharField(max_length=35, help_text=" Enter neighborhood",required=False)
    #ciudades=City.objects.filter(pk__in=[1,22]).values()
    #barrios=['merkaz RamatAsharon','merkaz RA'],['tzafon iashan TA','TzafonIashanTA'],['merkaz Hertzlia','Hertzlyia Mercaz'],['shikunDaletBeerSheva','ShikunDaletBeersheva'],['Hertzlyia Mercaz','הרצליה מרכז']
    #ciudades=['Tel Aviv','TelAviv'],['Ramat Hasharon','RmatASharon'],['Hertzlyia','Hertzlyia'],['Beer Sheba','BeerSheba'],['Hertzlia','הרצליה'],[ 'Tel Aviv','TelAviv'],['Ramat Hasharon','RmatASharon'],['Hertzlyia','Hertzlyia'],['Beer Sheba','BeerSheba'],['הרצליה','הרצליה'],[ 'Tel Aviv','TelAviv'],['Ramat Hasharon','RmatASharon'],['Hertzlyia','Hertzlyia'],['Beer Sheba','BeerSheba'],['הרצליה','הרצליה'],[ 'Tel Aviv','TelAviv'],['Ramat Hasharon','RmatASharon'],['Hertzlyia','Hertzlyia'],['Beer Sheba','BeerSheba'],['הרצליה','הרצליה'],[ 'Tel Aviv','TelAviv'],['Ramat Hasharon','RmatASharon'],['Hertzlyia','Hertzlyia'],['Beer Sheba','BeerSheba'],['הרצליה','הרצליה'],[ 'Tel Aviv','TelAviv'],['Ramat Hasharon','RmatASharon'],['Hertzlyia','Hertzlyia'],['Beer Sheba','BeerSheba'],['הרצליה','הרצליה'],[ 'Tel Aviv','TelAviv'],['Ramat Hasharon','RmatASharon'],['Hertzlyia','Hertzlyia'],['Beer Sheba','BeerSheba'],['הרצליה','הרצליה'],[ 'Tel Aviv','TelAviv'],['Ramat Hasharon','RmatASharon'],['Hertzlyia','Hertzlyia'],['Beer Sheba','BeerSheba'],['הרצליה','הרצליה'],[ 'Tel Aviv','TelAviv'],['Ramat Hasharon','RmatASharon'],['Hertzlyia','Hertzlyia'],['Beer Sheba','BeerSheba'],['הרצליה','הרצליה']
    barrios=['Hertzlyia Mercaz','הרצליה מרכז'],['RSM','Ramat Ha Sharon Mercaz']
    ciudades=['Hertzlyia','הרצליה'],['TA','Tel Aviv']
    city=forms.ChoiceField(label='ישוב',choices=ciudades,widget=forms.Select(attrs={'class': 'form-control'}))
    neighborhood=forms.ChoiceField(label='שכונה',choices=barrios,widget=forms.Select(attrs={'class': 'form-control'}))                       
    roomsnumber=forms.DecimalField(label='מספר חדרים',max_digits=6,help_text="בין 1 ל9")
    builtarea=forms.DecimalField(label='שטח נטו',max_digits=8,decimal_places=2,help_text="בין 20 ל500")
    street=forms.CharField(label='רחוב',max_length=35,help_text="שם הרחוב")
    streetnumber=forms.IntegerField(label='מספר הבית',help_text="מספר")
    email=forms.EmailField(label='אמייל',help_text="אמייל תקין")
    surfingdate=forms.DateField(label='תאריך',help_text="דוגמה 2006-10-25")
    """
class Meta:
    model = Surfer  
    widgets = {
        'city': forms.Select(attrs={'class': 'bootstrap-select'}),
    }
    """
    #here we validate the input
    def clean_roomsnumber(self):
        data = self.cleaned_data['roomsnumber']
        #check if roomsnumber is valid
        if data < 1.: raise ValidationError(_('Invalid rooms number < 1'))
        if data > 9.: raise ValidationError(_('Invalid rooms number > 9'))
        return data
    def clean_builtarea(self):
        data = self.cleaned_data['builtarea']
        #check if builtarea is valid
        if data < 20. : raise ValidationError(_('Invalid built area < 20'))
        if data > 500.: raise ValidationError(_('Invalid built area > 500'))
        #remember to return data
        return data
    def clean_city(self):
        data = self.cleaned_data['city']
        return data
    def clean_neighborhood(self):
        data = self.cleaned_data['neighborhood']
        return data     
    def clean_street(self):
        data = self.cleaned_data['street']
        return data     
    def clean_email(self):
        data = self.cleaned_data['email']
        return data
    def clean_streetnumber(self):
        data = self.cleaned_data['streetnumber']
        return data
    def clean_surfingdata(self):
        data = self.cleaned_data['surfingdate']
        return data     

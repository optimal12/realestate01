from django.shortcuts import render,get_object_or_404
from .models import City, Neighborhood, Property, Surfer
from django.views import generic
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .forms import HomeValueForm
import datetime
# Create your views here.
def index(request):
    #view function for site's homepage
    #generate COUNTS OF 2 lists 1)Cities and 2)Neighborhoods
    cities = City.objects.all().count()
    neighborhoods = Neighborhood.objects.all().count()
    #Render the HTML index.html with data in the context variable
    return render(
        request,
        'index.html',
context = {'cities_num' : cities,'neighborhoods_num' : neighborhoods},
    )            
class CityListView(generic.ListView):
    model=City
    paginate_by = 10
class NeighborhoodListView(generic.ListView):
    model=Neighborhood
    queryset=Neighborhood.objects.all()
    paginate_by = 10
    #i=self.request.GET.get('q')
    #queryset=Neighborhood.objects.filter(city = i)
    #select the neihborhoods for picked city
def home_value_calculate(request):
    #if this is a POST request process data
    if request.method == 'POST':
        #create a form instance
        form= HomeValueForm(request.POST)
        #check if the form is valid
        if form.is_valid():
            #Now Calculate Home Value
            cityx=form.cleaned_data['city']
            neighborhoodx = form.cleaned_data['neighborhood']
            roomsx=form.cleaned_data['roomsnumber']
            areax=form.cleaned_data['builtarea']
            streetx=form.cleaned_data['street']
            streetnumberx=form.cleaned_data['streetnumber']                          
            emailx=form.cleaned_data['email']
            streetx=form.cleaned_data['street']
            surfingdatex=form.cleaned_data['surfingdate']
            #irx=form.cleaned_data['ir']
            #schunax=form.cleaned_data['schuna']
            #cityx='הרצליה'
            #neighborhoodx='הרצליה מרכז'
            #tt=City.objects.filter(city=cityx)
            #tr=Neighborhood.objects.filter(neighborhood=neighborhoodx)
            #cityx=tt.id
            #neighborhoodx=tr.id
            properties=Property.objects.filter(city=cityx).filter(neighborhood=neighborhoodx)
            #properties=Property.objects.filter(city=irx,neighborhood=schunax)
            orderedproperties=properties.order_by('roomsnumber','builtarea')
            countx=orderedproperties.count()
            i=0
            j=0
            proper_list=list(orderedproperties.all())
            for i in range(countx):
                if proper_list(i).roomsnumber >= roomsx:
                    for j in range(i,countx):
                        if proper_list(j).builtarea >= areax:
                            numero=j
            #numero is the ordered properties index selected to calculate the price
            #Here we deal with the case in wich the i is the last element inordredproperties
            if  j==0:
                pricex=((proper_list(countx).price-proper_list(countx-1).price)*(proper_list(countx).roomsnumber-proper_list(countx-1).roomsnumber)/proper_list(countx-1).roomsnumber)+orderedproperies(count).price
            #Here we deal with the case in wich the j is the last element inordredproperties
            if j>= countx:
                pricex=((proper_list(countx).price-proper_list(countx-1).price)*(proper_list(countx).builtarea-proper_list(countx-1).builtarea)/proper_list(countx-1).builtarea)+orderedproperies(count-1).price
            if j>0 and j<contx:
                #here we select numero as the price rendering property
                pricex=((proper_list(numero).price-proper_list(numero-1).price)*(proper_list(numero).builtarea-proper_list(numero-1).builtarea)/proper_list(numero-1).builtarea)+orderedproperies(numero-1).price
            #pricex is the result of the search
      
            #process the data.Now insert a new surfer record
            surfer=Surfer()
            surfer.city=irx
            surfer.neighborhood=schunax
            surfer.roomsnumber=roomsx
            surfer.builtarea=areax
            surfer.street=streetx
            surfer.streetnumber=streetnumberx
            surfer.email=emailx
            surfer.surfingdate=surfindatex
            surfer.price = pricex
            surfer.save()
    #redirect to the Home page
            return HttpResponseRedirect(reverse('omdan'))
    #if this is a GET or any other method create default form        
    else:
        form = HomeValueForm()
    return render(request,'home_value_calculate.html',{'form':form })    



            

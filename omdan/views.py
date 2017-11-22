from django.shortcuts import render,get_object_or_404
from .models import City, Neighborhood, Property, Surfer
from django.views import generic
from django.http import HttpResponseRedirect
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
        context ={ 'cities_num' : cities ,'neighborhoods_num' : neighborhoods},
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
 #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    #def attribute estimation

def estimation(request):
    #view function for estimation results
    #generate COUNTS OF 2 lists 1)Cities and 2)Neighborhoods
    price = pricex
    #Render the HTML index.html with data in the context variable
    return render(
        request,
        'estimation.html',
        context ={ 'price' : price },
    )
    #XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX       
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
            #properties=Property.objects.filter(city=cityx).filter(neighborhood=neighborhoodx)
            #orderedproperties=properties.order_by('roomsnumber','builtarea')
            #countx=orderedproperties.count()
            #i=0
            #j=0
            #proper_list=list(orderedproperties.all())
            #for i in range(countx):
            #    if proper_list(i).roomsnumber >= roomsx:
            #        for j in range(i,countx):
            #           if proper_list(j).builtarea >= areax:
            #                numero=j
            #numero is the ordered properties index selected to calculate the price
            #Here we deal with the case in wich the i is the last element inordredproperties
            #if  j==0:
            #    pricex=((proper_list(countx).price-proper_list(countx-1).price)*(proper_list(countx).roomsnumber-proper_list(countx-1).roomsnumber)/proper_list(countx-1).roomsnumber)+orderedproperies(count).price
            #Here we deal with the case in wich the j is the last element inordredproperties
            #if j>= countx:
            #    pricex=((proper_list(countx).price-proper_list(countx-1).price)*(proper_list(countx).builtarea-proper_list(countx-1).builtarea)/proper_list(countx-1).builtarea)+orderedproperies(count-1).price
            #if j>0 and j<contx:
                #here we select numero as the price rendering property
                #pricex=((proper_list(numero).price-proper_list(numero-1).price)*(proper_list(numero).builtarea-proper_list(numero-1).builtarea)/proper_list(numero-1).builtarea)+orderedproperies(numero-1).price
            #get a subset of Property with given city,neighborhood,rooms ordered buy area
            N= Property.objects.filter(city=cityx).filter(neighborhood=neighborhoodx).filter(roomsnumber=roomsx).order_by('builtarea').count()
            #N= Property.objects.filter(city__contains=cityx).filter(neighborhood__contains=neighborhoodx).filter(roomsnumber=roomsx).order_by('builtarea').count()
            if N == 0: #when there is an empty queryset redirect
                return HttpResponseRedirect(reverse('index'))# was 'index'
            i=0
            for e in Property.objects.filter(city=cityx).filter(neighborhood=neighborhoodx).filter(roomsnumber=roomsx).order_by('builtarea'):
            #for e in Property.objects.filter(city__contains=cityx).filter(neighborhood__contains=neighborhoodx).filter(roomsnumber=roomsx).order_by('builtarea'):
                i=i+1     
                if (e.builtarea >= areax) and i <=N:#for the general case
                    pricea=e.price
                    areaa=e.builtarea
                    pricex=(pricea*(areax-areaa)/areax)+pricea
                #here we have areax over all the available areas
                if (e.builtarea<areax) and (i>=N):
                    arean=e.builtarea
                    pricen=e.price
                    pricex=(pricen*(areax-arean)/arean)+pricen
            #pricex is the result of the search
            """
            here we send an email to the surfer with the estimate
            from django.core.mail import send_mail
            send_mail(
                'Subject here',
                'Here is the message.',
                'from@example.com',
                ['to@example.com'],
                fail_silently=False,
            )
            Mail is sent using the SMTP host and port specified in the EMAIL_HOST and EMAIL_PORT settings. The
EMAIL_HOST_USER and EMAIL_HOST_PASSWORD settings, if set, are used to authenticate to the SMTP server,
and the EMAIL_USE_TLS and EMAIL_USE_SSL settings control whether a secure connection is used.
            """
            #process the data.Now insert a new surfer record
            surfer=Surfer()
            surfer.city=cityx
            surfer.neighborhood=neighborhoodx
            surfer.roomsnumber=roomsx
            surfer.builtarea=areax
            surfer.street=streetx
            surfer.streetnumber=streetnumberx
            surfer.email=emailx
            surfer.surfingdate=surfingdatex
            surfer.price = pricex
            surfer.save()
            #redirect to the Home page
            #return HttpResponseRedirect(reverse('estimation',kwargs={ 'price':pricex}))
            #render the resuls to estimation template
            return render(request,'estimation.html', { 'price':pricex })
    #if this is a GET or any other method create default form        
    else:
        form = HomeValueForm()
    return render(request,'home_value_calculate.html',{'form':form })    

    


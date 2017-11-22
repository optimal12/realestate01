from django.conf.urls import url
# Use include() to add URLS from the omdan application 
from django.conf.urls import include
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^cities/$',views.CityListView.as_view(),name='cities'),
    url(r'^neighborhoods/$',views.NeighborhoodListView.as_view(),name='neighborhoods'),
]



#Add URL maps to redirect the base URL to our application

from django.views.generic import RedirectView
urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/omdan/', permanent=True)),
]
# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [
    url(r'^home_value_calculate$',views.home_value_calculate,name='home_value_calculate'),
]
urlpatterns += [
    url(r'^$',views.estimation,name='estimation'),
]


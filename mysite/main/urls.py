"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path , re_path
from . import views

app_name = "main"

urlpatterns = [
   	
   	path("",views.start),
   	re_path(r'about.html/$',views.about,name='about'),
   	re_path(r"agents.html/$",views.agents,name='agents'),
   	re_path(r"apartemnt.html/$",views.apartment,name='apartment'),
   	re_path(r"apartment-building.html/$",views.apartmentBuilding,name='apartmentbuilding'),
   	re_path(r"blog-details.html/$",views.blogDetails,name='blogdetails'),
   	re_path(r"car.html/$",views.car,name='car'),
   	re_path(r"columns.html/$",views.columns,name='columns'),
   	re_path(r"contact.html/$",views.contact,name='contact'),
   	re_path(r"dashboard.html/$",views.dashboard,name='dashboard'),
   	re_path(r"faq.html/$",views.faq,name='faq'),
   	re_path(r"full-gallery.html/$",views.fullGallery,name='fullgallery'),
   	re_path(r"gridlisting.html/$",views.gridListing,name='gridlisting'),
   	re_path(r"index.html/$",views.index,name='index'),
   	re_path(r"large-map.html/$",views.large_Map,name='largemap'),
   	re_path(r"listing-map.html/$",views.listing_Map,name='listingmap'),
   	re_path(r"listing.html/$",views.listing,name='listing'),
   	re_path(r"listingmap.html/$",views.listingMap,name='listingmap2'),
   	re_path(r"login.html/$",views.login,name='login'),
   	re_path(r"miami-city.html/$",views.miamiCity,name='miamicity'),
   	re_path(r"news.html/$",views.news,name='news'),
   	re_path(r"normal-slider.html/$",views.normalSlider,name='normalslider'),
   	re_path(r"office.html/$",views.office,name='office'),
   	re_path(r"portfolio-2.html/$",views.portfolio2,name='portfolio2'),
   	re_path(r"portfolio-3.html/$",views.portfolio3,name='portfolio3'),

   	re_path(r"portfolio-4.html/$",views.portfolio4,name='portfolio4'),
    re_path(r"property.html/$",views.property,name='property'),
   	re_path(r"rent.html/$",views.rent,name='rent'),
   	re_path(r"rev-slider.html/$",views.revSlider,name='revslider'),
   	re_path(r"sale.html/$",views.sale,name='sale'),
   	re_path(r"shop.html/$",views.shop,name='shop'),
   	re_path(r"signup.html/$",views.signup,name='signup'),
   	re_path(r"single-family.html/$",views.singleFamily,name='singlefamily'),
   	re_path(r"single-property.html/$",views.singleProperty,name='singleproperty'),
   	re_path(r"start.html/$",views.start,name='start'),
   	re_path(r"submission.html/$",views.submission,name='submission'),
   	re_path(r"testimonials.html/$",views.testimonials,name='testimonials'),
   	re_path(r"typography.html/$",views.typography,name='typography'),
   	re_path(r"viall.html/$",views.viall,name='viall'),
  		



]

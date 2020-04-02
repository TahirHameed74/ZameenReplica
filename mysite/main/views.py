from django.shortcuts import render ,redirect
from django.http import HttpResponse
# Create your views here.


def start(request): 
    return render(request, 'main/start.html')	
def about(request):
	return render(request, 'main/about.html')	
def agents(request):
	return render(request, 'main/agents.html')
def apartment(request):
	return render(request, 'main/apartemnt.html')	
def apartmentBuilding(request):
	return render(request, 'main/apartment-building.html')
def blogDetails(request):
	return render(request, 'main/blog-details.html')
def car(request):
	return render(request, 'main/car.html')			
def columns(request):
	return render(request, 'main/columns.html')		
def contact(request):
	return render(request, 'main/contact.html')
def dashboard(request):
	return render(request, 'main/dashboard.html')
def faq(request):
	return render(request, 'main/faq.html')
def fullGallery(request):
	return render(request, 'main/full-gallery.html')
def gridListing(request):
	return render(request, 'main/gridlisting.html')
def index(request):
	return render(request, 'main/index.html')
def large_Map(request):
	return render(request, 'main/large-map.html')
def listing_Map(request):
	return render(request, 'main/listing-map.html')
def listing(request):
	return render(request, 'main/listing.html')
def listingMap(request):
	return render(request, 'main/listingmap.html')
def login(request):
	return render(request, 'main/login.html')
def miamiCity(request):
	return render(request, 'main/miami-city.html')
def news(request):
	return render(request, 'main/news.html')
def normalSlider(request):
	return render(request, 'main/normal-slider.html')
def office(request):
	return render(request, 'main/office.html')
def portfolio2(request):
	return render(request, 'main/portfolio-2.html')
def portfolio3(request):
	return render(request, 'main/portfolio-3.html')
def portfolio4(request):
	return render(request, 'main/portfolio-4.html')
def property(request):
	return render(request, 'main/property.html')
def rent(request):
	return render(request, 'main/rent.html')
def revSlider(request):
	return render(request, 'main/rev-slider.html')
def sale(request):
	return render(request, 'main/sale.html')
def shop(request):
	return render(request, 'main/shop.html')
def signup(request):
	return render(request, 'main/signup.html')
def singleFamily(request):
	return render(request, 'main/single-family.html')
def singleProperty(request):
	return render(request, 'main/single-property.html')
def submission(request):
	return render(request, 'main/submission.html')
def testimonials(request):
	return render(request, 'main/testimonials.html')
def typography(request):
	return render(request, 'main/typography.html')
def viall(request):
	return render(request, 'main/viall.html')



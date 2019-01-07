from django.shortcuts import render
from .models import Listing
from django.shortcuts import get_object_or_404, render   
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator #importing Paginator from django.core
from listings.choices import state_choices,bedroom_choices,price_choices

# Create your views here.

def  index(request):
   # listings = Listing.objects.all() #fetches all records from db, not an error just a linting error in editor
   listings = Listing.objects.order_by('-list_date').filter(is_piblished=True)#Fetches all records from db by descending order of date as specified by -list_date and filter specifies condition so is_piblihed checkbox is checked then only that listing will be shown
   paginator = Paginator(listings, 1)#1st param is for what should be paginated and second param is for how many listing per page should appear
   page = request.GET.get('page') #This will get the url parameter value of page for eg page=2 will return 2 and store it in page variable
   paged_listings = paginator.get_page(page)#This will return a page when when called for so when page=2 2nd page listings will be called


   
   context = {
      'listings': paged_listings
   }
   return render(request, 'listings/listings.html',context)

def  listing(request, listing_id):
   listing = get_object_or_404(Listing, pk=listing_id) #check if listing_id exist in db for eg if someone enters /listing/50 manually and 50 is not present then 404 error is generated


   context={
      'listing':listing
   }
   return render(request, 'listings/listing.html',context)

def search(request):
   querset_list = Listing.objects.order_by('-list_date')
   
   # Keywords
   if 'keywords' in request.GET:
      keywords = request.GET['keywords']
      if keywords:
         querset_list = querset_list.filter(description__icontains=keywords)


   # city
   if 'city' in request.GET:
      city = request.GET['city']
      if city:
         querset_list = querset_list.filter(city__iexact=city)

   # state
   if 'state' in request.GET:
      state = request.GET['state']
      if state:
         querset_list = querset_list.filter(state__iexact=state)

   #Bedrooms
   if 'bedrooms' in request.GET:
      bedrooms = request.GET['bedrooms']
      if bedrooms:
         querset_list = querset_list.filter(bedrooms__lte=bedrooms)

   # Price
   if 'price' in request.GET:
      price = request.GET['price']
      if price:
         querset_list = querset_list.filter(price__lte=price)

   context = {
      'state_choices': state_choices,
      'bedroom_choices': bedroom_choices,
      'price_choices': price_choices,
      'listings': querset_list,
      'values': request.GET  #this wil help us for form layout data persistence
   }

   return render(request, 'listings/search.html',context)
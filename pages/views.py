from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing 
from realtors.models import Realtor
from listings.choices import price_choices , bedroom_choices, state_choices


# Create your views here.



def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_piblished=True)[:3]
    # listings = Listing.objects.order_by('-list_date').filter(is_piblished=True)
    context = {
        'listings':listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices
        
    }
    return render(request,'pages/index.html',context)

def about(request):
    # Get all Realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Get mvp realtor
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context1= {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    
    return render(request,'pages/about.html',context1)
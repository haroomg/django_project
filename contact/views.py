from django.shortcuts import render
from .models import *

# Create your views here.

def index(reques):
    
    contacts = Contact.objects.all()
    
    context = {
        'contacts': contacts
    }
    
    return render(reques, 'contact/index.html', context) 

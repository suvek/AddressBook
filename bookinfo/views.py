from django.shortcuts import render

from bookinfo.models import AddressBook
from bookinfo.forms import ContactForm


def home(request):
	contact_list = AddressBook.objects.all()
	return render(request,'home.html', {'contact_list': contact_list})

def contactDetails(request):
	passed_id = request.GET["id"]
	contact_details = AddressBook.objects.get(pk = passed_id)
	return render(request,'contactDetails.html', {'contact_details': contact_details})

def newContact(request):
	if request.method == 'POST':
	
		form = ContactForm(request.POST)
		if form.is_valid():
			instance = form.save() 
			instance.save() 		      
            						                
	else:  
		form = ContactForm()

	return render(request,'newContact.html', {'form': form})

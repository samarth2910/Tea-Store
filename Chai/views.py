from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Chai
# Create your views here.
def all_chai(request):
    # This view will render a template that lists all chai items
    chai_info= Chai.objects.all()  # Fetch all Chai objects from the database
    return render(request, 'Chai/all_chai.html', {'chais': chai_info})

def chai_detail(request, chai_id):
    # This view will render a template that shows details of a specific chai item
    chai_item = get_object_or_404(Chai,pk=chai_id)  # Fetch a specific Chai object by its ID
    return render(request, 'Chai/chai_detail.html', {'chai': chai_item})

def chai_home(request):
    chai_info = Chai.objects.all()  # Fetch all Chai objects from the database
    return render(request, 'Chai/chai_home.html', {'chais': chai_info})

def view_cart(request):
    return HttpResponse("Cart page coming soon!")


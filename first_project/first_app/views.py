from django.shortcuts import render
from first_app.models import AccessRecord, Topic, Webpage, Users

# Create your views here.

from  django.http import HttpResponse

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' : webpage_list}
    
    return render(request, 'first_app/index.html', context=date_dict)

def users(request):
    
    users_list = Users.objects.order_by('lastName')
    users_dict = {
        'users' : users_list, 
    }
    
    return render(request, 'first_app/users.html', context=users_dict)
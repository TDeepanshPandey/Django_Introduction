from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessRecord, User

# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    my_dict = {"insert_me": "Changed I am from views.py!"}
    return render(request, "first_app/index.html", context=date_dict)

def users(request):
    user = User.objects.order_by('first_name')
    user_dict = {'users': user}
    return render(request, "first_app/users.html", context=user_dict)

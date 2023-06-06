from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessRecord, User
from .forms import NewUser
# Create your views here.
def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    my_dict = {"insert_me": "Changed I am from views.py!"}
    return render(request, "first_app/index.html", context=date_dict)

def users(request):
    form = NewUser()
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error form invalid")
    return render(request, "first_app/users.html", {'form': form})


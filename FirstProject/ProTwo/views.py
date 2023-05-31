from django.shortcuts import render


# Create your views here.
def help(request):
    help_dict = {"help_insert": "HELP PAGE"}
    return render(request, "ProTwo/index.html", context=help_dict)

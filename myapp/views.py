from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def index(request):
#     return HttpResponse('Thats Works !')

# def feb(request):
#     return HttpResponse("IT's Feb")

def monthly_challenges(request,month):
    challenge_text = None
    if month == "january":
        challenge_text ="This is january"
    elif month == "february":
        challenge_text =  "This is Feburary"
    elif month == "march":
        challenge_text = "This Is March"
    elif month == "april":
        challenge_text = "This is April"    
    else:
        return HttpResponseNotFound("This is not found")      
    return HttpResponse(challenge_text)
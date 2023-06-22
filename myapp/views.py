from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# def index(request):
#     return HttpResponse('Thats Works !')

# def feb(request):
#     return HttpResponse("IT's Feb")

monthly_challenges = {
    "january": "This is january",
    "february" : "This is Feb",
    "march" : "This Is March",
    "april":"This Is April",
    "may": "This is May"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("myapp",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This is not found")      
    
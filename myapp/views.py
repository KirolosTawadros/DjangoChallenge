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
    redirect_path = reverse("my-app",args=[redirect_month])   #/myapp/january "my-app"-->myapp////args-->/month
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This is not found")      
    
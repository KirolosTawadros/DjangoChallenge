from django.urls import path
from . import views


urlpatterns = [
    # path('january',views.index),
    # path('february',views.feb),
    path('<int:month>',views.monthly_challenge_by_number),
    path('<str:month>',views.monthly_challenge, name='my-app')
]

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Produit, Album

def produit(request):
    latest_obj_list = Produit.objects.order_by('-pub_date')[:5]
    # output = ', '.join([q.name for q in latest_question_list])
    output = [q.name for q in latest_obj_list]

    return HttpResponse(output)
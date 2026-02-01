from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def notification_list(request):
    return JsonResponse({"message": "Notification list placeholder"})
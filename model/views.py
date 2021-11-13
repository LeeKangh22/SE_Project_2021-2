from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def getStaffList(request, sid):
    return HttpResponse("for test %s" % sid)

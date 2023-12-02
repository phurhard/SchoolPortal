from django.shortcuts import render

# Create your views here.

def index(request):
    '''this is the landing page for staffs'''
    return render(request, 'Staff/index.html')

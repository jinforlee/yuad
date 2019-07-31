from django.shortcuts import render
from django.contrib import messages





# Create your views here.

def new_2(request):
    return render(request, 'new_2.html')

def new_3(request):
    return render(request, 'new_3.html')

def final(request):
    return render(request, 'final.html')

def wrong_(request):
    return render(request, 'wrong_.html')
    

def worng_1(request):
    return render(request, 'wrong_1.html')
    
def wrong_2(request):
    return render(request, 'wrong_2.html')
    
def list_(request):
    food = request.GET['food']
    drink = request.GET['drink']
    place = request.GET['place']  
    content = {'food' : food, 'drink' : drink, 'place' :place}
    while food=='' or drink=='' or place=='' :
        messages.info(request, "빠짐 없이 입력해주시죠")
        return render(request, 'final.html')
    return render(request, 'list_.html', content)


    
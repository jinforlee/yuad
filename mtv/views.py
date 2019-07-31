from django.shortcuts import render


def index(request):
   
    return render(request, 'index.html')
        
       
        
#request는 웹구성에 필요한 내용들을 포함한다.
       
           #render(request, '화면에 표시할 html')
def new(request):
#request는 웹구성에 필요한 내용들을 포함한다.
    return render(request, 'new.html')
           #render

def sin(request):
   
    return render(request, 'sin.html')


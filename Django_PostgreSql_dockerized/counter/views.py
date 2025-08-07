from django.shortcuts import render

from .tasks import my_counter

# Create your views here.

def counter(request):
    
    result = my_counter.apply_async(countdown=3) 

    print("hello world from view")
    print('count value from view', result.get())

    return render(request, 'counter.html', {'result': result.get()})

# chat/views.py
from django.shortcuts import render

def indexView(request):
    return render(request, 'chat/index.html')



def roomView(request, room_name):

    context = {
        'room_name' : room_name
    }
    
    return render(request, 'chat/room.html', context)
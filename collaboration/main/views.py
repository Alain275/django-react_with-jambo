from django.shortcuts import render
from main.models import User

def hero_world_view(request):
    queryset = User.objects.filter(id__range=(7, 20)).order_by('-id')  # Adjust the range as needed
    context = {
        'users': queryset  # Passing the queryset to the template
    }
    return render(request, 'index.html', context)

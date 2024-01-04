from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Train

def home(request):
    trains_list = Train.objects.all()
    paginator = Paginator(trains_list, 4)  # Show 7 trains per page
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'myapp/index.html', {'trains': trains})

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Train, Station

def home(request):
    trains_list = Train.objects.filter(train_available=True)
    paginator = Paginator(trains_list, 4) 
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'myapp/index.html', {'trains': trains})

def train_details(request,train_number):
    train = get_object_or_404(Train,train_number=train_number, train_available=True)
    stations = Station.objects.filter(train=train)
    return render(request,'myapp/train_details.html',{'train':train,'stations':stations})

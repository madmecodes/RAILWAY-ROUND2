from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Train, Station
from django.db.models import F, Case, When, Value, Min, CharField, Q

def home(request):
    trains_list = Train.objects.filter(train_available=True)
    paginator = Paginator(trains_list, 4) 
    page = request.GET.get('page')
    trains = paginator.get_page(page)
    return render(request, 'myapp/index.html', {'trains': trains})

def train_details(request):
    train_number = request.GET.get('train_number', '')
    if train_number:
        train = get_object_or_404(Train, train_number=train_number, train_available=True)
        stations_list = Station.objects.filter(train=train)
        paginator=Paginator(stations_list,7)
        page= request.GET.get('page')
        stations = paginator.get_page(page)
        return render(request, 'myapp/train_details.html', {'train': train, 'stations': stations})
    else:
        return render(request, {'error_message': 'Please enter a valid train number'}, status=404)


def choose_train(request):
    station_codes = Station.objects.values_list('station_code', flat=True).distinct()
    #station_codes =   Station.objects.filter(station_code__isnull=False).distinct().distinct()
    context = {'station_codes': station_codes}
    return render(request, 'myapp/choose_train.html', context)

# generated helper function from gpt based on sql query::
# SELECT DISTINCT s1.train_number,s1.arrival_time as sourceStationTime, s2.arrival_time as DestinationStationTime
# FROM myapp_station s1
# INNER JOIN myapp_station s2 ON s1.train_number = s2.train_number
# WHERE s1.station_code = 'ST3'
#   AND s2.station_code = 'ST7'
#   AND s1.arrival_time < s2.arrival_time;

def get_relevant_train_number_and_time(source_station, destination_station):
    relevant_trains = (
        Station.objects
        .filter(station_code=source_station)
        .values('train__train_number','train__train_name' , 'train__total_seats_1ac','train__total_seats_2ac', 'train__total_seats_3ac', 'train__runs_on', 'train__fare_1ac','train__fare_2ac','train__fare_3ac','distance' ,'arrival_time','station_name')
        .annotate(
            destination_arrival_time=Min(
                Case(
                    When(train__station__station_code=destination_station, then=F('train__station__arrival_time')),
                    default=Value('23:59:59'),  # Set a default time to ensure it is greater than any valid time
                    output_field=CharField()  # You may need to adjust the output field type based on your model
                )
            )
        )
        .filter(destination_arrival_time__gt=F('arrival_time'))
        .values('train__train_number', 'arrival_time', 'destination_arrival_time','train__train_name' , 'train__total_seats_1ac','train__total_seats_2ac', 'train__total_seats_3ac', 'train__runs_on', 'train__fare_1ac','train__fare_2ac','train__fare_3ac','distance','station_name')
        .distinct()
    )
    return relevant_trains

def find_trains(source_code, destination_code):
    # Assuming you have a model called Station with fields train_number, arrival_time, and station_code
    # and a model called Train with fields train_number and train_name

    # Filter stations for the source and destination codes
    source_stations = Station.objects.filter(station_code=source_code)
    destination_stations = Station.objects.filter(station_code=destination_code)

    # Get trains for the source and destination stations
    source_trains = Train.objects.filter(station__in=source_stations)
    destination_trains = Train.objects.filter(station__in=destination_stations)

    # Get common trains between source and destination
    common_trains = source_trains.filter(train_number__in=destination_trains.values('train_number'))

    # Annotate source and destination times
    common_trains = common_trains.annotate(
        source_time=F('station__arrival_time'),
        destination_time=F('station__arrival_time')
    )

    # Filter trains based on source_time and destination_time
    common_trains = common_trains.filter(Q(source_time__lt=F('destination_time')))

    # Distinct trains based on train_number, train_name, source_time, destination_time
    common_trains = common_trains.distinct().values(
        'train_number', 'train_name', 'source_time', 'destination_time'
    )

    return common_trains

def choose_train_list(request):
    if(request.method == 'POST'):
        source_station = request.POST.get('source_station', '')
        destination_station = request.POST.get('destination_station','')
        relevant_trains = get_relevant_train_number_and_time(source_station,destination_station)
        station_codes = Station.objects.values_list('station_code', flat=True).distinct()
        context= {'relevant_trains':relevant_trains, 'stations_codes':station_codes,'source_station':source_station,'destination_station':destination_station}

    return render(request,'myapp/choose_train_list.html',context)
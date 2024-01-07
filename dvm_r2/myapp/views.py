from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Train, Station
from django.db.models import F, Case, When, Value, Min, CharField, Q
from django.db import models


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
        .annotate(
            destination_arrival_time=Min(
                'train__station__arrival_time', 
                filter=Q(train__station__station_code=destination_station)
            ),
            source_distance=F('distance'),
            destination_distance=Min(
                'train__station__distance',
                filter=Q(train__station__station_code=destination_station)
            )
        )
        .filter(destination_arrival_time__gt=F('arrival_time'))
        .values(
            'train__train_number', 
            'arrival_time', 
            'destination_arrival_time',
            'train__train_name',
            'train__total_seats_1ac',
            'train__total_seats_2ac',
            'train__total_seats_3ac',
            'train__runs_on',
            'train__fare_1ac',
            'train__fare_2ac',
            'train__fare_3ac',
            'source_distance',
            'destination_distance',
            'station_name'
        )
        .distinct()
    )

    return relevant_trains


def calculate_overall_relative_distance(relevant_trains):
    overall_relative_distance = (
        relevant_trains.aggregate(
            overall_relative_distance=Min(F('source_distance') - F('destination_distance')) 
            #doubt why Min; if not error if random value else not 
        )['overall_relative_distance'] or 0
    )
    overall_relative_distance = abs(overall_relative_distance)
    return overall_relative_distance

def calculate_relative_fare(fare, overall_relative_distance):
    relative_fare = round(fare * overall_relative_distance/10)

    return relative_fare

def choose_train_list(request):
    if request.method == 'POST':
        source_station = request.POST.get('source_station', '')
        destination_station = request.POST.get('destination_station', '')
        relevant_trains = get_relevant_train_number_and_time(source_station, destination_station)

        overall_relative_distance = calculate_overall_relative_distance(relevant_trains)

        for train in relevant_trains:
            train['relative_fare_1ac'] = calculate_relative_fare(train.get('train__fare_1ac', 0), overall_relative_distance)
            train['relative_fare_2ac'] = calculate_relative_fare(train.get('train__fare_2ac', 0), overall_relative_distance)
            train['relative_fare_3ac'] = calculate_relative_fare(train.get('train__fare_3ac', 0), overall_relative_distance)

        station_codes = Station.objects.values_list('station_code', flat=True).distinct()
        context = {
            'relevant_trains': relevant_trains,
            'station_codes': station_codes,
            'source_station': source_station,
            'destination_station': destination_station,
            'overall_relative_distance': overall_relative_distance,
        }

        return render(request, 'myapp/choose_train_list.html', context)
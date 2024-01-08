from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Passenger
import json

# Create your views here.

@login_required
def booking_form(request):
    if request.method == 'POST':
        ticket_type = request.POST.get('ticket_type')
        fare = request.POST.get('fare')
        total_seats = request.POST.get('total_tickets')
        train_number = request.POST.get('train_number')

        context = {
            'ticket_type': ticket_type,
            'fare': fare,
            'total_seats': total_seats,
            'train_number': train_number,
        }
        
        return render(request, 'booking/booking_form.html', context)

    return redirect('myapp-home')


def booking_submit(request):
    if request.method == 'POST':
        try:
            passenger_data = json.loads(request.body)
            print('Raw request body:', passenger_data)
            if passenger_data is not None:
                if passenger_data:
                    passengers = passenger_data.get('passengers', [])
                    for passenger in passengers:
                        Passenger.objects.create(
                            user=request.user,
                            train_number=passenger['train_number'],
                            ticket_type=passenger['ticket_type'],
                            fare=passenger['ticket_fare'],
                            passenger_first_name=passenger['name'],
                            passenger_age=passenger['age'],
                        )
                    return JsonResponse({'success': True})
                else:
                    return JsonResponse({'success': False, 'message': 'No passengers provided.'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid JSON data.'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


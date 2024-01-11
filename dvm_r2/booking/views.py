from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Passenger
from myapp.models import Train
import json
from django.db import transaction
from django.db.models import F
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.


@login_required
def booking_form(request):
    if request.method == "POST":
        ticket_type = request.POST.get("ticket_type")
        fare = request.POST.get("fare")
        total_seats = request.POST.get("total_tickets")
        train_number = request.POST.get("train_number")
        travel_date = request.POST.get("travel_date")

        context = {
            "ticket_type": ticket_type,
            "fare": fare,
            "total_seats": total_seats,
            "train_number": train_number,
            "travel_date": travel_date
        }

        return render(request, "booking/booking_form.html", context)

    return redirect("myapp-home")


@login_required
def booking_submit(request):
    if request.method == "POST":
        try:
            passenger_data = json.loads(request.body)
            if passenger_data is not None:
                if passenger_data:
                    passengers = passenger_data.get("passengers", [])
                    total_fare = 0
                    total_tickets = len(passengers)
                    train_number = passengers[0]["train_number"]
                    ticket_type = passengers[0]["ticket_type"]
                    travel_date = passengers[0]["travel_date"]

                    available_seats = get_available_seats(train_number, ticket_type)
                    if available_seats < total_tickets:
                        return JsonResponse(
                            {"success": False, "message": "Not enough available seats."}
                        )

                    for passenger in passengers:
                        total_fare += passenger['ticket_fare']
                    user_profile = request.user.profile
                    if user_profile.wallet_balance >= total_fare:
                        with transaction.atomic():
                            for passenger in passengers:
                                Passenger.objects.create(
                                    user=request.user,
                                    train_number=passenger["train_number"],
                                    ticket_type=passenger["ticket_type"],
                                    fare=passenger["ticket_fare"],
                                    passenger_first_name=passenger["name"],
                                    passenger_age=passenger["age"],
                                    travel_date = travel_date,
                                    
                                )

                            update_available_seats(train_number, ticket_type, total_tickets)

                            user_profile.wallet_balance -= total_fare
                            user_profile.save()
                            send_booking_confirmation_email(request.user.email,passengers,travel_date)

                    return JsonResponse({"success": True})
                else:
                    return JsonResponse(
                        {"success": False, "message": "No passengers provided."}
                    )
            else:
                return JsonResponse({"success": False, "message": "Invalid JSON data."})

        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    return JsonResponse({"success": False, "message": "Invalid request method."})

def get_available_seats(train_number, ticket_type):
    train = get_object_or_404(Train, train_number=train_number)
    if ticket_type == "1AC":
        return train.total_seats_1ac
    elif ticket_type == "2AC":
        return train.total_seats_2ac
    elif ticket_type == "3AC":
        return train.total_seats_3ac
    else:
        return 0

def update_available_seats(train_number, ticket_type, booked_seats):
    if ticket_type == "1AC":
        Train.objects.filter(
            train_number=train_number
        ).update(total_seats_1ac=F("total_seats_1ac") - booked_seats)
    elif ticket_type == "2AC":
        Train.objects.filter(
            train_number=train_number
        ).update(total_seats_2ac=F("total_seats_2ac") - booked_seats)
    elif ticket_type == "3AC":
        Train.objects.filter(
            train_number=train_number
        ).update(total_seats_3ac=F("total_seats_3ac") - booked_seats)

@login_required
def edit_passenger(request, booking_id):
    passenger = get_object_or_404(Passenger, id=booking_id, user=request.user)

    if request.method == 'POST':
        try:
            passenger_info = json.loads(request.body)
            new_name = passenger_info.get('newName')
            new_age = passenger_info.get('newAge')

            passenger.passenger_first_name = new_name
            passenger.passenger_age = new_age
            passenger.save()

            return JsonResponse({'success': True, 'message': 'Passenger information updated successfully.'})

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})
@login_required
def my_tickets(request):
    bookings = Passenger.objects.filter(user=request.user)
    context = {"bookings": bookings}
    return render(request, "booking/mytickets.html", context)

def send_booking_confirmation_email(user_email,passengers,travel_date):
    subject = 'Booking Confirmation'
    message = render_to_string('booking/booking_confirmation_email.html', {'passengers':passengers,'travel_date':travel_date})
    plain_message = strip_tags(message)
    from_email = "ayushguptadev1@gmail.com"
    recipient_list = [user_email]
    send_mail(subject,plain_message,from_email,recipient_list,html_message=message)

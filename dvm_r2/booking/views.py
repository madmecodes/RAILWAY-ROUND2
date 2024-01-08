from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Passenger
from myapp.models import Train
import json
from django.db import transaction
from django.db.models import F

# Create your views here.


@login_required
def booking_form(request):
    if request.method == "POST":
        ticket_type = request.POST.get("ticket_type")
        fare = request.POST.get("fare")
        total_seats = request.POST.get("total_tickets")
        train_number = request.POST.get("train_number")

        context = {
            "ticket_type": ticket_type,
            "fare": fare,
            "total_seats": total_seats,
            "train_number": train_number,
        }

        return render(request, "booking/booking_form.html", context)

    return redirect("myapp-home")


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
                    print(train_number,ticket_type)
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
                                )
                            print(passengers[0]["ticket_type"])
                            if ticket_type== "1AC":
                                Train.objects.filter(
                                    train_number=train_number
                                ).update(total_seats_1ac=F("total_seats_1ac") - total_tickets)
                            elif ticket_type== "2AC":
                                Train.objects.filter(
                                    train_number=train_number
                                ).update(total_seats_2ac=F("total_seats_2ac") - total_tickets)
                            elif ticket_type== "3AC":
                                Train.objects.filter(
                                    train_number=train_number
                                ).update(total_seats_3ac=F("total_seats_3ac") - total_tickets)
                            user_profile.wallet_balance -= total_fare
                            user_profile.save()
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


@login_required
def my_tickets(request):
    bookings = Passenger.objects.filter(user=request.user)
    context = {"bookings": bookings}
    return render(request, "booking/mytickets.html", context)

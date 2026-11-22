# search.py
# This module handles searching for a parked vehicle
# using its vehicle number.

from parking import validation


def search_vehicle(parking):
    """
    Search for a vehicle by its number and display its details:
    Owner Name, Vehicle Number, Vehicle Type, and Parking Slot.
    """

    vehicle_number = input("Enter Vehicle Number to search: ").upper()

    if validation.is_vehicle_parked(parking, vehicle_number):
        details = parking[vehicle_number]
        print("\nVehicle Found!")
        print("Owner Name     :", details["owner"])
        print("Vehicle Number :", vehicle_number)
        print("Vehicle Type   :", details["type"])
        print("Parking Slot   :", details["slot"])
    else:
        print("\nVehicle not found in the parking area.")

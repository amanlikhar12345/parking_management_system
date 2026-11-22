# validation.py
# This module contains functions to validate user input
# such as checking duplicate vehicle numbers and valid vehicle types.


def is_vehicle_parked(parking, vehicle_number):
    """
    Check if a vehicle number already exists in the parking dictionary.
    Returns True if the vehicle is already parked, otherwise False.
    """
    if vehicle_number in parking:
        return True
    else:
        return False


def is_valid_vehicle_type(vehicle_type):
    """
    Check if the entered vehicle type is one of the allowed types:
    Bike, Car, or Truck (case-insensitive).
    Returns True if valid, otherwise False.
    """
    allowed_types = ["bike", "car", "truck"]

    if vehicle_type.lower() in allowed_types:
        return True
    else:
        return False


def is_valid_vehicle_number(vehicle_number):
    """
    Check that the vehicle number entered by the user is not empty.
    Returns True if valid, otherwise False.
    """
    if vehicle_number.strip() == "":
        return False
    else:
        return True

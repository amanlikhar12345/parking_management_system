# billing.py
# This module handles the calculation of parking charges
# based on the type of vehicle.

# Fixed parking charges (in Rupees) for each vehicle type
PARKING_CHARGES = {
    "bike": 20,
    "car": 50,
    "truck": 100
}


def calculate_charge(vehicle_type):
    """
    Calculate and return the parking fee based on vehicle type.
    The vehicle_type is converted to lowercase to match the
    keys in the PARKING_CHARGES dictionary.
    """
    vehicle_type = vehicle_type.lower()

    if vehicle_type in PARKING_CHARGES:
        return PARKING_CHARGES[vehicle_type]
    else:
        # Default charge in case of an unexpected vehicle type
        return 0

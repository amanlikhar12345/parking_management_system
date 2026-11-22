# remove.py
# This module handles removing a vehicle from the parking area,
# freeing its slot, and showing the parking fee to be paid.

from parking import validation
from parking import billing


def remove_vehicle(parking, available_slots):
    """
    Remove a vehicle from parking:
    1. Take vehicle number as input.
    2. Check if the vehicle exists in the parking dictionary.
    3. Calculate the parking charge based on vehicle type.
    4. Free the slot and remove the vehicle record.
    """

    vehicle_number = input("Enter Vehicle Number to remove: ").upper()

    # Check if the vehicle is actually parked
    if not validation.is_vehicle_parked(parking, vehicle_number):
        print("\nError: Vehicle not found in the parking area.")
        return

    # Get vehicle details before removing
    vehicle_type = parking[vehicle_number]["type"]
    freed_slot = parking[vehicle_number]["slot"]
    owner_name = parking[vehicle_number]["owner"]

    # Calculate the parking charge
    charge = billing.calculate_charge(vehicle_type)

    # Remove the vehicle from the dictionary
    del parking[vehicle_number]

    # Add the freed slot back to the list of available slots
    available_slots.append(freed_slot)

    # Display the bill and confirmation message
    print("\nVehicle Removed Successfully!")
    print("Owner Name     :", owner_name)
    print("Vehicle Number :", vehicle_number)
    print("Vehicle Type   :", vehicle_type)
    print("Freed Slot     :", freed_slot)
    print("Parking Charge : Rs.", charge)

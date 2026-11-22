# park.py
# This module handles parking a new vehicle.
# It takes user input, validates it, assigns a free slot,
# and stores the vehicle details in the parking dictionary.

from parking import validation


def park_vehicle(parking, available_slots):
    """
    Park a new vehicle:
    1. Check if slots are available.
    2. Take owner name, vehicle number, and vehicle type as input.
    3. Validate the input.
    4. Assign the first available slot.
    5. Store the vehicle details in the parking dictionary.
    """

    # Step 1: Check if any slot is available
    if len(available_slots) == 0:
        print("\nSorry! Parking is FULL. No slots available.")
        return

    # Step 2: Take input from the user
    owner_name = input("Enter Owner Name: ")
    vehicle_number = input("Enter Vehicle Number: ").upper()
    vehicle_type = input("Enter Vehicle Type (Bike/Car/Truck): ")

    # Step 3: Validate vehicle number (not empty)
    if not validation.is_valid_vehicle_number(vehicle_number):
        print("\nError: Vehicle number cannot be empty.")
        return

    # Step 4: Check for duplicate vehicle number
    if validation.is_vehicle_parked(parking, vehicle_number):
        print("\nError: This vehicle is already parked.")
        return

    # Step 5: Validate vehicle type
    if not validation.is_valid_vehicle_type(vehicle_type):
        print("\nError: Invalid vehicle type. Choose Bike, Car, or Truck.")
        return

    # Step 6: Assign the first available slot (smallest slot number)
    available_slots.sort()
    assigned_slot = available_slots[0]
    available_slots.remove(assigned_slot)

    # Step 7: Store vehicle details in the parking dictionary
    parking[vehicle_number] = {
        "owner": owner_name,
        "type": vehicle_type.capitalize(),
        "slot": assigned_slot
    }

    # Step 8: Display success message
    print("\nVehicle Parked Successfully!")
    print("Vehicle Number :", vehicle_number)
    print("Assigned Slot  :", assigned_slot)

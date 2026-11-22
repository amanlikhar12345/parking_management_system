# display.py
# This module handles displaying all parked vehicles
# and the current parking status (total, occupied, available slots).


def display_all_vehicles(parking):
    """
    Display details of all currently parked vehicles in a table format.
    """
    if len(parking) == 0:
        print("\nNo vehicles are currently parked.")
        return

    print("\n{:<10}{:<15}{:<15}{:<10}".format("Slot", "Owner", "Vehicle No", "Type"))
    print("-" * 50)

    # Loop through the dictionary and print each vehicle's details
    for vehicle_number in parking:
        details = parking[vehicle_number]
        print("{:<10}{:<15}{:<15}{:<10}".format(
            details["slot"],
            details["owner"],
            vehicle_number,
            details["type"]
        ))


def display_parking_status(parking, available_slots, total_slots):
    """
    Display the total, occupied, and available parking slots.
    """
    occupied = len(parking)
    available = len(available_slots)

    print("\n----- PARKING STATUS -----")
    print("Total Slots     :", total_slots)
    print("Occupied Slots  :", occupied)
    print("Available Slots :", available)

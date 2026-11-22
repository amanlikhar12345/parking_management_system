# main.py
# Entry point of the Parking Management System.
# This file initializes the parking data, shows the menu in a loop,
# and calls the appropriate function based on user choice.

from parking import menu
from parking import park
from parking import remove
from parking import search
from parking import display

# ---------------------------------------------------------
# Shared Data Structures
# ---------------------------------------------------------

# Dictionary to store parked vehicle details
# Format: { "vehicle_number": {"owner": ..., "type": ..., "slot": ...} }
parking = {}

# Total number of slots in the parking area
TOTAL_SLOTS = 10

# List of available (free) parking slots
available_slots = list(range(1, TOTAL_SLOTS + 1))


def main():
    """
    Main function that runs the menu-driven program in a loop
    until the user chooses to exit.
    """
    while True:
        menu.display_menu()
        choice = input("\nEnter your choice: ")

        if choice == "1":
            park.park_vehicle(parking, available_slots)

        elif choice == "2":
            remove.remove_vehicle(parking, available_slots)

        elif choice == "3":
            search.search_vehicle(parking)

        elif choice == "4":
            display.display_all_vehicles(parking)

        elif choice == "5":
            display.display_parking_status(parking, available_slots, TOTAL_SLOTS)

        elif choice == "6":
            print("\nThank you for using the Parking Management System. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")


# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()

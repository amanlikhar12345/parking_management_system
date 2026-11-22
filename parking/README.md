# 🅿️ Parking Management System (Core Python)

## 1. Introduction
A simple, menu-driven **Parking Management System** built using only **Core Python** — no classes, no external libraries, no file handling, and no exception handling. It is designed for beginners to practice functions, modules, packages, dictionaries, lists, loops, and conditional statements.

## 2. Features
- **Park a Vehicle** – enter owner name, vehicle number, and type; auto-assigns the first free slot.
- **Remove Vehicle** – frees the slot and shows the parking fee.
- **Search Vehicle** – find a vehicle's owner, type, and slot by number.
- **Display All Vehicles** – table of all currently parked vehicles.
- **Parking Status** – total, occupied, and available slots.
- **Exit** – quits the program.
- Prevents duplicate vehicle numbers and parking when the lot is full.

## 3. Folder Structure
```
Parking_Management_System/
│
├── main.py
├── README.md
│
└── parking/
    ├── __init__.py
    ├── menu.py
    ├── park.py
    ├── remove.py
    ├── search.py
    ├── display.py
    ├── billing.py
    └── validation.py
```

## 4. Python Concepts Used
| Concept | Where Used |
|---|---|
| Functions | Every module |
| Modules & Packages | `parking/` package, imported in `main.py` |
| Dictionary | `parking` dict stores vehicle records |
| List | `available_slots` list manages free slots |
| Loops (`for`, `while`) | `main()` loop, `display_all_vehicles()` loop |
| Conditionals (`if/elif/else`) | Menu routing, validation checks |
| Basic I/O | `input()` / `print()` throughout |

## 5. Module Explanation
- **`main.py`** – Entry point. Holds the shared `parking` dictionary and `available_slots` list, runs the menu loop, and dispatches user choices to the right module.
- **`parking/menu.py`** – Prints the main menu.
- **`parking/park.py`** – Takes vehicle input, validates it, assigns the lowest-numbered free slot, and stores the record.
- **`parking/remove.py`** – Looks up a vehicle number, calculates its bill, deletes the record, and returns the slot to `available_slots`.
- **`parking/search.py`** – Looks up and prints one vehicle's details.
- **`parking/display.py`** – Prints all parked vehicles in a table and shows slot statistics.
- **`parking/billing.py`** – Holds the `PARKING_CHARGES` dictionary (Bike ₹20, Car ₹50, Truck ₹100) and calculates the fee.
- **`parking/validation.py`** – Checks for duplicate/empty vehicle numbers and valid vehicle types.

## 6. How to Run
1. Make sure Python 3 is installed (`python3 --version`).
2. Open a terminal in the `Parking_Management_System` folder.
3. Run:
   ```
   python3 main.py
   ```
4. Follow the on-screen menu (enter a number 1–6).

## 7. Sample Output
```
==================================
      PARKING MANAGEMENT SYSTEM
==================================
1. Park Vehicle
2. Remove Vehicle
3. Search Vehicle
4. Display All Vehicles
5. Parking Status
6. Exit

Enter your choice: 1
Enter Owner Name: Aman
Enter Vehicle Number: MP09AB1234
Enter Vehicle Type (Bike/Car/Truck): Car

Vehicle Parked Successfully!
Vehicle Number : MP09AB1234
Assigned Slot  : 1
```
```
Enter your choice: 2
Enter Vehicle Number to remove: MP09AB1234

Vehicle Removed Successfully!
Owner Name     : Aman
Vehicle Number : MP09AB1234
Vehicle Type   : Car
Freed Slot     : 1
Parking Charge : Rs. 50
```

## 8. Future Improvements
- Add file/database storage so data isn't lost when the program closes.
- Add time-based billing (charge by duration, not a flat rate).
- Add exception handling for invalid inputs.
- Convert to an OOP design with classes for Vehicle and ParkingLot.
- Add a GUI or web interface.

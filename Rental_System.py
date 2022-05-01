import random
import time
from datetime import datetime
from abc import ABC, abstractmethod
from collections import deque

# PYTHON COLOR CODES TO PRINT FONT OF OWN COLOR CHOICE

color = {
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'DARKCYAN': '\033[36m',
    'BLUE': '\033[94m',
    'GREEN': '\033[92m',
    'YELLOW': '\033[93m',
    'RED': '\033[91m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'END': '\033[0m'
}


# FUNCTION TO DISPLAY PROCESS GOING ON

def process(msg):
    print("\n")
    t = random.randint(2, 6)
    for i in range(t + 1):
        info = '----->> {0:^20} <<-----'.format(msg)
        print_colored(info, "BLUE")
        time.sleep(1)
    print("\n")


# FUNCTION TO PRINT COLORED TEXT
def print_colored(message, msg_color=None):
    print((color['BOLD'] + color[msg_color] + message + color['END']).center(125))


# FUNCTION TO DISPLAY MESSAGE WITH CERTAIN COLOR
def display(message, color):
    print()
    pattern = "********************************************************************"
    print_colored(pattern, color)
    print_colored(message, color)
    print_colored(pattern, color)
    print()


class Vehicle(ABC):
    """
    An abstract class to force its subclass to implement abstract attribute and abstract method
    """

    # ABSTRACT ATTRIBUTE
    @property
    @abstractmethod
    def vehicle_type(self) -> str:
        raise NotImplementedError

    # ABSTRACT METHOD
    @abstractmethod
    def __str__(self) -> str:
        raise NotImplementedError


# Models being used in the inventory
Electric_Models = {"Maruti Alto": 1500, "Maruti Swift": 2000, "Hyundai Creta": 2500, "Honda City": 3000,
                   "Toyota Fortuner": 4000}
Fuel_Models = {"Mahindra Thar": 300, "Honda Amaze": 500, "Hyundai Verna": 1000}


class Electric_Cars(Vehicle):
    """
   Electric Car class inheriting abstract class Vehicle
    """
    vehicle_type = "Electric Car"

    def __init__(self, number, model):
        """
        Constructor to initializes the fuel_car object with field below
        """
        self.vehicle_number = number
        self.model = model
        self.rent_price = Electric_Models[model]

    def __str__(self):
        """
        Format to print car
        """
        return f'Type : {Electric_Cars.vehicle_type}\tId : {self.vehicle_number}\nModel : {self.model}\tRent_Price : {self.rent_price}'


class Fuel_Cars(Vehicle):
    """
    fuel_car class inheriting abstract class Vehicle
    """
    vehicle_type = "Fuel Car"

    def __init__(self, number, model):
        """
        Constructor to initializes the fuel_car object with field below
        """
        self.vehicle_number = number
        self.model = model
        self.rent_price = Fuel_Models[model]

    def __str__(self):
        """
        Format to print fuel_car
        """
        return f'Type : {Fuel_Cars.vehicle_type}\tId : {self.vehicle_number}\nModel : {self.model}\tRent_Price : {self.rent_price}'


def display_bill(customer, color):
    bill_amount = 0
    days_used = (datetime.now() - customer.rental_time).days
    print_colored("CUSTOMER INVOICE", color)
    pattern = "*******************************************************************************"
    print_colored(pattern, color)
    columns_info = '| {0:^12} | {1:^20} | {2:^12} | {3:^12} |'.format("VEHICLE", "MODEL", "PRICE/DAY", "TOTAL PRICE")
    print_colored(columns_info, color)
    print_colored(pattern, color)
    for vehicle in customer.vehicles:
        vehicle_info = '| {0:^12} | {1:^20} | {2:^12} | {3:^12} |'.format(vehicle.vehicle_type, vehicle.model,
                                                                          vehicle.rent_price,
                                                                          vehicle.rent_price * days_used)
        print_colored(vehicle_info, color)
        bill_amount += (vehicle.rent_price) * days_used
    print_colored(pattern, color)
    print()
    return bill_amount


class Inventory:
    """
    Inventory class to contain list of fuel_car and electric_car
    """

    def __init__(self):
        """
        Constructor to initialize the inventory object with empty sets of vehicles
        """
        # set is used here so, adding and removing complexity is O(1)
        self.fuel = set()
        self.electric_car = set()

    def add_item(self, item):
        """
        Add vehicle item in inventory
        """
        if item.vehicle_type == "Fuel Car":
            self.fuel.add(item)
        else:
            self.electric_car.add(item)

    def del_item(self, item):
        """
        Remove vehicle item from inventory
        """
        if item.vehicle_type == "Fuel Car":
            self.fuel.remove(item)
        else:
            self.electric_car.remove(item)

    def display_stocks(self):
        """
        Display the stocks in the inventory
        """
        display(f"We currently have {len(self.fuel)} Fuel car and {len(self.electric_car)} Electric car", "PURPLE")

    def rent(self, customer, num_of_fuel_car=0, num_of_electric_car=0):
        """
        Rent the vehicles from inventory as requested
        """
        total_fuel_car = len(self.fuel)
        total_electric_car = len(self.electric_car)
        process_status = False
        if total_fuel_car <= 0 and total_electric_car <= 0:
            display("Sorry !, Our Inventory is empty")

        elif num_of_fuel_car > total_fuel_car:
            display("Sorry! We have currently only {} fuel_car available to rent.".format(total_fuel_car), "PURPLE")

        elif num_of_electric_car > total_electric_car:
            display("Sorry! We have currently only {} electric_car available to rent.".format(total_electric_car),
                    "PURPLE")

        else:

            customer.rental_time = datetime(2022,4,29)

            # Iterating over copy bcs the set is changed in the iteration
            for fuel1 in self.fuel.copy():
                if num_of_fuel_car <= 0:
                    break
                num_of_fuel_car -= 1
                self.del_item(fuel1)
                customer.vehicles.append(fuel1)

            for electric1 in self.electric_car.copy():
                if num_of_electric_car <= 0:
                    break
                num_of_electric_car -= 1
                self.del_item(electric1)
                customer.vehicles.append(electric1)


            display("Request completed successully !", "CYAN")
            display("Enjoy the ride , Sir !", "BLUE")
            process_status = True

        return process_status

    def generate_bill(self, customer):
        """
        Display the bill and return the bill
        """
        bill_amt = display_bill(customer, "PURPLE")
        return bill_amt

# Inventory object
shop = Inventory()

# Adding items in the inventory
"""
In case we can read from file or fetch items from database to make it more real , for
simplicity we are adding manually
"""
Electric_car = []
Fuel_car = []
for model in Electric_Models:
    for i in range(5):
        Electric_car.append(Electric_Cars("E" + str(i) + model[0].upper() + model[-1].upper(), model))

for model in Fuel_Models:
    for i in range(5):
        Fuel_car.append(Fuel_Cars("F" + str(i) + model[0].upper() + model[-1].upper(), model))

random.shuffle(Electric_car)
random.shuffle(Fuel_car)

for electric1 in Electric_car:
    shop.add_item(electric1)
for fuel1 in Fuel_car:
    shop.add_item(fuel1)


class Customer:
    def __init__(self, name, aadhar_number):
        """
        Our constructor method which initializes the customer object with field below
        """
        self.name = name
        self.aadhar_number = aadhar_number
        self.vehicles = deque()
        self.rental_time = 0
        self.bill = 0

    def request_vehicle(self):
        """
        Takes a request from the customer for the vehicles to be rented.
        """
        while True:
            num_of_Fuel_cars = input("Enter number of Fuel_cars to be rented ")
            num_of_Electric_cars = input("Enter number of Electric_cars to be rented  ")
            try:
                num_of_Fuel_cars, num_of_Electric_cars = int(num_of_Fuel_cars), int(num_of_Electric_cars)

            except ValueError:
                display("Please enter a integer value", "RED")
                continue

            if num_of_Fuel_cars < 1 or num_of_Electric_cars < 1:
                display("Invalid input , number of vehicles should be greater than zero", "RED")
            else:
                break

        display(f'Customer requested for {num_of_Fuel_cars} Fuel_cars and {num_of_Electric_cars} cars', 'GREEN')
        process("PROCESS GOING ON")
        # Funtion to rent the vehicles requested
        if shop.rent(self, num_of_Fuel_cars, num_of_Electric_cars) == False:
            self.request_vehicle()

    def return_vehicles(self):
        """
        Allows customers to return their vehicles to the rental shop after generating the bill.
        """
        display("Customer wants to return vehicles", "GREEN")
        process("PROCESS GOING ON")
        self.bill = shop.generate_bill(self)
        display(f" Total Amount =  Rs. {self.bill}", "PURPLE")
        for vehicle in self.vehicles.copy():
            if vehicle.vehicle_type == "Fuel_car":
                shop.fuel.add(vehicle)
            else:
                shop.electric_car.add(vehicle)

            self.vehicles.remove(vehicle)
        display("Returned vehicles successfully !", "CYAN")

    def pay_bill(self):
        """
        Pays the bill
        """
        display(f"Payment of Amt Rs. {self.bill} initiated", "CYAN")
        process("Payment on process,wait for seconds")
        display(f"{self.name} with total bill of Rs.{self.bill} has paid successfully", "GREEN")
        self.bill = 0
        display("Thank You Sir, for having service from us!", "BLUE")

    def __str__(self):
        """
        Format to print the customer
        """
        return f'Name : {self.name}\tAadhar Number: {self.aadhar_number}'

from Rental_System import *

while True:
    print_colored("""
    1. Registration of Customer
    2. Stocks in th shop
    3. Request for vehicle
    4. Return of vehicle
    5. Pay bill
    6. Exit
    """, "CYAN")
    choice = int(input("\nHow would you like to use our services\n"))

    if choice == 1:
        str1=input("Name:")
        str2=input("Aadhar Number:")
        c= Customer(str1, str2)
    elif choice == 2:
        shop.display_stocks()
    elif choice == 3:
        c.request_vehicle()

    elif choice == 4:
        c.return_vehicles()

    elif choice == 5:
        c.pay_bill()
    elif choice == 6:
        display("Thank you for using this service ☺","GREEN")
        exit()
    else:
        print("Enter Correct Number")



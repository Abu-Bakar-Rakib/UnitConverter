def convert_units():
    print("Select conversion type:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")

    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print(f"{km} kilometers is equal to {miles} miles.")
    elif choice == '2':
        miles = float(input("Enter miles: "))
        km = miles / 0.621371
        print(f"{miles} miles is equal to {km} kilometers.")
    elif choice == '3':
        celsius = float(input("Enter Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F.")
    elif choice == '4':
        fahrenheit = float(input("Enter Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F is equal to {celsius}°C.")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    convert_units()

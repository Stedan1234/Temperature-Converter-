def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def get_temperature_input():
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            return temperature
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the Temperature Converter!")
    
    while True:
        print("\nChoose the conversion type:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            celsius = get_temperature_input()
            print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius)}°F")

        elif choice == '2':
            fahrenheit = get_temperature_input()
            print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit)}°C")

        elif choice == '3':
            celsius = get_temperature_input()
            print(f"{celsius}°C is equal to {celsius_to_kelvin(celsius)}K")

        elif choice == '4':
            kelvin = get_temperature_input()
            print(f"{kelvin}K is equal to {kelvin_to_celsius(kelvin)}°C")

        elif choice == '5':
            fahrenheit = get_temperature_input()
            print(f"{fahrenheit}°F is equal to {fahrenheit_to_kelvin(fahrenheit)}K")

        elif choice == '6':
            kelvin = get_temperature_input()
            print(f"{kelvin}K is equal to {kelvin_to_fahrenheit(kelvin)}°F")

        elif choice == '7':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 7.")

        # Ask if the user wants to perform another conversion
        repeat = input("\nWould you like to perform another conversion? (yes/no): ").strip().lower()
        if repeat != 'yes':
            print("Thank you for using the Temperature Converter. Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Exiting the program. Goodbye!")
def convert_temperature():
    print("Temperature Converter")
    print("Enter the temperature value and unit (C for Celsius, F for Fahrenheit, K for Kelvin):")
    
    try:
        value = float(input("Temperature Value: "))
        unit = input("Unit (C/F/K): ").strip().upper()
        
        if unit == 'C':
            fahrenheit = (value * 9/5) + 32
            kelvin = value + 273.15
            print(f"{value}°C is equivalent to {fahrenheit:.2f}°F and {kelvin:.2f}K.")
        
        elif unit == 'F':
            celsius = (value - 32) * 5/9
            kelvin = celsius + 273.15
            print(f"{value}°F is equivalent to {celsius:.2f}°C and {kelvin:.2f}K.")
        
        elif unit == 'K':
            celsius = value - 273.15
            fahrenheit = (celsius * 9/5) + 32
            print(f"{value}K is equivalent to {celsius:.2f}°C and {fahrenheit:.2f}°F.")
        
        else:
            print("Invalid unit. Please enter C, F, or K.")
    
    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")


convert_temperature()
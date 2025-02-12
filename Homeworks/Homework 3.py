# Homework 3, Alexander Watts, 2/11/25 
import time
import math

# Problem 1: Projectile Motion (Throwing an Object)
# This function calculates the range of a projectile given initial velocity and launch angle.
def projectile_range(v0: float, theta: float):
    g = 9.81  # Acceleration due to gravity (m/s^2)
    radians = math.radians(theta)  # Convert angle to radians
    R = (v0 ** 2) * math.sin(2 * radians) / g  # Calculate range
    return R

# Problem 2: Efficiency of a Heat Engine
# This function calculates the efficiency of a heat engine given hot and cold reservoir temperatures.
def calculate_efficiency(temperature_hot: float, temperature_cold: float):
    if temperature_hot <= 0 or temperature_cold <= 0:
        raise ValueError("Input temperatures must be positive numbers.")
    
    efficiency = 1 - (temperature_hot / temperature_cold)  # Calculate efficiency
    return efficiency

# Problem 3: Temperature Conversion
# This function converts a given temperature to Fahrenheit, Rankine, Celsius, and Kelvin.
def ConvertTemperature(temperature: str):
    temperature = temperature.lower() + "|"  # Normalize input and add delimiter
    if (any(sub in temperature for sub in ["f|", "c|", "r|", "k|", "fahrenheit|", "celcius|", "rankine|", "kelvin|"])):
        temperatureNumber = float(''.join(i for i in temperature if i.isdigit() or i == '.' or i == '-'))  # Extract numeric value
        
        # Convert to Fahrenheit
        if "f" in temperature:
            fahrenheit = temperatureNumber
        elif "r" in temperature:
            fahrenheit = temperatureNumber - 459.67
        elif "c" in temperature:
            fahrenheit = temperatureNumber * 9 / 5 + 32
        elif "k" in temperature:
            fahrenheit = (temperatureNumber - 273.15) * 9 / 5 + 32

        # Convert to other units
        rankine = fahrenheit + 459.67
        celcius = (fahrenheit - 32) * (5/9)
        kelvin = celcius + 273.15
        fahrenheit = fahrenheit

        return rankine, celcius, kelvin, fahrenheit

# Problem 4: Summation of a Series
# This function calculates the summation of the harmonic series up to the nth term.
def summation_of_series(n: int):
    if n <= 0:
        return 0
    series_sum = 0
    for i in range(1, n+1):
        series_sum += 1 / i  # Add the reciprocal of each term
    return series_sum

# Main function to run the program
while True:
    # Display menu
    print("┌──────────────────────────────────────────────┐")
    print("│ Select a function to run:                    │")
    print("├───┬──────────────────────────────────────────┤")
    print("│ 1 │ Projectile Motion (Throwing an Object)   │")
    print("│ 2 │ Efficiency of a Heat Engine              │")
    print("│ 3 │ Temperature Conversion                   │")
    print("│ 4 │ Summation of a Series                    │")
    print("│ 5 │ Exit                                     │")
    print("└───┴──────────────────────────────────────────┘")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        # Get inputs and calculate projectile range
        v0 = int(input("Inital Velocity (m/s): "))
        theta = int(input("Launch Angle (Degrees): "))
        print(f"Projectile Range: {projectile_range(v0, theta):.2f}")
        time.sleep(2)
    elif choice == '2':
        # Get inputs and calculate heat engine efficiency
        temperature_hot = float(input("Temperature Hot: "))
        temperature_cold = float(input("Temperature Cold: "))
        efficiency = calculate_efficiency(temperature_hot, temperature_cold)
        print(f"Efficiency of the heat engine: {efficiency:.2f}")
        time.sleep(2)
    elif choice == '3':
        # Convert temperature and display results
        while True:
            temperature = str(input("What is the temperature you would like to convert? (Q to quit)\n"))
            if 'q' in temperature.lower():
                break
            elif temperature == '' or temperature.isdigit() or not any(char.isdigit() for char in temperature):
                print("Please enter a temperature to convert.")
            else:
                rankine, celcius, kelvin, fahrenheit = ConvertTemperature(temperature)
                print(f"Converted Units:\n Fahrenheit: {fahrenheit:.2f}\n Rankine:    {rankine:.2f}\n Celcius:    {celcius:.2f}\n Kelvin:     {kelvin:.2f}")
        time.sleep(2)
    elif choice == '4':
        # Get input and calculate summation of series
        n = int(input("How many itterations: "))
        print(f"The sum of the first {n} terms of the series is: {summation_of_series(n):.3f}")
        time.sleep(2)
    elif choice == '5':
        # Exit the program
        break
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)

#Homework 3, Alexander Watts, 2/10/25 
import time
import math


#Problem 1: Projectile Motion (Throwing an Object)
def projectile_range(v0:float, theta:float):
    g = 9.81
    radians = math.radians(theta)
    R = (v0 ** 2) * math.sin(2 * radians) / g
    return R

#Problem 2: Efficiency of a Heat Engine
def calculate_efficiency(temperature_hot:float, temperature_cold:float):
    if temperature_hot <= 0 or temperature_cold <= 0:
        raise ValueError("Input temperatures must be positive numbers.")

    efficiency = 1 - (temperature_hot / temperature_cold)

    return efficiency

#Problem 3: Temperature Conversion
def ConvertTemperature(temperature:str):
    temperature = temperature.lower() + "|"
    if (any(sub in temperature for sub in ["f|","c|","r|","k|","fahrenheit|","celcius|","rankine|","kelvin|"])):

        temperatureNumber = float(''.join(i for i in temperature if i.isdigit() or i == '.' or i == '-'))
        
        if "f" in temperature:
            fahrenheit = temperatureNumber
        elif "r" in temperature:
            fahrenheit = temperatureNumber - 459.67
        elif "c" in temperature:
            fahrenheit = temperatureNumber * 9 / 5 + 32
        elif "k" in temperature:
            fahrenheit = (temperatureNumber - 273.15) * 9 / 5 + 32

        rankine     = fahrenheit + 459.67
        celcius     = (fahrenheit - 32) * (5/9)
        kelvin      = celcius + 273.15
        fahrenheit  = fahrenheit

        return rankine, celcius, kelvin, fahrenheit

#Problem 4: Summation of a Series
def summation_of_series(n:int):
    if n <= 0:
        return 0
    series_sum = 0
    for i in range(1, n+1):
        series_sum += 1 / i
    return series_sum



# Main function to run the program
while True:
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
        v0 = int(input("Inital Velocity (m/s): "))
        theta = int(input("Launch Angle (Degrees): "))
        print(f"Projectile Range: {projectile_range(v0, theta):.2f}")
        time.sleep(2)
    elif choice == '2':
        temperature_hot = float(input("Temperature Hot: "))
        temperature_cold = float(input("Temperature Cold: "))

        efficiency = calculate_efficiency(temperature_hot, temperature_cold)
        print(f"Efficiency of the heat engine: {efficiency:.2f}")
        time.sleep(2)
    elif choice == '3':
        while True:
            temperature = input("What is the temperature you would like to convert? (Q to quit)\n")
            if str(temperature) == 'q':
                break
            else:
                rankine, celcius, kelvin, fahrenheit = ConvertTemperature(temperature)
                print(f"Converted Units:\n Fahrenheit: {fahrenheit:.2f}\n Rank1ine:    {rankine:.2f}\n Celcius:    {celcius:.2f}\n Kelvin:     {kelvin:.2f}")
        time.sleep(2)
    elif choice == '4':
        n = int(input("How many itterations: "))
        print(f"The sum of the first {n} terms of the series is: {summation_of_series(n):.3f}")
        time.sleep(2)
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)

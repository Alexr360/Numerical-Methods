import math

def flow_rate():
    while True:
        d = float(input("Enter pipe diameter (m): "))
        l = float(input("Enter pipe length (m): "))
        mu = float(input("Enter fluid viscosity (Pa·s): "))
        
        p1 = float(input("Enter inlet pressure (Pa): "))
        p2 = float(input("Enter outlet pressure (Pa): "))

        if p1 <= p2:
            print("Inlet pressure must be greater than outlet pressure!")
            continue

        r = d / 2
        q = (math.pi * (r**4) * (p1 - p2)) / (8 * mu * l)

        print(f"Flow rate: {q:.6e} m³/s")

        if input("Calculate another case? (y/n): ").lower() != 'y':
            break

flow_rate()

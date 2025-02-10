#Homework 1, Alexander Watts, 2/3/25 
import math
import time

#Question 1: Function to calculate the surface area and volume of a cylinder
def calculate_cylinder_properties(r:float, h:float):
    # Calculate surface area and volume
    surface_area = 2 * math.pi * r * h + 2 * math.pi * r**2
    volume = math.pi * r**2 * h
    
    return surface_area, volume


#Question 2: Function to calculate the maximum deflection of a beam
def calculate_max_deflection(F:float, L:float, E:float, I:float):
    return (F * L**3) / (48 * E * I)


#Question 3: Function to convert speed from m/s to km/h and mph
def convert_speed(speed_mps: float):
    # Conversion factors
    MPS_TO_KMPH = 3.6  # 1 m/s = 3.6 km/h
    MPS_TO_MPH = 2.23694  # 1 m/s = 2.23694 mph
    
    # Convert to km/h and mph
    speed_kmph = speed_mps * MPS_TO_KMPH
    speed_mph = speed_mps * MPS_TO_MPH

    return speed_kmph, speed_mph


#Question 4: Function to solve a quadratic equation
def solve_quadratic(a: float, b: float, c: float):
    # Print the quadratic equation
    print(f"The quadratic equation is: {a}x^2 + {b}x + {c} = 0")
    
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check the number of roots and compute them
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"The equation has two real roots: {root1} and {root2}")
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"The equation has one real root: {root}")
        return root,
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        print(f"The equation has complex roots: {real_part} ± {imaginary_part}i")
        return real_part, imaginary_part


#Question 5: Function to classify flow based on Reynolds number
def classify_flow(density: float, viscosity: float, diameter: float, velocity: float):
    # Compute Reynolds number
    Re = (density * velocity * diameter) / viscosity

    # Classify the flow
    if Re < 2000:
        flow_type = "Laminar Flow"
    elif 2000 <= Re <= 4000:
        flow_type = "Transitional Flow"
    else:
        flow_type = "Turbulent Flow"

    return Re, flow_type


#Question 6: Function to calculate gear ratio and classify efficiency
def gear_ratio_efficiency(input_teeth: int, output_teeth: int):
    # Compute gear ratio
    gear_ratio = output_teeth / input_teeth

    # Classify efficiency
    if gear_ratio < 3:
        efficiency = "High Efficiency"
    elif 3 <= gear_ratio <= 5:
        efficiency = "Moderate Efficiency"
    else:
        efficiency = "Low Efficiency"

    return gear_ratio, efficiency

# Main function to run the program
def main():
    while True:
        time.sleep(2)

        # Display menu options
        print("\nSelect a function to run:")
        print("1. Calculate Cylinder Properties")
        print("2. Calculate Maximum Deflection")
        print("3. Convert Speed")
        print("4. Solve Quadratic Equation")
        print("5. Classify Flow")
        print("6. Gear Ratio Efficiency")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            # Get input for cylinder properties calculation
            r = float(input("Enter the radius of the cylinder: "))
            h = float(input("Enter the height of the cylinder: "))
            surface_area, volume = calculate_cylinder_properties(r, h)
            print(f"Surface Area: {surface_area:.2f}")
            print(f"Volume: {volume:.2f}")
        elif choice == '2':
            # Get input for maximum deflection calculation
            F = float(input("Enter the applied force (N): "))
            L = float(input("Enter the beam length (m): "))
            E = float(input("Enter the modulus of elasticity (Pa): "))
            I = float(input("Enter the moment of inertia (m^4): "))
            delta_max = calculate_max_deflection(F, L, E, I)
            print(f"Maximum Deflection: {delta_max:.6f} meters")
        elif choice == '3':
            # Get input for speed conversion
            speed_mps = float(input("Enter speed in meters per second (m/s): "))
            speed_kmph, speed_mph = convert_speed(speed_mps)
            print(f"Speed in kilometers per hour: {speed_kmph:.2f} km/h")
            print(f"Speed in miles per hour: {speed_mph:.2f} mph")
        elif choice == '4':
            # Get input for solving quadratic equation
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            solve_quadratic(a, b, c)
        elif choice == '5':
            # Get input for flow classification
            density = float(input("Enter the fluid density (kg/m³): "))
            viscosity = float(input("Enter the dynamic viscosity (Pa·s or N·s/m²): "))
            diameter = float(input("Enter the pipe diameter (m): "))
            velocity = float(input("Enter the fluid velocity (m/s): "))
            Re, flow_type = classify_flow(density, viscosity, diameter, velocity)
            print(f"Reynolds Number: {Re:.2f}")
            print(f"Flow Type: {flow_type}")
        elif choice == '6':
            # Get input for gear ratio efficiency calculation
            input_teeth = int(input("Enter the number of teeth on the input gear: "))
            output_teeth = int(input("Enter the number of teeth on the output gear: "))
            gear_ratio, efficiency = gear_ratio_efficiency(input_teeth, output_teeth)
            print(f"Gear Ratio: {gear_ratio:.2f}")
            print(f"Efficiency Level: {efficiency}")
        elif choice == '7':
            # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
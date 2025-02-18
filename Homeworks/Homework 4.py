import math
import time
import numpy as np

# Problem 1: For Loop - Beam Deflection Calculation
def calculate_deflection(q, L, E, I):
    deflection = []
    for i in range(11):  # 10 equally spaced points plus the start point
        x = i * L / 10
        y = (q * x * (L**3 - 2 * L * x**2 + x**3)) / (24 * E * I)
        deflection.append((x, y))
    return deflection

# Problem 2: While Loop - Convergence of a Numerical Solution
def newtons_cooling(T0, T_inf, k):
    Tn = T0
    iterations = 0
    
    while abs(Tn - T_inf) >= 0.01:
        Tn = Tn - k * (Tn - T_inf)
        iterations += 1
    
    return iterations

# Problem 3: Nested Loop - Stress Distribution in a Plate
def stress_distribution(L, W, k):
    # Determine the step size for x and y directions
    x_step = L / 4
    y_step = W / 4

    # Initialize a 2D array to store stress values along with their positions
    stress_array = []

    # Nested loops to compute stress at each grid point
    for i in range(5):
        row = []
        for j in range(5):
            x = i * x_step
            y = j * y_step
            stress = k * (x**2 + y**2)
            row.append((x, y, stress))
        stress_array.append(row)

    return stress_array

# Problem 4: Matrix Operations in Structural Analysis
def structural_analysis():
    # Define the stiffness matrix K
    K = np.array([[12, -6],[-6, 4]])

    # Define the force vector F
    F = np.array([10, 4])

    # Compute the displacement vector U
    U = np.linalg.inv(K).dot(F)
    return U

# Problem 5: Data Analysis of Temperature Measurements
TC = np.array([23.5, 24.1, 22.8, 25.0, 23.9, 24.5, 22.7, 24.8, 23.6, 25.2])

def data_analysis_temperature_measurements(TC):
    mean = np.mean(TC)
    standard_deviation = np.std(TC)
    TF = (9/5) * TC + 32
    MaxF = TF.max()
    MinF = TF.min()
    MaxC = TC.max()
    MinC = TC.min()
    return mean, standard_deviation, TF, MaxF, MinF, MaxC, MinC


# Main function to run the program
while True:
    # Display menu
    print("┌──────────────────────────────────────────────────────┐")
    print("│ Select one of the following functions to run:        │")
    print("├───┬──────────────────────────────────────────────────┤")
    print("│ 1 │ For Loop - Beam Deflection Calculation           │")
    print("│ 2 │ While Loop - Convergence of a Numerical Solution │")
    print("│ 3 │ Nested Loop - Stress Distribution in a Plate     │")
    print("│ 4 │ Matrix Operations in Structural Analysis         │")
    print("│ 5 │ Data Analysis of Temperature Measurements        │")
    print("│ 6 │ Exit                                             │")
    print("└───┴──────────────────────────────────────────────────┘")
    
    choice = input("Enter your choice (1-5): ")

    print("\n")

    if choice == '1':
        # Input from user
        q = float(input("Enter the load per unit length (N/m): "))
        L = float(input("Enter the beam length (m): "))
        E = float(input("Enter Young’s modulus (Pa): "))
        I = float(input("Enter the moment of inertia (m^4): "))

        # Calculate deflection
        deflection = calculate_deflection(q, L, E, I)

        # Output the deflection at 10 points
        print("Deflection at 10 equally spaced points along the beam:")
        for x, y in deflection:
            print(f"x = {x:.2f} m, y = {y:.6f} m")
        input("┌──────────────────────────────────────────────┐\n│ Press [Enter] when you are ready to continue │\n└──────────────────────────────────────────────┘")
    elif choice == '2':
        # Input from user
        T0 = float(input("Enter the initial temperature (T0): "))
        T_inf = float(input("Enter the ambient temperature (T∞): "))
        k = float(input("Enter the cooling constant (k): "))

        # Calculate number of iterations needed
        iterations = newtons_cooling(T0, T_inf, k)

        # Output the number of iterations
        print(f"The number of iterations needed: {iterations}")
        input("┌──────────────────────────────────────────────┐\n│ Press [Enter] when you are ready to continue │\n└──────────────────────────────────────────────┘")
    elif choice == '3':
        L = float(input("Enter the length of the plate (L): "))
        W = float(input("Enter the width of the plate (W): "))
        k = float(input("Enter the constant k: "))
        stress_array = stress_distribution(L, W, k)

        # Print the stress array with positions
        for row in stress_array:
            for (x, y, stress) in row:
                print(f"Position ({x:.2f}, {y:.2f}): Stress = {stress:.2f}")
        input("┌──────────────────────────────────────────────┐\n│ Press [Enter] when you are ready to continue │\n└──────────────────────────────────────────────┘")
    elif choice == '4':
        U = structural_analysis()

        np.set_printoptions(
            threshold=np.inf,
            linewidth=200,
            precision=4,
            suppress=True
        )
        
        print("The displacement vector U is:", U)

        input("┌──────────────────────────────────────────────┐\n│ Press [Enter] when you are ready to continue │\n└──────────────────────────────────────────────┘")
    elif choice == '5':
        mean, standard_deviation, TF, MaxF, MinF, MaxC, MinC = data_analysis_temperature_measurements(TC)

        print(f"Mean (Celsius): {mean:.2f} \nStandard Deviation (Celsius): {standard_deviation:.2f} \nTemperatures (Fahrenheit): {TF} \nMax Temperature (Fahrenheit): {MaxF:.2f} \n Min Temperature (Fahrenheit): {MinF:.2f} \nMax Temperature (Celsius): {MaxC:.2f} \nMin Temperature (Celsius): {MinC:.2f}")
        input("┌──────────────────────────────────────────────┐\n│ Press [Enter] when you are ready to continue │\n└──────────────────────────────────────────────┘")
    elif choice == '6':
        # Exit the program
        break
    else:
        print("┌──────────────────────────────────┐\n│ Invalid Choice Please Try Again  │\n└──────────────────────────────────┘")
        time.sleep(2)

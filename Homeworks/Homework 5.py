import math
import time
import numpy as np

import matplotlib.pyplot as plt

# Problem 1: Computing the Moment of Inertia of a Beam Section
def MomentOfInertiaOfBeam(b, h):
    # Calculate the moment of inertia using the formula
    I = (b * h**3) / 12
    return I

# Problem 2: Solving an Axial Load Problem in a Truss
def SolveAxialLoadProblem():
    # Define the coefficient matrix
    A = np.array([[3, 2, -1],
                  [-2, 5, 3],
                  [4, -3, 2]])

    # Define the constant matrix
    B = np.array([1000, 500, 200])

    # Solve the system of equations
    F = np.linalg.solve(A, B)

    return F

# Problem 3: Visualizing a Projectile Motion
def ComputeProjectileTrajectory(v0, theta):
    g = 9.81
    t = np.linspace(0, 2 * v0 * np.sin(theta) / g, 100)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t**2
    return x, y

# Problem 4: Analyzing Heat Transfer in a Fin
def ComputeTemperatureDistribution():
    L = 0.1
    T0 = 150
    T_inf = 25
    m = 5

    x = np.linspace(0, L, 10)
    T = T_inf + (T0 - T_inf) * np.exp(-m * x)

    return x, T

# Problem 5: Computing the Stress in a Rotating Disc
def ComputeRadialStress():
    rho = 7800
    omega = 1000
    nu = 0.3
    R = 0.2

    r = np.linspace(0, R, 10)
    sigma_r = (rho * omega**2 / 8) * (3 + nu - (1 + nu) * r**2 / R**2) * R**2

    return r, sigma_r

# Main function to run the program
while True:
    # Display menu
    print("┌───────────────────────────────────────────────────────┐")
    print("│ Select one of the following functions to run:         │")
    print("├───┬───────────────────────────────────────────────────┤")
    print("│ 1 │ Computing the Moment of Inertia of a Beam Section │")
    print("│ 2 │ Solving an Axial Load Problem in a Truss          │")
    print("│ 3 │ Visualizing a Projectile Motion                   │")
    print("│ 4 │ Analyzing Heat Transfer in a Fin                  │")
    print("│ 5 │ Computing the Stress in a Rotating Disc           │")
    print("│ 6 │ Exit                                              │")
    print("└───┴───────────────────────────────────────────────────┘")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        # Problem 1: Computing the Moment of Inertia of a Beam Section
        I = MomentOfInertiaOfBeam(0.2, 0.3)
        print(f"The moment of inertia of the beam section is: {I:.5f}")

        input("┌──────────────────────────────────────────────┐\n│ Press [Enter] when you are ready to continue │\n└──────────────────────────────────────────────┘")
    elif choice == '2':
        # Problem 2: Solving an Axial Load Problem in a Truss
        F = SolveAxialLoadProblem()
        print(f"The forces in the truss members are: {F}")

        input("┌──────────────────────────────────────────────┐\n│ Press [Enter] when you are ready to continue │\n└──────────────────────────────────────────────┘")
    elif choice == '3':
        # Problem 3: Visualizing a Projectile Motion
        x, y = ComputeProjectileTrajectory(50, np.deg2rad(45))

        # Plot the trajectory of the projectile
        plt.plot(x, y)
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title('Projectile Trajectory')
        plt.grid(True)
        print("     ┌───────────────────────────────────────────┐\n     │ Displaying Graph of Projectile Trajectory │\n     │         Close Figure to Continue!         │\n     └───────────────────────────────────────────┘")
        plt.show()
    elif choice == '4':
        # Problem 4: Analyzing Heat Transfer in a Fin
        x, T = ComputeTemperatureDistribution()

        # Plot the temperature distribution
        plt.plot(x, T)
        plt.xlabel('Position along the fin (m)')
        plt.ylabel('Temperature (°C)')
        plt.title('Temperature Distribution along the Fin')
        plt.grid(True)
        print("     ┌──────────────────────────────────────────────┐\n     │ Displaying Graph of Temperature Distribution │\n     │           Close Figure to Continue           │\n     └──────────────────────────────────────────────┘")
        plt.show()
    elif choice == '5':
        # Problem 5: Computing the Stress in a Rotating Disc
        r, sigma_r = ComputeRadialStress()

        # Plot the radial stress vs r
        plt.plot(r, sigma_r)
        plt.xlabel('r (m)')
        plt.ylabel('Radial Stress (Pa)')
        plt.title('Radial Stress vs r')
        plt.grid(True)
        print("     ┌───────────────────────────────────┐\n     │ Displaying Graph of Radial Stress │\n     │       Close Figure to Continue    │\n     └───────────────────────────────────┘")
        plt.show()
    elif choice == '6':
        # Exit the program
        break
    else:
        print("┌──────────────────────────────────┐\n│ Invalid Choice Please Try Again  │\n└──────────────────────────────────┘")
        time.sleep(2)

def beam_deflection():
    while True:
        l = float(input("Enter beam length (m): "))
        f = float(input("Enter applied force (N): "))
        x = float(input("Enter position along the beam (m): "))
        e = float(input("Enter modulus of elasticity (Pa): "))
        i = float(input("Enter moment of inertia (m^4): "))

        if x > l:
            print("Position cannot be greater than beam length.")
            continue

        delta = (f * x**2 * (3*l - x)) / (6 * e * i)
        print(f"Deflection at {x}m: {delta:.6e} m")

        if input("Calculate again? (y/n): ").lower() != 'y':
            break

beam_deflection()

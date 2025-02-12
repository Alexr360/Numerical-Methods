def beam_deflection():
    l = float(input("Enter beam length (m): "))
    f = float(input("Enter applied force (N): "))
    x = float(input("Enter position along the beam (m): "))
    e = float(input("Enter modulus of elasticity (Pa): "))
    i = float(input("Enter moment of inertia (m^4): "))


    if x < l:
        delta = (f * x**2 * (3*l - x)) / (6 * e * i)
        return delta


while True:
    delta = beam_deflection()
    
    try:
        print(f"Deflection at {x}m: {delta:.6e} m")
    except:
        print("Position cannot be greater than beam length.")

    if input("Calculate again? (y/n): ").lower() != 'y':
        break
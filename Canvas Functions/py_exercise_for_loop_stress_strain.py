E = 200e9  # Young’s Modulus (Pa)
strains = [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]

for strain in strains:
    stress = E * strain
    print(f"Strain: {strain:.5f}, Stress: {stress/1e6:.2f} MPa")

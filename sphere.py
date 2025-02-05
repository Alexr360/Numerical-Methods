import math

radi = [5,7,3,4,5,8]

# Calculate surface area and volume
def calculate_cylinder_properties(radius_list):
    radius_list = list(radius_list)
    surface_area = [4 * math.pi * r**2 for r in radius_list]
    volume = [4 / 3 * math.pi * r**3 for r in radius_list]
    data = [surface_area, volume]
    return data

surface_area, volume = calculate_cylinder_properties(radi)
i=0
for r in radi:
    print(f"Radius:{r:.2f}, Surface Area:{surface_area[i]:.2f}, Volume:{volume[i]:.2f}")
    i=i+1
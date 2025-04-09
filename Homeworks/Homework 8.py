import numpy as np
import matplotlib.pyplot as plt

def ans_box(config):
    if not config or not isinstance(config, list):
        return
    
    # Extract content from config
    content = [line['text'] for line in config]
    
    # Calculate maximum content width
    content_width = max(len(line) for line in content)
    
    # Create dynamic borders
    horizontal_border = "─" * (content_width + 2)
    top_border = f"┌{horizontal_border}┐"
    bottom_border = f"└{horizontal_border}┘"
    divider = f"├{horizontal_border}┤"
    
    # Print the box
    print(top_border)
    for i, line in enumerate(config):
        text = line['text']
        align = line.get('align', 'left')
        
        # Handle alignment
        if align == 'center':
            padding_left = (content_width - len(text)) // 2
            padding_right = content_width - len(text) - padding_left
        elif align == 'right':
            padding_left = content_width - len(text)
            padding_right = 0
        else:
            padding_left = 0
            padding_right = content_width - len(text)
        
        # Print the line with padding
        print(f"│ {' ' * padding_left}{text}{' ' * padding_right} │")
        
        # Handle dividers based on config
        if line.get('divider', False):
            print(divider)
    print(bottom_border)

# Given data
strain = np.array([0.000, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.007])
stress = np.array([0.00, 85.1, 158.3, 223.4, 280.2, 328.7, 389.0, 401.0])

# Construct the design matrix for cubic regression
A = np.vstack([np.ones_like(strain), strain, strain**2, strain**3]).T

# Solve the normal equations: (A^T A) x = A^T b
coefficients = np.linalg.solve(A.T @ A, A.T @ stress)

# Generate the fitted curve
strain_fit = np.linspace(min(strain), max(strain), 100)
stress_fit = coefficients[0] + coefficients[1] * strain_fit + coefficients[2] * strain_fit**2 + coefficients[3] * strain_fit**3

# Calculate the error values
error = stress - (coefficients[0] + coefficients[1] * strain + coefficients[2] * strain**2 + coefficients[3] * strain**3)

# Plot the original data and fitted curve with error bars
plt.errorbar(strain, stress, yerr=abs(error), fmt='o', color='red', label='Original Data')
plt.plot(strain_fit, stress_fit, color='blue', label='Cubic Fit')
plt.xlabel('Strain')
plt.ylabel('Stress (MPa)')
plt.title('Cubic Fit of Stress-Strain Data')
plt.legend()
plt.grid()

displayError = str('Error Values (MPa): ' + ', '.join(map(lambda x: f'{x:.2f}', error)))
data = [
    {'text': 'Fitted Coefficients:', 'align': 'center', 'divider': True},
    {'text': f"a0 │ {coefficients[0]}"},
    {'text': f"a1 │ {coefficients[1]}"},
    {'text': f"a2 │ {coefficients[2]}"},
    {'text': f"a3 │ {coefficients[3]}", 'divider': True},
    {'text': displayError}
]

ans_box(data)

ans_box([{'text':'Show Graph? (y/n)'}])
if input() == 'y':
    plt.show()

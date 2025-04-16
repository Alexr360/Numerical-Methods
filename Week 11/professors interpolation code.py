import matplotlib.pyplot as plt

x = [1, 2, 4, 5]  # Example x values
y = [2, 4, 8, 10]  # Example y values

xinterp = 3
yinterp = 0

for i in range(len(x)):
    Li = 1
    for j in range(len(x)):
        if i != j:
            Li = Li * (xinterp - x[j]) / (x[i] - x[j])
    yinterp += Li * y[i]

plt.plot(x, y, 'o', label='Data Points')
plt.plot(xinterp, yinterp, 'ro', label='Interpolated Point')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
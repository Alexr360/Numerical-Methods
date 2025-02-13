import numpy as np

def summation_of_series(n: int):
    if n <= 0:
        return 0
    series_sum = 0
    for i in range(1, n+1):
        series_sum += 1 / i**2
    return series_sum


# Get input and calculate summation of series
n = int(input("How many itterations: "))

print(f"The sum of the first {n} terms of the series is: {summation_of_series(n)},  Exact value is {(np.pi)**2/6}")
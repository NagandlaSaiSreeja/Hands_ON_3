import timeit
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(size):
    x = 1
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            x += 1

# Given size values
size_values = [1, 6, 15, 25, 34, 56, 75, 90, 120, 250, 320, 600, 1010, 3050, 4400]

# Measure execution time
timing_results = []
for size in size_values:
    elapsed_time = timeit.timeit(lambda: f(size), number=1)
    timing_results.append(elapsed_time)

# Fit a polynomial curve (quadratic) to the data
polynomial_coeffs = np.polyfit(size_values, timing_results, 2)
polynomial_model = np.poly1d(polynomial_coeffs)

# Identify n_0 (where data deviates from the polynomial trend)
residuals = np.array(timing_results) - polynomial_model(size_values)
threshold = np.mean(residuals) + 2 * np.std(residuals)  # Outlier detection threshold

# Find n_0 candidates (where timing deviates significantly)
n_0_candidates = [size_values[i] for i in range(len(size_values)) if abs(residuals[i]) > threshold]

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(size_values, timing_results, label='Measured Time', marker='x', color='orange')
plt.plot(size_values, polynomial_model(size_values), label='Polynomial ', marker='o', color='red')

# Highlight n_0 candidates on the plot
for n_0 in n_0_candidates:
    plt.axvline(x=n_0, linestyle='dotted', color='green', alpha=0.7)
    plt.text(n_0, polynomial_model(n_0), f'n_0={n_0}', fontsize=10, verticalalignment='bottom', horizontalalignment='right', color='blue')

plt.xlabel('Size of (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Zoomed-In Execution Time vs Input Size for f(n)')
plt.legend()
plt.grid(True)
plt.show()

# Print the approximate values of n_0
print("Approximate values of n_0 (where deviations occur):",n_0_candidates)

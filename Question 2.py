import timeit
import matplotlib.pyplot as plt
import numpy as np

def f(size):
 x = 1
 for i in range(1, size + 1):
  for j in range(1, size + 1):
   x += 1

size_values = [1, 6, 15, 25, 34, 56, 75, 90, 120, 250, 320, 600, 1010, 3050, 4400]
timing_results = []
for size in size_values:
    elapsed_time = timeit.timeit(lambda: f(size), number=1)
    timing_results.append(elapsed_time)

polynomial_coeffs = np.polyfit(size_values, timing_results, 2)
polynomial_model = np.poly1d(polynomial_coeffs)


plt.figure(figsize=(10, 6))
plt.plot(size_values, timing_results, label='measured time', marker='x', color='orange')
plt.plot(size_values, polynomial_model(size_values), label='polynomial (Degree 2)', marker='o', color='red')
plt.xlabel('input size of (n)')
plt.ylabel('execution time in (seconds)')
plt.title('execution time vs input size for Function f(size)')
plt.legend()
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Define allometric functions
def allometric_function(x, k, b):
    return k * x ** b

# Print the equations for different values of k and b
parameters = [(1, 2), (1, 0.5), (2, 3), (0.5, -1)]  # (k, b) pairs
print("Allometric Functions:")
for k, b in parameters:
    print(f"Allometric Function Equation: y = {k} * x^{b}")

# Generate x values for allometric functions (domain: (0, ∞))
x_vals = np.linspace(0.01, 10, 500)  # Starting just above 0 to avoid issues with x=0

# Create plots
plt.figure(figsize=(15, 5))

# Plot for k = 1, b = 2 (y = 1 * x^2)
plt.subplot(1, 4, 1)
plt.plot(x_vals, allometric_function(x_vals, 1, 2), label='y = 1 * x^2', color='b')
plt.title('Allometric Function: y = 1 * x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot for k = 1, b = 0.5 (y = 1 * x^(1/2))
plt.subplot(1, 4, 2)
plt.plot(x_vals, allometric_function(x_vals, 1, 0.5), label='y = 1 * x^(1/2)', color='g')
plt.title('Allometric Function: y = 1 * x^(1/2)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot for k = 2, b = 3 (y = 2 * x^3)
plt.subplot(1, 4, 3)
plt.plot(x_vals, allometric_function(x_vals, 2, 3), label='y = 2 * x^3', color='orange')
plt.title('Allometric Function: y = 2 * x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Plot for k = 0.5, b = -1 (y = 0.5 * x^(-1))
plt.subplot(1, 4, 4)
plt.plot(x_vals, allometric_function(x_vals, 0.5, -1), label='y = 0.5 * x^(-1)', color='purple')
plt.title('Allometric Function: y = 0.5 * x^(-1)')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()

# Display the plots
plt.tight_layout()
plt.show()

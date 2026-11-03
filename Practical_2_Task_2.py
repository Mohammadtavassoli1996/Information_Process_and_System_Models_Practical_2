import numpy as np

# Coefficients of the equations
A = [
    [-1.857142857142857, 1, 0],
    [0.905, -1.875, 1],
    [0, -30, 32]
]

# Right-hand side
b = [-0.438442857142857, 0.016, 2.14]

# Solve the system
answer = np.linalg.solve(A, b)

# Print results
print("y(0.7) =", 0.51)
print("y(0.8) =", answer[0])
print("y(0.9) =", answer[1])
print("y(1.0) =", answer[2])

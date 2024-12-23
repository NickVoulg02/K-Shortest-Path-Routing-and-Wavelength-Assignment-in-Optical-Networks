import time
import numpy as np
import wavelength_assignment

# Define the paths for each pair of nodes.
# The pairs are represented as tuples (i, j) with i < j.
# Each value is a list of nodes representing the path.
paths = \
    {
        (1, 2): [1, 3, 4, 2],
        (1, 3): [1, 3],
        (1, 4): [1, 3, 4],
        (1, 5): [1, 3, 4, 5],
        (2, 3): [2, 4, 3],
        (2, 4): [2, 4],
        (2, 5): [2, 5],
        (3, 4): [3, 4],
        (3, 5): [3, 4, 5],
        (4, 5): [4, 5]
    }

# Traffic matrix B
B = np.array([
    [0, 0, 2, 0, 0],
    [0, 0, 0, 1, 2],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 2, 0, 1, 0]
])

num_nodes = 5
lambda_count = 5  # Number of wavelengths available per link

# Extract the list of all links from the paths without reversing their direction.
links = set()
for p in paths.values():
    for i in range(len(p) - 1):
        link = (p[i], p[i + 1])
        links.add(link)

links = list(links)

# Measure execution time for Random Fit
start_time = time.perf_counter()
blocked_percentage, wavelength_allocation = wavelength_assignment.random_fit(paths, lambda_count, num_nodes, B, links)
end_time = time.perf_counter()
random_fit_time = end_time - start_time

print("\nWavelength to Connections Mapping based on Random Fit Algorithm:")
for w, connections in wavelength_allocation.items():
    if connections:
        conn_str = ", ".join(f"{c[0]}-{c[1]}" for c in connections)
        print(f"λ{w} = {conn_str}")
    else:
        print(f"λ{w} = None")

print("\nPercentage of requests blocked: {:.2f}%".format(blocked_percentage))
print(f"Time taken by Random Fit: {random_fit_time:.9f} seconds")

# Measure execution time for First Fit
start_time = time.perf_counter()
blocked_percentage2, wavelength_allocation2 = wavelength_assignment.first_fit(paths, lambda_count, num_nodes, B, links)
end_time = time.perf_counter()
first_fit_time = end_time - start_time

print("\nWavelength to Connections Mapping based on First Fit Algorithm:")
for w, connections in wavelength_allocation2.items():
    if connections:
        conn_str = ", ".join(f"{c[0]}-{c[1]}" for c in connections)
        print(f"λ{w} = {conn_str}")
    else:
        print(f"λ{w} = None")

print("\nPercentage of requests blocked: {:.2f}%".format(blocked_percentage2))
print(f"Time taken by First Fit: {first_fit_time:.9f} seconds")

# Measure execution time for Least Used
start_time = time.perf_counter()
blocked_percentage3, wavelength_allocation3 = wavelength_assignment.least_used(paths, lambda_count, num_nodes, B, links)
end_time = time.perf_counter()
least_used_time = end_time - start_time

print("\nWavelength to Connections Mapping based on Least Used Algorithm:")
for w, connections in wavelength_allocation3.items():
    if connections:
        conn_str = ", ".join(f"{c[0]}-{c[1]}" for c in connections)
        print(f"λ{w} = {conn_str}")
    else:
        print(f"λ{w} = None")

print("\nPercentage of requests blocked: {:.2f}%".format(blocked_percentage3))
print(f"Time taken by Least Used: {least_used_time:.9f} seconds")

# Summary of execution times
print("\nExecution Time Summary:")
print(f"Random Fit: {random_fit_time:.9f} seconds")
print(f"First Fit: {first_fit_time:.9f} seconds")
print(f"Least Used: {least_used_time:.9f} seconds")

import csv
import numpy as np
import matplotlib.pyplot as plt

# Function to read CSV data skipping the first three rows
def read_csv(file_path):
    with open(file_path, 'r') as file:
        # Skip the first four rows
        for _ in range(2):
            next(file)
        # Read the rest of the data
        reader = csv.reader(file)
        data = list(reader)
    return data

# Function to plot CSV data
def plot_csv(data):
    time_values = [float(row[0]) * 1e6 for row in data]
    CLK_values = [float(row[1]) * 1 for row in data]

    x_ticks = np.arange(-2.5, 3, 0.5).tolist()
    x_tick_labels = [f"{i} μs" for i in x_ticks]

    plt.figure(figsize=(12, 8))

    plt.plot(time_values, CLK_values, color='orange', marker='o', markersize=0.1)
    plt.xlabel('Time (μs)')
    plt.xticks(x_ticks, x_tick_labels)
    plt.yticks([0, 3.3], ['0 V', '3.3 V'])
    plt.grid(axis='x') # Add vertical grid lines
    plt.title('1 MHz CLK, plot from scope_1.csv and scope at PMOD0_0')

    # Display the plot
    plt.show()

# Read CSV data
csv_data = read_csv('scope_1.csv')

# Plot the data
plot_csv(csv_data)
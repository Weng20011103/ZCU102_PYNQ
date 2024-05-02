import csv
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
    time_values = [float(row[0]) * 1e3 for row in data]
    CLR_values = [float(row[1]) * 1 for row in data]
    VOUT_values = [float(row[2]) * 1 for row in data]

    x_ticks = list(range(-15, 20 , 5))
    x_tick_labels = [f"{i} ms" for i in x_ticks]

    # Creating subplots for each channel
    plt.figure(figsize=(12, 8))

    # Subplot for CLR
    plt.subplot(2, 1, 1)
    plt.plot(time_values, CLR_values, color='green', marker='o', markersize=0.1)
    plt.xticks(x_ticks, x_tick_labels)
    plt.yticks([0, 3.3], ['0 V', '3.3 V'])
    plt.title('CLR')
    plt.grid(axis='x') # Add vertical grid lines

    # Subplot for Vout
    plt.subplot(2, 1, 2)
    plt.plot(time_values, VOUT_values, color='violet', marker='o', markersize=0.1)
    plt.xticks(x_ticks, x_tick_labels)
    plt.yticks([0, 1, 2.07], ['0 V', '1 V', '2.07 V'])
    plt.title('VOUT')
    plt.xlabel('Time')
    plt.grid(axis='x') # Add vertical grid lines
    plt.axhline(y=2.1, xmin=0, xmax=0.2, color='violet', linestyle='--')
    
    # Adjust layout
    plt.tight_layout()

    # Display the plot
    plt.show()

# Read CSV data
csv_data = read_csv('scope_1.csv')

# Plot the data
plot_csv(csv_data)
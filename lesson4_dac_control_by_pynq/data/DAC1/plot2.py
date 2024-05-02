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
    CLK_values = [float(row[1]) * 1 for row in data]
    SDI_values = [float(row[2]) * 1 for row in data]
    LD_values = [float(row[3]) * 1 for row in data]
    VOUT_values = [float(row[4]) * 1 for row in data]

    x_ticks = list(range(-20, 300 , 20))
    x_tick_labels = [f"{i} ms" for i in x_ticks]

    # Creating subplots for each channel
    plt.figure(figsize=(12, 8))

    # Subplot for CLK
    plt.subplot(4, 1, 1)
    plt.plot(time_values, CLK_values, color='orange', marker='o', markersize=0.1)
    plt.title('CLK')
    plt.xticks(x_ticks, x_tick_labels)
    plt.yticks([0, 3.3], ['0 V', '3.3 V'])
    plt.grid(axis='x') # Add vertical grid lines

    # Subplot for SDI
    plt.subplot(4, 1, 2)
    plt.plot(time_values, SDI_values, color='blue', marker='o', markersize=0.1)
    plt.yticks([0, 3.3], ['0 V', '3.3 V'])
    plt.title('SDI = 0b101010101010')
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)  # Remove x-axis labels

    # Subplot for LD
    plt.subplot(4, 1, 3)
    plt.plot(time_values, LD_values, color='green', marker='o', markersize=0.1)
    plt.yticks([0, 3.3], ['0 V', '3.3 V'])
    plt.title('LD')
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)  # Remove x-axis labels

    # Subplot for Vout
    plt.subplot(4, 1, 4)
    plt.plot(time_values, VOUT_values, color='violet', marker='o', markersize=0.1)
    plt.yticks([0, 1, 2.1], ['0 V', '1 V', '2.1 V'])
    plt.xticks(x_ticks, x_tick_labels)
    plt.title('VOUT = 2.10 V')
    plt.xlabel('Time')
    plt.axhline(y=2.1, xmin=0, xmax=0.86, color='violet', linestyle='--')
    
    # Adjust layout
    plt.tight_layout()

    # Display the plot
    plt.show()

# Read CSV data
csv_data = read_csv('scope_2.csv')

# Plot the data
plot_csv(csv_data)
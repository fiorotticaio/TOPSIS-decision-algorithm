# TOPSIS Algorithm Implementation

import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":    
    matrix_d = np.genfromtxt("matrix_d.csv", delimiter=",") # Read a matrix in a csv file
    m, n = matrix_d.shape # Get number of lines m and columns n

    weights = np.genfromtxt("weights.csv", delimiter=",") # Read the weights in a csv file

    # Normalize the matrix_d into anothe matrix_r
    matrix_r = np.zeros((m, n)) # Create a matrix with zeros
    for j in range(n):
        sum = 0
        for i in range(m):
            sum += matrix_d[i][j] ** 2
        for i in range(m):
            matrix_r[i][j] = matrix_d[i][j] / np.sqrt(sum)

    # Multiply the values of the matrix r with the weight vector, generating a new matrix p
    matrix_p = np.zeros((m, n)) # Create a matrix with zeros
    for i in range(m):
        for j in range(n):
            matrix_p[i][j] = matrix_r[i][j] * weights[j][0]

    # First step of TOPSIS: Calculate the ideal and anti-ideal solutions
    ideal = np.zeros(n) # Create a vector with zeros
    anti_ideal = np.zeros(n) # Create a vector with zeros
    for j in range(n):
        if weights[j][1] == 1: # If the criteria is to maximize
            ideal[j] = np.max(matrix_p[:, j])
            anti_ideal[j] = np.min(matrix_p[:, j])
        else: # If the criteria is to minimize
            ideal[j] = np.min(matrix_p[:, j])
            anti_ideal[j] = np.max(matrix_p[:, j])

    # Second step of TOPSIS: Calculate the distance of each alternative to the ideal and anti-ideal solutions
    distance_ideal = np.zeros(m) # Create a vector with zeros
    distance_anti_ideal = np.zeros(m) # Create a vector with zeros
    for i in range(m):
        sum_ideal = 0
        sum_anti_ideal = 0
        for j in range(n):
            sum_ideal += (ideal[j]- matrix_p[i][j]) ** 2
            sum_anti_ideal += (anti_ideal[j] - matrix_p[i][j]) ** 2
        distance_ideal[i] = np.sqrt(sum_ideal)
        distance_anti_ideal[i] = np.sqrt(sum_anti_ideal)

    # Third step of TOPSIS: Calculate the relative closeness to the ideal solution
    closeness = np.zeros(m) # Create a vector with zeros
    for i in range(m):
        closeness[i] = distance_anti_ideal[i] / (distance_ideal[i] + distance_anti_ideal[i])
        

    # Plot the results
    options = np.genfromtxt("options.csv", delimiter=",", dtype=str) # Read the options in a csv file

    # Define colors for the bars
    colors = plt.cm.viridis(closeness / max(closeness))  # Scale colors to closeness values

    # Plot the results
    fig, ax = plt.subplots()
    bars = ax.bar(options, closeness, color=colors)

    # Add closeness values on top of each bar
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height:.2f}', 
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')

    # General plot settings
    ax.set_ylabel('Closeness')
    ax.set_xlabel('Options')
    ax.set_title('TOPSIS Algorithm Results')
    ax.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    # Add a color legend to explain the relationship between closeness values and bar colors
    color_legend = plt.cm.ScalarMappable(cmap=plt.cm.viridis)
    color_legend.set_array(closeness)
    cbar = plt.colorbar(color_legend, ax=ax)
    cbar.set_label('Closeness')

    plt.show()
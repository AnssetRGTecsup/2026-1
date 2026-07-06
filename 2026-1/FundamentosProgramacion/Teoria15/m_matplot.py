import matplotlib.pyplot as plt

# Read more in: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html   

def DrawGraphGraph():
    # Data
    x = [1, 2, 3, 4]
    y = [10, 15, -10, -5]

    # Create plot
    plt.plot(x, y, marker='o', mfc="red", mec='black', linestyle='dashdot', color='blue')
    plt.title("Matplotlib Simple Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.show()

def DrawData(x, y, x_label, y_label):
    plt.bar(x, y, color='skyblue')
    plt.title('Monthly Sales (Matplotlib)')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
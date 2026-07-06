import seaborn as sns
import matplotlib.pyplot as plt

def DrawGraphGraph():
    # Load example dataset
    tips = sns.load_dataset("tips")

    # Create a scatter plot
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
    plt.title("Seaborn Scatter Plot")
    plt.show()

def DrawData(x, y, x_label, y_label):
    # Using a built-in theme for a modern look
    sns.set_theme(style="whitegrid")
    sns.barplot(x=x, y=y, palette="viridis")

    plt.title('Monthly Sales (Seaborn)')
    plt.show()
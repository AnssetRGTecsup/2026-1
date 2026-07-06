import plotly.express as px

def DrawGraphGraph():
    # Data
    df = px.data.iris()

    # Create interactive scatter plot
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                    title="Plotly Interactive Scatter Plot")
    fig.show()

def DrawData(x, y, x_label, y_label):
    fig = px.bar(x, y, title="Monthly Sales (Plotly)", 
             labels={'x': x_label, 'y': y_label})
    fig.show()
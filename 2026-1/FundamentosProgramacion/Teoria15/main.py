import m_matplot
import m_plotly
import m_seaborn

def main():
    #m_matplot.DrawGraphGraph()

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    sales = [150, 200, 180, 250, 300]

    #m_matplot.DrawData(months, sales, "Months", "Units Sold")
    m_plotly.DrawData(months, sales, "Months", "Units Sold")
    #m_seaborn.DrawData(months, sales, "Months", "Units Sold")


if __name__ == "__main__":
    main()
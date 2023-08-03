
from datetime import datetime

class Salesanalysis:
    def __init__(self):
        self.sales_data = []

    def add_sale(self, name, amount, date):# Get a Name,Amount,Date and append in Empty list as sales_data.
        sale = {
            "Salesperson Name": name,
            "Sales Amount": amount,
            "Sales Date": date
        }
        self.sales_data.append(sale)
        

    def total_sales(self):# To calculate the total amount of sales.
        total_sales = 0
        for sale in self.sales_data:
            total_sales += sale["Sales Amount"]
        return total_sales

    def avgdaily_sales(self):# To calculate the average sales of the each day.
        sales_dates = set()
        for sale in self.sales_data:
            sales_dates.add(sale["Sales Date"])
        total_days = len(sales_dates)
        return self.total_sales() / total_days

    def top_salesperson(self):# To get a top sales person name considered as a sales amount is maximum in the list.
        max_sales = None
        top_salesperson = ""
        for sale in self.sales_data:
            if max_sales is None or sale["Sales Amount"] > max_sales:
                max_sales = sale["Sales Amount"]
                top_salesperson = sale["Salesperson Name"]
        return top_salesperson

    def lowest_salesperson(self): # To get a lowest sales person name considered as a sales amount is lower in the list.
        min_sales = None
        lowest_salesperson = ""
        for sale in self.sales_data:
            if min_sales is None or sale["Sales Amount"] < min_sales:
                min_sales = sale["Sales Amount"]
                lowest_salesperson = sale["Salesperson Name"]
        return lowest_salesperson

    def monthlysales_distribution(self): # To calculate the monthly sales amount.
        monthly_sales = {}
        for sale in self.sales_data:
            year_month = sale["Sales Date"][:7]  # Get "YYYY-MM" from the date
            monthly_sales[year_month] = monthly_sales.get(year_month, 0) + sale["Sales Amount"]
        return monthly_sales

    def analysis_results(self): #Call all the five methods and print.
        total_sales = self.total_sales()
        avg_daily_sales = self.avgdaily_sales()
        top_salesperson = self.top_salesperson()
        lowest_salesperson = self.lowest_salesperson()
        monthly_sales_distribution = self.monthlysales_distribution()

        print("*" * 75)
        print("Total sales amount:", total_sales)
        print("Average amount of daily sales:", avg_daily_sales)
        print("Top salesperson is:", top_salesperson)
        print("Lowest salesperson is:", lowest_salesperson)

        for month, sales in sorted(monthly_sales_distribution.items()):
            print("Monthly sales distribution:", month, "And total amount is", sales)

        print("*" * 75)


obj = Salesanalysis()
while True:
    name = input("Enter salesperson name: ")

    if not name.isalpha():
        print("The name should contain only alphabetic characters.")
        continue

    while True:
        amount = input("Enter the Sales amount: ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("The sales amount should be a numeric value.")
            else:
                break
        except ValueError:
            print("Invalid sales amount. Please enter a numeric value.")

    while True:
        date = input("Enter the sales date (YYYY-MM-DD): ")
        try:
            input_date = datetime.strptime(date, "%Y-%m-%d")
            if input_date > datetime.now():
                print("The date cannot be greater than the current date.")
            else:
                break
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD' format.")

    obj.add_sale(name, amount, date)

    continuee = input("Do you want to add more details? (YES/NO): ").lower()
    if continuee == "no":
        break
    elif continuee != "yes":
        print("Please enter 'YES' or 'NO'.")
        break

obj.analysis_results()

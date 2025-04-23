#asking the user for total sales input
total_sales = float(input("What is your total sales amount? "))

#asking user for commission percentage
commision_percentage = float(input("What is your commission on sales? "))

#calculating the commission amount
commission_amount = (commision_percentage/100)*total_sales

#displaying the commissiom
print(f"your total commission amount is {commission_amount}")
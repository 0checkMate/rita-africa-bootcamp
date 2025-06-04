import pandas as pd
import csv

#collecting customer feedback data using input function
# customer_name1 = input("Enter the first customer's name: ")
# customer_rating1 = input("Enter the first customer's rating (1-5): ")
# customer_feedback1 = input("Enter the first customer's feedback: ")


#saving the data to a CSV file
with open('customer_feedback.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Customer Name', 'Rating', 'Feedback'])
    writer.writerow([customer_name1, customer_rating1, customer_feedback1])

    for i in range(1, 6):
        customer_name = input(f"Enter the {i}th customer's name: ")
        customer_rating = input(f"Enter the {i}th customer's rating (1-5): ")
        customer_feedback = input(f"Enter the {i}th customer's feedback: ")
        writer.writerow([customer_name, customer_rating, customer_feedback])

#reading the data from the CSV file
df = pd.read_csv('customer_feedback.csv')

#displaying the collected feedback
print(df)

# Displaying the first row of the dataset
print(df.head())

# Displaying the info of the dataset
print(df.info())

#Calculating the total and average ratings
total_ratings = df['Rating'].astype(int).sum()
# average_rating = df['Rating'].astype(int).mean()
average_rating = total_ratings / len(df)
print(f"Total Ratings: {total_ratings}")
print(f"Average Rating: {average_rating:.2f}") # Displaying the average rating formatted to 2 decimal places using :.2f

#categorizing feedback based on ratings 
def categorize_feedback(row):
    if row['Rating'] >= 4 and 'excellent' in row['Feedback'].lower():
        return'Very positive'
    elif row['Rating'] >= '4':
        return 'Positive'
    elif row['Rating'] == '3':
        return 'Neutral'
    else:
        return 'Negative'

df['Feedback Category'] = df.apply(categorize_feedback, axis=1)

# Displaying the categorized feedback
print("\nCategorized Feedback:")
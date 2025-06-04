import pandas as pd
import csv

# Helper function to correct ordinal suffix (1st, 2nd, 3rd, etc.)
def ordinal(n):
    return f"{n}{'tsnrhtdd'[(n//10%10!=1)*(n%10<4)*n%10::4]}"

#collecting customer feedback data using input function and saving the data to a CSV file
#Overwrites previous file every time the script is run
with open('customer_feedback.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Writing the header row
    writer.writerow(['Name', 'Rating', 'Feedback'])

    for i in range(1,6):
        i = ordinal(i)
        customer_name = input(f"Enter the {i} customer's name: ")
        customer_rating = int(input(f"Enter the {i} customer's rating (1-5): "))
        customer_feedback = input(f"Enter the {i} customer's feedback: ")
        writer.writerow([customer_name, customer_rating, customer_feedback])

#reading the data from the CSV file
df = pd.read_csv('customer_feedback.csv')

#displaying the collected feedback
print("\nCollected Customer Feedback:")
print(df)

# Displaying the first row of the dataset
print("\nFirst Row of the Dataset:")
print(df.head())

# Displaying the info of the dataset
print("\nDataset Information:")
print(df.info())

#Calculating the total and average ratings
df['Rating'] = df['Rating'].astype(int)  # Ensuring the 'Rating' column is of integer type
total_ratings = df['Rating'].sum()
average_rating = df['Rating'].mean()

# Displaying the total and average ratings
print(f"Total Ratings: {total_ratings}")
print(f"Average Rating: {average_rating:.2f}") # Displaying the average rating formatted to 2 decimal places using :.2f

#categorizing feedback based on ratings 
def categorize_feedback(row):

    rating = int(row['Rating'])
    feedback = str(row['Feedback']).lower()

    if rating >= 4 and 'excellent' in feedback:
        return'Very positive'
    elif rating >= 4:
        return 'Positive'
    elif rating == 3:
        return 'Neutral'
    else:
        return 'Negative'

# Applying the categorization function to each row (axis=1 for rows/ axis=0 for columns)
#creating a new column 'Feedback Category' based on the categorization function
df['Feedback Category'] = df.apply(categorize_feedback, axis=1)

# Displaying the categorized feedback
print("\nCategorized Feedback:")
print(df[['Name', 'Rating', 'Feedback', 'Feedback Category']])
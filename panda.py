import pandas as pd

# Create a Pandas DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 32, 18, 47, 23],
        'City': ['New York', 'Paris', 'London', 'Tokyo', 'Sydney']}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Select rows based on a condition
adults = df[df['Age'] >= 18]
print(adults)

# Sort the DataFrame by age in descending order
sorted_df = df.sort_values('Age', ascending=False)
print(sorted_df)

# Group the DataFrame by city and calculate the mean age for each city
grouped_df = df.groupby('City').mean()
print(grouped_df)

# Save the DataFrame to a CSV file
df.to_csv('people.csv', index=False)

# Read the CSV file into a DataFrame
df2 = pd.read_csv('people.csv')
print(df2)

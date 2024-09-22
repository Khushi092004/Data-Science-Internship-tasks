import pandas as pd

# File path
file_path = r'C:\projects\Data Science Internship\Task-01_Population_Distribution_Visualization\data\india-districts-census-2011.csv'

# Load the dataset
try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()

# Display initial data information
print("Initial Data Information:")
print(data.info())

# Drop columns that are irrelevant or contain too many missing values
# Example: You can adjust the column names based on your analysis
columns_to_drop = ['Column_Name_1', 'Column_Name_2']  # Replace with actual column names
data.drop(columns=columns_to_drop, errors='ignore', inplace=True)

# Handle missing values
# Option 1: Fill missing values with zeros
data.fillna(0, inplace=True)

# Option 2: Drop rows with missing target values (if any)
# data.dropna(subset=['Population'], inplace=True)  

# Check for duplicates and remove them
data.drop_duplicates(inplace=True)

# Display cleaned data information
print("Cleaned Data Information:")
print(data.info())

# Save cleaned data
cleaned_file_path = r'C:\projects\Data Science Internship\Task-01_Population_Distribution_Visualization\data\cleaned_population_data.csv'
data.to_csv(cleaned_file_path, index=False)
print("Cleaned data saved successfully!")

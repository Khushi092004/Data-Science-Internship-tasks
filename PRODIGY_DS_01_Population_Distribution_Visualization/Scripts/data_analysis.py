import pandas as pd

# Load cleaned dataset
file_path = r'C:\projects\Data Science Internship\PRODIGY_DS_01_Population_Distribution_Visualization\data\cleaned_population_data.csv'

# Load the dataset
try:
    data = pd.read_csv(file_path)
    print("Cleaned data loaded successfully!")
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()

# Summary Statistics analysis
summary_stats = data.describe()
print("Summary Statistics:")
print(summary_stats)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# File path
file_path = r'C:\projects\Data Science Internship\Task-01_Population_Distribution_Visualization\data\india-districts-census-2011.csv'

# Load the dataset
try:
    data = pd.read_csv(file_path)
    print("Data loaded successfully!")
except FileNotFoundError:
    print(f"File not found at {file_path}. Please check the path.")
    exit()
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()

# Bar Plot for Population by State
plt.figure(figsize=(12, 6))
sns.barplot(x='State name', y='Population', data=data, estimator=sum, errorbar=None)
plt.title('Population Distribution by State')
plt.xlabel('State Name')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('population_distribution_by_state.png')  # Save the plot
plt.show()

# Histogram for Population
plt.figure(figsize=(10, 6))
sns.histplot(data['Population'], bins=30, kde=True)
plt.title('Population Distribution Histogram')
plt.xlabel('Population')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('population_distribution_histogram.png')  # Save the plot
plt.show()

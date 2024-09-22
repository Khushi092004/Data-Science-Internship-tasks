import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
cleaned_file_path = r'C:\projects\Data Science Internship\Task-02_EDA\data\cleaned_train.csv'
def load_data():
    return pd.read_csv(cleaned_file_path)

# Perform EDA
def perform_eda(data):
    # Display basic statistics
    print(data.describe())
    
    # Countplot of Survived
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Survived', data=data)
    plt.title('Count of Survived vs Not Survived')
    plt.show()
    
    # Barplot of Survival Rate by Gender
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Sex', y='Survived', data=data)
    plt.title('Survival Rate by Gender')
    plt.show()
    
    # Correlation Heatmap
    plt.figure(figsize=(12, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

if __name__ == "__main__":
    data = load_data()
    perform_eda(data)

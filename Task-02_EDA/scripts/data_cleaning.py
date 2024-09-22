import pandas as pd

# File path
file_path = r'C:\projects\Data Science Internship\Task-02_EDA\data\train.csv'
cleaned_file_path = r'C:\projects\Data Science Internship\Task-02_EDA\data\cleaned_train.csv'

# Load the dataset
def load_data():
    return pd.read_csv(file_path)

# Clean the dataset
def clean_data(data):
    # Drop columns with too many missing values or irrelevant information
    data.drop(columns=['Cabin', 'Ticket'], inplace=True)
    
    # Handle missing values
    data['Age'].fillna(data['Age'].median(), inplace=True)
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
    
    return data

def save_cleaned_data(data):
    data.to_csv(cleaned_file_path, index=False)
    print("Cleaned data saved successfully!")

if __name__ == "__main__":
    data = load_data()
    cleaned_data = clean_data(data)
    save_cleaned_data(cleaned_data)

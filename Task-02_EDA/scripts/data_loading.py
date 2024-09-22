import pandas as pd

file_path = r'C:\projects\Data Science Internship\Task-02_EDA\data\train.csv'

def load_data():
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully!")
        return data
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

if __name__ == "__main__":
    load_data()

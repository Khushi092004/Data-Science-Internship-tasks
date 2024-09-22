import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns
file_path = r'C:\projects\Data Science Internship\Task-03_Decision_Tree\data\bank-marketing.csv'
try:
    data = pd.read_csv(file_path, sep=';')  # Ensure correct delimiter
    print("Data loaded successfully!")
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit()
# Check for missing values/ data cleaninngg
print("Missing values in each column:")
print(data.isnull().sum())

# Encoding categorical variables
data['y'] = data['y'].map({'yes': 1, 'no': 0})  # Target variable

# Features and target variable
X = data.drop(columns=['y'])
y = data['y']

# One-hot encoding for categorical features
X = pd.get_dummies(X, drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Model Training
classifier = DecisionTreeClassifier(random_state=42)
classifier.fit(X_train, y_train)

# Predictions
y_pred = classifier.predict(X_test)

# Evaluation
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Visualize the decision tree 
from sklearn.tree import plot_tree

plt.figure(figsize=(20, 10))
plot_tree(classifier, filled=True, feature_names=X.columns, class_names=['Not Purchased', 'Purchased'])
plt.title("Decision Tree Visualization")
plt.savefig(r'C:\projects\Data Science Internship\Task-03_Decision_Tree\outputs\decision_tree.png')  # Save the tree visualization
plt.show()

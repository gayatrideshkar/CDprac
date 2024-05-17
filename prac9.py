import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the iris dataset
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
iris = pd.read_csv(url)

# Inspect the dataset
print("First 5 rows of the dataset:")
print(iris.head())

# Define the features and target
X = iris.drop('species', axis=1)
y = iris['species']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train the k-NN classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Make predictions
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

# Display the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(conf_matrix)

# Identify correct and incorrect predictions
correct_predictions = X_test[y_test == y_pred]
incorrect_predictions = X_test[y_test != y_pred]

# Display correct and incorrect predictions
print("\nCorrect Predictions:")
for i in range(len(y_test)):
    if y_test.iloc[i] == y_pred[i]:
        print(f"Predicted: {y_pred[i]}, Actual: {y_test.iloc[i]}, Features: {X_test[i]}")

print("\nIncorrect Predictions:")
for i in range(len(y_test)):
    if y_test.iloc[i] != y_pred[i]:
        print(f"Predicted: {y_pred[i]}, Actual: {y_test.iloc[i]}, Features: {X_test[i]}")

import pandas as pd 
from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC 
from sklearn.metrics import accuracy_score 
iris = load_iris() 
X = iris.data 
y = iris.target 
# Describe function to get a statistical summary of the dataset 
print("Multiple Regression Model Dataset Summary:\n") 
print(pd.DataFrame(X).describe()) 
# Split the dataset into training and testing sets 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
# Choose a classifier. In this example, we will use the Support Vector Machine (SVM) classifier 
svm = SVC() 
# Fit the model on the training data 
svm.fit(X_train, y_train) 
# Predict the target variable on the testing data 
y_pred = svm.predict(X_test) 
# Evaluate the performance of the classifier using accuracy score 
accuracy = accuracy_score(y_test, y_pred) 

import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset from the web
url = "https://stats.idre.ucla.edu/stat/data/binary.csv"
df = pd.read_csv(url)

# Rename columns for better readability
df.columns = ['admit', 'gre', 'gpa', 'rank']

# Inspect the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Define the independent variables (GRE and Rank) and the dependent variable (GPA)
X = df[['gre', 'rank']]
y = df['gpa']

# Add a constant to the model (the intercept term)
X = sm.add_constant(X)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Fit the multiple linear regression model
model = sm.OLS(y_train, X_train)
result = model.fit()

# Print the summary of the multiple regression model
print("\nSummary of the multiple regression model:")
print(result.summary())

# Predict the GPA on the test set
y_pred = result.predict(X_test)

# Calculate the Mean Squared Error and R-squared value
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R-squared Value:", r2)

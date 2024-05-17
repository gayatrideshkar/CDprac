import pandas as pd
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Load the dataset from the web
url = "https://stats.idre.ucla.edu/stat/data/binary.csv"
df = pd.read_csv(url)

# Rename columns for better readability
df.columns = ['admit', 'gre', 'gpa', 'rank']

# Inspect the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Define the independent variables (GRE, GPA, and Rank) and the dependent variable (admit)
X = df[['gre', 'gpa', 'rank']]
y = df['admit']

# Add a constant to the model (the intercept term)
X = sm.add_constant(X)

# Split the dataset into training and testing s

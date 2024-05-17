import pandas as pd

# Load the iris dataset
iris = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

# Calculate the correlation matrix
correlation_matrix = iris.corr()

print("Correlation Matrix:")
print(correlation_matrix)


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset
iris = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

# Calculate the correlation matrix
correlation_matrix = iris.corr()

# Plot the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Iris Dataset')
plt.show()





import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

# Load the iris dataset
iris = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")

# Perform ANOVA for Sepal Length grouped by Species
model = ols('sepal_length ~ C(species)', data=iris).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print("ANOVA Table for Sepal Length by Species:")
print(anova_table)

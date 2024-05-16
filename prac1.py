import pandas as pd

# Load mtcars dataset
mtcars = pd.read_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")

# Summary statistics
summary_stats = mtcars.describe()

# Information about the dataset
data_info = mtcars.info()

# Quartiles
q1 = mtcars.quantile(0.25)
q2 = mtcars.quantile(0.50)  # Median
q3 = mtcars.quantile(0.75)

print("Summary Statistics:")
print(summary_stats)

print("\nDataset Information:")
print(data_info)

print("\nQuartiles:")
print("Q1:")
print(q1)
print("\nMedian (Q2):")
print(q2)
print("\nQ3:")
print(q3)

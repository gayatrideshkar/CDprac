import pandas as pd
import os

# Define function to read CSV from web
def read_csv_from_web(url):
    df = pd.read_csv(url)
    return df

# Define function to read TXT from disk
def read_txt_from_disk(file_path):
    df = pd.read_csv(file_path, delimiter='\t')
    return df

# Define function to write DataFrame to a CSV file
def write_to_disk(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"File written to {output_path}")

# URL of the Iris dataset (CSV)
csv_url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"

# Path to save the CSV file
output_csv_path = "output_iris.csv"

# Read CSV from web
iris_df = read_csv_from_web(csv_url)

# Write the CSV data to disk
write_to_disk(iris_df, output_csv_path)

# Create a sample TXT file to read from disk
sample_txt_content = """sepal_length\tsepal_width\tpetal_length\tpetal_width\tspecies
5.1\t3.5\t1.4\t0.2\tsetosa
4.9\t3.0\t1.4\t0.2\tsetosa
4.7\t3.2\t1.3\t0.2\tsetosa
4.6\t3.1\t1.5\t0.2\tsetosa
5.0\t3.6\t1.4\t0.2\tsetosa
"""

# Write the sample TXT content to a file
sample_txt_path = "sample_iris.txt"
with open(sample_txt_path, "w") as file:
    file.write(sample_txt_content)

# Read the TXT file from disk
txt_df = read_txt_from_disk(sample_txt_path)

# Path to save the TXT file read data
output_txt_path = "output_iris_from_txt.csv"

# Write the TXT data to disk as a CSV
write_to_disk(txt_df, output_txt_path)

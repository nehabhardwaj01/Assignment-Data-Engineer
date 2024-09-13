from pandas import read_csv

# 3a) Write a simple block of Python code that
# (a) reads the input file (and all of its transactions)
df = read_csv("transactions.csv")
print(df)

# (b) calculates the average transaction amount across all records.
avg = df['TransactionAmount'].mean()
print(f"average is: {avg}")

# 3b) If this file were to be saved in a GCS bucket, how could you access it from BigQuery?

# The following steps could be followed
# 1. Ensure the Bigquery and GCS are in the same project
# 2. Create new table in the Bigquery
# 3. Select Google cloud storage as the SOURCE option
# 4. Select the GCS file URI
# 5. Select file format as CSV
# 6. Mention the dataset and the table name



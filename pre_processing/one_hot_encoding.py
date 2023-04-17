import pandas as pd

# Load the CSV file into a pandas dataframe
df = pd.read_csv('C:/Users/User/CSNL/Deep_Learning/Project/Deep_Learning_Project/data/cleaned_train.csv')

# Select the column you want to one-hot encode
column_to_encode = 'topic'

# Use pandas get_dummies function to one-hot encode the selected column
one_hot_encoded = pd.get_dummies(df[column_to_encode], prefix=column_to_encode)

# Concatenate the one-hot encoded values into a single column
concatenated = one_hot_encoded.astype(str).apply(lambda x: '[' + ''.join(x) + ']', axis=1)

# Replace the original column with the concatenated one-hot encoded values
df[column_to_encode] = concatenated

# Save the updated dataframe to a new CSV file
df.to_csv('your_encoded_file.csv', index=False)

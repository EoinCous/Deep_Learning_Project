import pandas as pd

# Read the CSV file
df = pd.read_csv('C:/Users/User/CSNL/Deep_Learning/Project/Deep_Learning_Project/data/cleaned_train.csv')


# Define a function to get the length of a numerical sequence separated by commas
def get_sequence_length(sequence):
    try:
        return len(sequence.split(','))
    except:
        return 0


# Define a function to pad a sequence with zeros
def pad_sequence(sequence, length):
    return sequence + [0]*(length-len(sequence))


# Read the CSV file
df = pd.read_csv('C:/Users/User/CSNL/Deep_Learning/Project/Deep_Learning_Project/data/cleaned_train.csv')

# Find the maximum length of the numerical sequences
max_len = df['numerical_sequence_headline_abstract_keywords'].apply(get_sequence_length).max()

# Pad the sequences with zeros if they are less than the maximum length
df['padded_sequence'] = df['numerical_sequence_headline_abstract_keywords'].apply(lambda x: pad_sequence(x.split(','), max_len) if isinstance(x, str) else x)

# Write the updated DataFrame to a new CSV file
df.to_csv('padded_file.csv', index=False)

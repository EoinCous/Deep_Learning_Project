import csv

# Open the CSV file in read mode
with open('C:/Users/User/CSNL/Deep_Learning/Project/Deep_Learning_Project/data/cleaned_train.csv', 'r', encoding='utf-8-sig') as infile:
    # Create a CSV reader object
    reader = csv.reader(infile)
    # Get the header row
    header = next(reader)
    # Find the index of the column to decrement
    col_index = header.index('BERT_sentiment_score')  # Replace 'column_name' with the actual column name

    # Create a list to store the updated rows
    updated_rows = []

    # Loop through each row in the CSV file
    for row in reader:
        try:
            # Decrement the value in the specified column by 1
            row[col_index] = str(int(row[col_index]) - 1)
            # Add the updated row to the list of updated rows
            updated_rows.append(row)
        except ValueError:
            pass

# Write the updated rows to a new CSV file
with open('output.csv', 'w', newline='', encoding='utf-8-sig') as outfile:
    # Create a CSV writer object
    writer = csv.writer(outfile)
    # Write the header row
    writer.writerow(header)
    # Write the updated rows
    writer.writerows(updated_rows)

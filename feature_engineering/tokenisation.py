import csv
import nltk

def concat():
    # open the input and output csv files
    with open('C:/Users/User/CSNL/Deep_Learning/Project/Deep_Learning_Project/data/cleaned_train.csv', encoding='utf-8-sig') as infile, open('C:/Users/User/CSNL/Deep_Learning/Project/Deep_Learning_Project/data/output_file.csv', 'w', encoding='utf-8-sig', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # skip headers
        next(reader)

        # loop through each row in the input file
        for row in reader:
            # combine the three columns of sentences into one column
            combined_sentence = row[1] + " " + row[2] + " " + row[3]

            # write the new row to the output file
            writer.writerow([combined_sentence])


def tokenise():
    import nltk
    import re
    nltk.download('punkt')

    # regular expression pattern to match special characters
    pattern = r'[^a-zA-Z0-9\s]'

    # open the input and output csv files
    with open('C:/Users/User/CSNL/Deep_Learning/Project/Deep_Learning_Project/data/output_file.csv', encoding='utf-8') as infile, open('C:/Users/User/CSNL/Deep_Learning/Project/Deep_Learning_Project/data/output_file_tokenised.csv', 'w', encoding='utf-8',
                                                                  newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # loop through each row in the input file
        for row in reader:
            # tokenize the text in the first column
            tokenized_text = nltk.word_tokenize(row[0])

            # remove special characters from tokens
            cleaned_text = [re.sub(pattern, '', token) for token in tokenized_text]

            # write the new row to the output file
            writer.writerow([' '.join(cleaned_text)])


def numericalisation():
    from keras.preprocessing.text import Tokenizer

    # load the input CSV file
    with open('C:/Users/User/CSNL/Deep_Learning/Project/Deep_Learning_Project/data/output_file_tokenised.csv', 'r') as infile:
        reader = csv.reader(infile)

        # extract the column of tokenized text
        texts = [row[0] for row in reader]

    # create a Tokenizer object
    tokenizer = Tokenizer()

    # fit the tokenizer on the text data
    tokenizer.fit_on_texts(texts)

    # convert the text data to numerical sequences
    sequences = tokenizer.texts_to_sequences(texts)

    # write the sequences to the output CSV file
    with open('C:/Users/User/CSNL/Deep_Learning/Project/Deep_Learning_Project/data/output_file_numericalised.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for seq in sequences:
            writer.writerow([','.join(map(str, seq))])

if __name__ == "__main__":
    #concat()
    #tokenise()
    numericalisation()

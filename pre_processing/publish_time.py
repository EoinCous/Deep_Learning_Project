import pandas as pd


def dayOfWeek(day):
    match day:
        case 0:
            return "Monday"
        case 1:
            return "Tuesday"
        case 2:
            return "Wednesday"
        case 3:
            return "Thursday"
        case 4:
            return "Friday"
        case 5:
            return "Saturday"
        case 6:
            return "Sunday"
        case _:
            return None

def main():


    # Read CSV file into dataframe
    df = pd.read_csv('../data/cleaned_train.csv')

    # Convert date-time column to datetime format
    df['pub_date'] = pd.to_datetime(df['pub_date'])

    # Extract day of week and hour of day
    df['pub_day'] = df['pub_date'].dt.dayofweek

    df['pub_hour'] = df['pub_date'].dt.hour

    # Write modified dataframe to CSV file
    df.to_csv('data/data_modified.csv', index=False)


if __name__ == '__main__':
    main()
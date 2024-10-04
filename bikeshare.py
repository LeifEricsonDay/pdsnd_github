import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    invalid_input = True
    while invalid_input:
        city = input("Which city would you like information on? Enter an option from (chicago, new york city, or washington). \n")
        city = city.lower()
        if city not in ["chicago", "new york city", "washington"]:
            print("You didn't input a valid city, please try again")
        else:
            invalid_input = False   

    # TO DO: get user input for month (all, january, february, ... , june)
    invalid_input = True
    while invalid_input:
        month = input("Which month (if any) would you like information on? Enter an option from (all, january, february, ... , june) \n")
        month = month.lower()
        if month not in ["all", "january", "february", "march", "april", "may", "june"]:
            print("You didn't input a valid month, please try again")
        else:
            invalid_input = False   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    invalid_input = True
    while invalid_input:
        day = input("Which day (if any) would you like information on? Enter an option from (all, monday, tuesday, ..., sunday) \n")
        day = day.lower()
        if day not in ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            print("You didn't input a valid day, please try again")
        else:
            invalid_input = False   

    print('-'*40)
    return city, month, day

# Use the load_data script from practice problme # 3
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df.head()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    most_popular_month = df['month'].mode()[0]
    print("The most popular month for bike rentals was {}".format(most_popular_month))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_popular_day = df['day_of_week'].mode()[0]
    print("The most popular day for bike rentals was {}".format(most_popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_popular_hour = df['hour'].mode()[0]
    print("The most popular hour for bike rentals was {}".format(most_popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_start_station = df['Start Station'].mode()[0]
    print("The most popular start station for bike rentals was {}".format(most_popular_start_station))

    # TO DO: display most commonly used end station
    most_popular_end_station = df['End Station'].mode()[0]
    print("The most popular end station for bike rentals was {}".format(most_popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    # Add additional column of start/end combos
    df['Start/End'] = df['Start Station'] + "," + df['End Station']
    most_common_route = df['Start/End'].mode()[0].split(',')
    print("The most common route was from {} to {}".format(most_common_route[0], most_common_route[1]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total time traveled across all rides was {} seconds".format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print("The mean travel time across all rides was {} seconds".format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The user types for these rides were:")
    print(df['User Type'].value_counts(), '\n')

    # TO DO: Display counts of gender
    # Analysis of the data sets shows that not every city has gender information. Use a try statement to account for this
    try:
        print("The gender of the users on these rides were:\n", df['Gender'].value_counts())
    except:
        print("Gender information is not available for this city")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    # Analysis of the data sets shows that not every city has birth year information. Use a try statement to account for this.
    try:
        earliest_birth_year = df['Birth Year'].min()
        latest_birth_year = df['Birth Year'].max()
        most_common_birth_year = df['Birth Year'].mode()[0]
        print("The earliest user birth year was {}".format(earliest_birth_year))
        print("The latest user birth year was {}".format(latest_birth_year))
        print("The most common user birth year was {}".format(most_common_birth_year))
    except:
        print("Birth year information is not available for this city")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        raw_data = input('\nWould you like to see 5 lines of raw data from the table? Enter yes or no.\n')
        if raw_data.lower() == 'yes':
            print(df.head())
            display_more = True
            start_row = 5
            end_row = 10
            while display_more:
                wants_more = input('\nWould you like to see 5 more lines of raw data from the table? Enter yes or no.\n')
                if wants_more.lower() == 'yes':
                    print(df.iloc[start_row:end_row])
                    if end_row == len(df.index):
                        print('That is the end of the data')
                        display_more = False
                    start_row = min(start_row + 5, len(df.index))
                    end_row = min(end_row + 5, len(df.index))
                else:
                    display_more = False
                    
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

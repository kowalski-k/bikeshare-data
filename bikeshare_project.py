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
    while True:
      city = input('Enter city you want to check: ').lower()
      try:
        int(city)
        textType = "int"
      except ValueError:
        try:
            float(city)
            textType = "float"
        except ValueError:
            textType = "string"

      if(textType == 'string'):
        break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input('Enter month you want to check: ').lower()
      try:
        int(month)
        textType = "int"
      except ValueError:
        try:
            float(month)
            textType = "float"
        except ValueError:
            textType = "string"

      if(textType == 'string'):
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input('Enter day of week you want to check: ').lower()
      try:
        int(day)
        textType = "int"
      except ValueError:
        try:
            float(day)
            textType = "float"
        except ValueError:
            textType = "string"

      if(textType == 'string'):
        break

    print('-'*40)
    return city, month, day


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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df["start_to_end_station"] = df['Start Station'] + ' to ' + df['End Station']

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month is ', df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('The most common day of week is ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('The most common start hour is ', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station is ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station is ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip 
    print('The most frequent combination of start station and end station trip is ', df['start_to_end_station'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time in seconds is ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean travel time in seconds is ', int(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('There are {} subscribers'.format(df['User Type'].value_counts()[0]))
    print('There are {} customers'.format(df['User Type'].value_counts()[1]))

    # TO DO: Display counts of gender
    if "Gender" in df:
        print('There are {} males'.format(df['Gender'].value_counts()[0]))
        print('There are {} females'.format(df['Gender'].value_counts()[1]))

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print('The earliest year of birth is ', np.min(df['Birth Year']))
        print('The most recent year of birth is ', np.max(df['Birth Year']))
        print('The most common year of birth is ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data_function(df):
    """Displays raw bikeshare data. """
    question = input('\nDo you want to see raw data? Enter yes or no.\n')
    index = 0
    final_question = "yes"
    while True:
        if question.lower() != 'yes' or final_question.lower() != 'yes':
            break
        print(df.iloc[[index, index + 5]])
        index = index + 5
        final_question = input('\nDo you want to see more 5 lines of raw data? Enter yes or no.\n')
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
              
        display_data_function(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

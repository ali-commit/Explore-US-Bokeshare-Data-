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
    cities = ['chicago', 'new york city', 'washington']
    city = input("Enter city name ").lower()
    while city not in cities:
        city = input('while nearly right,Please try again').lower()
        if city in cities:
            print("Great!,{}".format(city))
            break
        else:
             print("Ops!, nearly right, try again")
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all','january','june','july','august','september','may','april','october','november','december','february','march']
    month=input('Enter the month name ').lower()
    while month not in  months:
        month=input('while:try again ').lower()
        if month in months:
            print("well done,{}".format(month))
            break
        else:
            print ('Ops!, something went worng')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all','monday','sunday','tuesday','wednesday','thursday','friday','saturday']
    day=input('Enter the day ').lower()
    while day not in days:
        day=input('Ops! try please ').lower()
        if day in days:
            print('well done , the day is  {}'.format(day))
            break
        else:
                print('Ops, try again ')
    print('-'*40)
    return city, month, day
city, month, day = get_filters()
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
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df
df = load_data(city,month,day)
print(df)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    MCM=df['month'].mode()[0]
    
    
    


    # TO DO: display the most common day of week
    MCD=df['day_of_week'].mode()[0]
        
    
    


    # TO DO: display the most common start hour
    
    MCH=df['Start Time'].dt.hour.mode()[0]
    
    


    print("\nThis took %s seconds." % (time.time() - start_time),MCD,MCM,MCH)
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    MCS=df['Start Station'].mode()[0]


    # TO DO: display most commonly used end station
    MCE=df['End Station'].mode()[0]


    # TO DO: display most frequent combination of start station and end station trip
    df['Start StationEnd Station']=df['Start Station'] + df['End Station']
    MCSE=df['Start StationEnd Station'].mode()[0]


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
         

    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

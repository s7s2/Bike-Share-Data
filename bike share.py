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
    cities =["chicago", "new york city", "washington"] 
    while True:
        city = input('would you like to see data for this list: chicago, new york city, washington? ').lower()
        if city in cities:
            break
        else:
            print('this city is not exist')
    months= ["january", "february", "march","april","may","june","all"]
    while True:
        month = input('Which month? january, february, march, april, may, june,all ?').lower()
        if month in months:
            break 
        else:
            print('this month is not exist')
         
    Days= ["monday", "tuesday", "tuesday","wednesday","thursday","friday","saturday","sunday","all"]
    while True:
        day = input('Which day? monday, tuesday, wednesday, thursday, friday, saturday,sunday,all?').lower()
        
        if day in Days:
            break 
        else:
            print('this day is not exist')
    print('-'*40)
    return city, month ,day    
         
         
        
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
    # convert the Start Time column to datetime
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
     # filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        # filter by day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    months= ["january", "february", "march","april","may","june","all"]
    month=df['month'].mode()[0]
    print('the most common month is :{}'.format(months[month-1]))
    # display the most common day of week
    day=df['day_of_week'].mode()[0]
    print('the most common day is :{}'.format(day))
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most common day is :{}'.format(popular_hour))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print('the most start station is :{}'.format(start_station))

    # display most commonly used end station
    end_station=df['End Station'].mode()[0]      
    print('the most end station is :{}'.format(end_station))

    # display most frequent combination of start station and end station trip
    trip=df['Start Station']+"to"+df['End Station']
    print('the most trip is :{}'.format(trip.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    from datetime import timedelta as td
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel =(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days = total_travel.days
    hours =total_travel.seconds // (60*60)
    minutes =total_travel.seconds % (60*60) //60
    seconds =total_travel.seconds % (60*60) %60
    print(f'Total travel Time is:{days} days {hours} hours {minutes} minutes {seconds} seconds')      
    # display mean travel time
    average_travel =(pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days = average_travel.days
    hours =average_travel.seconds // (60*60)
    minutes = average_travel.seconds % (60*60) //60
    seconds =average_travel.seconds % (60*60) %60
    print(f'Average travel Time is:{days} days {hours} hours {minutes} minutes {seconds} seconds')          
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(city, df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print(df['User Type'].value_counts().to_frame())
    # Display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts().to_frame())
    # Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is : ',int(df['Birth Year'].min()))
        print('The most recent year of birth is : ',int(df['Birth Year'].max()))
        print('The most common year of birth is : ',int(df['Birth Year'].mode()[0]))
    else:
        print('there is no data for this city')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
def display_raw_data(df):
    """ Ask the user if the he wants to display the raw data and print 5 rows at time"""
    raw= input('would you like to display raw data?')
    if raw.lower() =='yes':
        count=0
        while True:
            print(df.iloc[count: count+5])
            count +=5
            ask=input('next 5 raws?')
            if ask.lower() !='yes':
                break
                
def main():
    while True:
         city, month, day = get_filters()
         df = load_data(city, month, day)
        
        
         time_stats(df)
         station_stats(df)
         trip_duration_stats(df)
         user_stats(city, df)
         display_raw_data(df)
        
        
         restart = input('\nWould you like to restart? Enter yes or no.\n')
         if restart.lower() != 'yes':
            print('thanks')
            break


if __name__ == "__main__":
	main()
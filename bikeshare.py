import pandas as pd
import time
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
def get_filters():    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # get user input for month (all, january, february, ... , june)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    """ while for city  """  
    city = str(input('would you like to see data for Chicago , New York City or Washington \n').title()) 
    while ((city !=  'Chicago') and( city != 'New York City') and (city != 'Washington')) :
         print('please enter city as it is described')
         city = str(input('enter city\n'))
      
    """ while for filter  """    
    filtering =str( input('would you like to filter data by month , day , both or not at all . Type none for no time filter\n').lower())    
    while ((filtering != 'month') and (filtering !='day') and (filtering !='both') and (filtering !='none')) :   
         print('please enter filter as it is described') 
         filtering = str(input('enter filter\n').lower())
          
    """ while for month  """     
    if (filtering == 'month') :
     day = None  
     month = str(input('which month , January , February , March , April , May , June\n').title())
     while (( month != 'January')and (month !='February') and (month !='March') and (month !='April') and (month !='May') and (month !='June')) :
         print('please enter month as it is described')
         month = str(input('enter month\n').title())
         
     """while for day """  
    elif (filtering == 'day') : 
     month = None   
     day = str(input('which day . Please type it as integer e.g. sunday=1 \n '))
     while ((day != '1') and (day !=  '2') and (day != '3') and (day != '4') and (day != '5') and (day != '6') and (day != '7')) :
         print('please enter day as it is described')
         day = input('enter day\n') 
    
    elif filtering == 'both' :
     month = str(input('which month , January , February , March , April , May , June\n').title())
     while (( month != 'January')and (month !='February') and (month !='March') and (month !='April') and (month !='May') and (month !='June')) :
         print('please enter month as it is described')
         month = str(input('enter month\n').title())
     day = str(input('which day . Please type it as integer e.g. sunday=1 \n '))
     while ((day != '1') and (day !=  '2') and (day != '3') and (day != '4') and (day != '5') and (day != '6') and (day != '7')) :
         print('please enter day as it is described')
         day = str(input('enter day\n'))  
         
    else :
        day = None 
        month = None     
    
    print('-'*40)
    return city, month, day,filtering
def load_data(city, month, day,filtering):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if (filtering) == 'month':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
        # filter by month to create the new dataframe
        df = df[df['month'] == month] 
    if (filtering == 'day') :
    # filter by day of week if applicable
        # filter by day of week to create the new dataframe
        days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','saturday']
        day = days[int(day)-1]
        df = df[df['day_of_week'] == day.title()]
    if (filtering == 'both') :
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
        df = df[df['month'] == month]
        days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','saturday']
        day = days[int(day)-1]
        df = df[df['day_of_week'] == day.title()]
    raw_data = str(input('do yo want to see some raw data , please answer with yes or no\n'))
    i =0
    while(raw_data == 'yes') :        
      print(df[i:i+5])
      raw_data = str(input('Do you want to see more data\n'))
      i=i+5
      while ((raw_data != 'yes') and( raw_data != 'no')):
       print('please enter the answer as it is described')
       raw_data = str(input('enter your answer\n'))
    return df 
def time_stats(df,filtering):
  """Displays statistics on the most frequent times of travel."""

  print('\nCalculating The Most Frequent Times of Travel...\n')
  start_time = time.time()
  x=df['month'].value_counts().idxmax()
  y=df['day_of_week'].value_counts().idxmax()
  z=df['Start Time'].dt.hour
  
  if filtering == 'none' :
    print('most common month is {} and it counts {} '.format(x,df['month'].value_counts()[x]))
    print('most common day is {} and it counts {} '.format(y,df['day_of_week'].value_counts()[y]))
    print('most common start hour is {} and it counts {} '.format(z.value_counts().idxmax(),z.value_counts()[z.value_counts().idxmax()]))

  elif filtering =='month' :
    print('most common day is {} and it counts {} '.format(y,df['day_of_week'].value_counts()[y]))
    print('most common start hour is {} and it counts {}'.format(z.value_counts().idxmax(),z.value_counts()[z.value_counts().idxmax()]))

  elif filtering == 'day' :
    print('most common month is {} and it counts {} '.format(x,df['month'].value_counts()[x]))
    print('most common start hour is {} and it counts {} '.format(z.value_counts().idxmax(),z.value_counts()[z.value_counts().idxmax()]))
  
  elif filtering == 'both' :
    print('most common start hour is {} and it counts {} '.format(z.value_counts().idxmax(),z.value_counts()[z.value_counts().idxmax()]))


  print("\nThis took %s seconds." % (time.time() - start_time))
  print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    x=df['Start Station'].value_counts().idxmax()
    print('most commonly used start station is {} and it counts {} '.format(x,df['Start Station'].value_counts()[x]))
    
    # display most commonly used end station
    y=df['End Station'].value_counts().idxmax()
    print('most commonly used end station is {} '.format(y,df['End Station'].value_counts()[y]))

    # display most frequent combination of start station and end station trip
    df["period"]=df["Start Station"] +[' And ']+ df["End Station"]
    z=df['period'].value_counts().idxmax()
    print('most most frequent combination of start station and end station is {} '.format(z,df['period'].value_counts()[z]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('total travel time {}'.format(df['Trip Duration'].sum()))

    # display mean travel time
    print('mean travel time is {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
  
def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    x=df['User Type'].value_counts()['Customer']
    y=df['User Type'].value_counts()['Subscriber']
    df.fillna(0)
    z=df['User Type'].value_counts()[0]
    
    # Display counts of gender
    print('Customer count is {}'.format(x))
    print('Subscriber count is {}'.format(y))
    print('Non defined type of user count is {}'.format(z))
    # Display earliest, most recent, and most common year of birth
    if city == 'Chicago' or city == 'New York city' :
     gen=df['Gender'].value_counts().idxmax()
     print('Earliest year of birth is {}'.format(df['Birth Year'].min()))
     print('Most recent year of birth is {}'.format(df['Birth Year'].max()))
     print('Most common year of birth is {}'.format(df['Birth Year'].value_counts().idxmax()))
     print('Most common gender is {} and counts {}'.format(gen,df['Gender'].value_counts()[gen]))
     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day,filtering = get_filters()
        df = load_data(city, month, day, filtering)
        time_stats(df,filtering)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    

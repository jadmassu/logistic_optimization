import pandas as pd

class WeekdayAdder:
    def __init__(self, df,date_column='Trip Start Time'):
        self.date_column = date_column
        self.df = df

    def is_weekday(self, date):
        return date.weekday() < 5  # Monday=0, Sunday=6; weekdays are 0 to 4

    def add_weekday_column(self,):
        
        try:
            self.df[self.date_column] = pd.to_datetime(self.df[self.date_column])  # Ensure the date column is in datetime format
            self.df['Weekday'] = self.df[self.date_column].apply(self.is_weekday)
            return self.df
        except KeyError:
            print(f"Error: Column '{self.date_column}' not found in DataFrame.")
        
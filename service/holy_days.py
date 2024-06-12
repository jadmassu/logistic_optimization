import requests
class HolidayFetcher:
    def __init__(self, api_key, country,date):
        self.api_key = api_key
        self.country = country
        self.date = date
        self.holidays_cache = {}

    def get_holidays(self, year):
        if year in self.holidays_cache:
            return self.holidays_cache[year]

        url = 'https://calendarific.com/api/v2/holidays'
        params = {
            'api_key': self.api_key,
            'country': self.country,
            'year': year
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            holidays = response.json().get('response', {}).get('holidays', [])
            holiday_dates = [holiday['date']['iso'] for holiday in holidays]
            self.holidays_cache[year] = holiday_dates
            return holiday_dates
        else:
            print(f"Error: {response.status_code}")
            return []

    def get_holidays_for_dates(self):
        holidays_for_dates = {}
        for date in self.date:
            year = date.year
            date_str = date.isoformat()

            # Fetch holidays if not already fetched for the year
            if year not in self.holidays_cache:
                self.holidays_cache[year] = self.get_holidays(year)

            # Check if there are holidays in the fetched data
            if self.holidays_cache[year]:
                holidays_for_dates[date_str] = [holiday for holiday in self.holidays_cache[year] if holiday.startswith(date_str)]
            else:
                holidays_for_dates[date_str] = []

        return holidays_for_dates

    def add_holiday_column(self, df, date_column_name='Trip Start Time'):
        # Fetch holidays for the given dates
        holidays = self.get_holidays_for_dates()

        # Add 'Holiday' column to DataFrame
        df['Holiday'] = df[date_column_name].apply(lambda x: any(x.date().isoformat() in holidays[date.isoformat()] for date in self.dates))
        return df

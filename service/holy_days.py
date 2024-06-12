import requests

def get_holidays(year, country):
    api_key = 'your_api_key'  # Replace with your actual API key
    url = 'https://calendarific.com/api/v2/holidays'
    params = {
        'api_key': api_key,
        'country': country,
        'year': year
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        holidays = response.json()['response']['holidays']
        holiday_dates = [holiday['date']['iso'] for holiday in holidays]
        return holiday_dates
    else:
        print(f"Error: {response.status_code}")
        return []
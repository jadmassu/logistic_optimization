import requests

def get_historical_weather(lat, lon, timestamp, api_key):
    url = f"https://api.openweathermap.org/data/3.0/onecall/timemachine"
    params = {
        'lat': lat,
        'lon': lon,
        'dt': timestamp,
        'appid': api_key,
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

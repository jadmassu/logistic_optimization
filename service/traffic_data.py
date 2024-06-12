import requests


def get_traffic_data(lat, lng, date_time,api_key):
        endpoint = "https://traffic.ls.hereapi.com/traffic/6.3/incidents.json"
        params = {
            'apiKey': api_key,
            'bbox': f"{lat-0.05},{lng-0.05};{lat+0.05},{lng+0.05}",
            'criticality': 'critical,major'
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        return data
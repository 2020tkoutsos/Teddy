import json, requests, datetime

def api_url(url):
    data = requests.get(url).json()
    icon = data["currently"]["icon"]
    print(icon)

api_url("https://api.darksky.net/forecast/5067bfddeeb2992069bd822ea8c91722/37.8267,-122.4233")

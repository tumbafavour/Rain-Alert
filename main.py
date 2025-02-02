import os
import requests
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

account_sid = ""
auth_token = ""
api_key = ""
LAT = "8.117936657463511"
LNG = "5.084163687677444"
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

weather_params = {
    "lat": LAT,
    "lon": LNG,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

# response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    # client = Client(account_sid, auth_token, http_client=proxy_client)
    # message = client.messages \
    #     .create(
    #         body="It's going to rain today. Remember to bring an umbrella☔",
    #         from_="",
    #         to="",
    #     )

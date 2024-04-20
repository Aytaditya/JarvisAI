import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return weather_description, temperature, humidity
    else:
        print("Error:", data['message'])
        return None

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
api_key = 'YOUR_API_KEY'
city_name = 'New York'  # Replace with the name of the city you want weather updates for

weather_data = get_weather(city_name, api_key)
if weather_data is not None:
    weather_description, temperature, humidity = weather_data
    print(f"The weather in {city_name} is {weather_description}.")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")

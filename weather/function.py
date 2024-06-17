from config.environment import weather_api_key, api_url


async def fetch_weather(session, city_name):
    # Параметры запроса к API
    params = {
        'key': weather_api_key,
        'q': city_name,
        'days': 1
    }

    async with session.get(api_url, params=params) as response:
        data = await response.json()

        # Извлечение нужных данных из ответа
        forecast = data['forecast']['forecastday'][0]['day']
        transformed_data = {
            "max_temp": forecast["maxtemp_c"],
            "min_temp": forecast["mintemp_c"],
            "maxwind_kph": forecast["maxwind_kph"],
            "daily_chance_of_rain": forecast["daily_chance_of_rain"],
            "daily_chance_of_snow": forecast["daily_chance_of_snow"],
            "totalprecip_mm": forecast["totalprecip_mm"]
        }
        return transformed_data

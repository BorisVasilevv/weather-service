# TravelRouteBuilder

## Описание запросов

```/weather/<string:city_name> ['GET']``` Принимает json вида:

Возвращает json вида:
```json
{
    "daily_chance_of_rain": 88,
    "daily_chance_of_snow": 0,
    "max_temp": 31.6,
    "maxwind_kph": 17.3,
    "min_temp": 19.0,
    "totalprecip_mm": 1.55
}
```
## Команды для разворота в docker

```
git clone https://github.com/AlexaLeonid/WetherService.git //
```

```
cd WetherService
```

```docker build -t weatherService .``` // создаем image проекта

```docker run -p 7777:7777 --name weatherService weatherService``` // создаем docker container

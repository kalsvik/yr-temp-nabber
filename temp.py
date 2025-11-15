import urllib.request
import json

DICTIONARY = {
    "clearsky_day": "clear sky day",
    "clearsky_night": "clear sky night",
    "clearsky_polartwilight": "clear sky polartwilight",
    "fair_day": "fair day",
    "fair_night": "fair night",
    "fair_polartwilight": "fair polartwilight",
    "partlycloudy_day": "partly cloudy day",
    "partlycloudy_night": "partly cloudy night",
    "partlycloudy_polartwilight": "partly cloudy polartwilight",
    "cloudy": "cloudy",
    "rainshowers_day": "rain showers day",
    "rainshowers_night": "rain showers night",
    "rainshowers_polartwilight": "rain showers polartwilight",
    "rainshowersandthunder_day": "rain showers and thunder day",
    "rainshowersandthunder_night": "rain showers and thunder night",
    "rainshowersandthunder_polartwilight": "rain showers and thunder polartwilight",
    "sleetshowers_day": "sleet showers day",
    "sleetshowers_night": "sleet showers night",
    "sleetshowers_polartwilight": "sleet showers polartwilight",
    "snowshowers_day": "snow showers day",
    "snowshowers_night": "snow showers night",
    "snowshowers_polartwilight": "snow showers polartwilight",
    "rain": "rain",
    "heavyrain": "heavy rain",
    "heavyrainandthunder": "heavy rain and thunder",
    "sleet": "sleet",
    "snow": "snow",
    "snowandthunder": "snow and thunder",
    "fog": "fog",
    "sleetshowersandthunder_day": "sleet showers and thunder day",
    "sleetshowersandthunder_night": "sleet showers and thunder night",
    "sleetshowersandthunder_polartwilight": "sleet showers and thunder polartwilight",
    "snowshowersandthunder_day": "snow showers and thunder day",
    "snowshowersandthunder_night": "snow showers and thunder night",
    "snowshowersandthunder_polartwilight": "snow showers and thunder polartwilight",
    "rainandthunder": "rain and thunder",
    "sleetandthunder": "sleet and thunder",
    "lightrainshowersandthunder_day": "light rain showers and thunder day",
    "lightrainshowersandthunder_night": "light rain showers and thunder night",
    "lightrainshowersandthunder_polartwilight": "light rain showers and thunder polartwilight",
    "heavyrainshowersandthunder_day": "heavy rain showers and thunder day",
    "heavyrainshowersandthunder_night": "heavy rain showers and thunder night",
    "heavyrainshowersandthunder_polartwilight": "heavy rain showers and thunder polartwilight",
    "lightssleetshowersandthunder_day": "light sleet showers and thunder day",
    "lightssleetshowersandthunder_night": "light sleet showers and thunder night",
    "lightssleetshowersandthunder_polartwilight": "light sleet showers and thunder polartwilight",
    "heavysleetshowersandthunder_day": "heavy sleet showers and thunder day",
    "heavysleetshowersandthunder_night": "heavy sleet showers and thunder night",
    "heavysleetshowersandthunder_polartwilight": "heavy sleet showers and thunder polartwilight",
    "lightssnowshowersandthunder_day": "light snow showers and thunder day",
    "lightssnowshowersandthunder_night": "light snow showers and thunder night",
    "lightssnowshowersandthunder_polartwilight": "light snow showers and thunder polartwilight",
    "heavysnowshowersandthunder_day": "heavy snow showers and thunder day",
    "heavysnowshowersandthunder_night": "heavy snow showers and thunder night",
    "heavysnowshowersandthunder_polartwilight": "heavy snow showers and thunder polartwilight",
    "lightrainandthunder": "light rain and thunder",
    "lightsleetandthunder": "light sleet and thunder",
    "heavysleetandthunder": "heavy sleet and thunder",
    "lightsnowandthunder": "light now and thunder",
    "heavysnowandthunder": "heavy snow and thunder",
    "lightrainshowers_day": "light rain showers day",
    "lightrainshowers_night": "light rain showers night",
    "lightrainshowers_polartwilight": "light rain showers polartwilight",
    "heavyrainshowers_day": "heavy rain showers day",
    "heavyrainshowers_night": "heavy rain showers night",
    "heavyrainshowers_polartwilight": "heavy rain showers polartwilight",
    "lightsleetshowers_day": "light sleet showers day",
    "lightsleetshowers_night": "light sleet showers night",
    "lightsleetshowers_polartwilight": "light sleet showers polartwilight",
    "heavysleetshowers_day": "heavy sleet showers day",
    "heavysleetshowers_night": "heavy sleet showers night",
    "heavysleetshowers_polartwilight": "heavy sleet showers polartwilight",
    "lightsnowshowers_day": "light now showers day",
    "lightsnowshowers_night": "light now showers night",
    "lightsnowshowers_polartwilight": "light now showers polartwilight",
    "heavysnowshowers_day": "heavy snow showers day",
    "heavysnowshowers_night": "heavy snow showers night",
    "heavysnowshowers_polartwilight": "heavy snow showers polartwilight",
    "lightrain": "light rain",
    "lightsleet": "light sleet",
    "heavysleet": "heavy sleet",
    "lightsnow": "light now",
    "heavysnow": "heavy snow",
}

# thank you, government funded weather report website
# bergen, norway

YR_LINK = "https://www.yr.no/api/v0/locations/1-92416/forecast/currenthour"


def getRelevantSymbol(description: str):
    if "rain" in description:
        if "thunder" in description:
            return "⛈️"
        return "🌧️"

    if "snow" in description:
        if "thunder" in description:
            return "⛈️"
        return "🌨️"

    if "sleet" in description:
        if "thunder" in description:
            return "⛈️"
        return "🌨️"

    if "fair" in description:
        if "night" in description:
            return "🌙"
        return "🌤️"

    if "clear sky" in description:
        if "night" in description:
            return "🌙"
        return "☀️"

    if "fog" in description:
        return "😶‍🌫️"

    return "?"


with urllib.request.urlopen(YR_LINK) as response:
    result = json.loads(response.read())
    symbol_code = str(result["symbolCode"]["next1Hour"])
    weather_description = DICTIONARY[symbol_code]
    emoji = getRelevantSymbol(weather_description)
    finalObject = {
        "text": f"{emoji} {result["temperature"]["value"]}",
        "tooltip": weather_description,
    }
    print(json.dumps(finalObject))

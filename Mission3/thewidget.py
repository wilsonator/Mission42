import customtkinter
import asyncio
import python_weather


async def getWeather(location) -> None:

  # Declare the client. The measuring unit used defaults to the metric system (celcius, km/h, etc.)
  async with python_weather.Client(unit=python_weather.IMPERIAL) as client:

    # Fetch a weather forecast from a city.
    weather = await client.get(location)

    # Fetch the temperature for today.
    return weather.temperature


def getAndDisplayLocations():
  locations = ["Charlotte", "New York", "Frankfurt", "Los Angeles"]
  for i in range (0, len(locations)):
    temp = asyncio.run(getWeather(locations[i]))
    appendedString = "The weather in: " + locations[i] + " is " + str(temp) + " Farhenheit"
    if temp <= 35:
        emoji = "🥶"
    elif  35 < temp < 80:
        emoji = "😎"
    else:
        emoji = "🥵"
    label=customtkinter.CTkLabel(app, text=appendedString + emoji + "\n")
    label.pack()
    


app = customtkinter.CTk()
app.title("Weather App")
app.geometry("600x250")
# everything goes here
getAndDisplayLocations()


app.mainloop()




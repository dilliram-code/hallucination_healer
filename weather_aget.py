import os 
import requests

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool 
from langchain_google_genai import ChatGoogleGenerativeAI

# load env varialbes
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
WEATHER_API_KEY=os.getenv("WEATHER_API_KEY")

if not GEMINI_API_KEY:
  raise ValueError("GEMINI_API_KEY is missing from .env")

if not WEATHER_API_KEY:
  raise ValueError("WEATHER_API_KEY is missing from .env")

# create the weather tool
@tool
def get_weather_data(city: str) -> str:
  
  url = "https://api.weatherstack.com/current"
  
  params = {
    "access_key": WEATHER_API_KEY,
    "query": city
  }
  
  try:
    response = requests.get(
      url,
      params,
      timeout=10
    )
    
    # raise an error for HTTPException
    response.raise_for_status()
    
    data = response.json()
    
    # weatherstack can return api level error 
    if "error" in data:
      return f"Weather API error: {data['error']}"
    
    # extract useful information
    location = data.get("location", {})
    current = data.get("current", {})

    city_name = location.get("name", city)
    country = location.get("country", "")

    temperature = current.get("temperature")
    feels_like = current.get("feelslike")
    humidity = current.get("humidity")
    wind_speed = current.get("wind_speed")
    description = current.get("weather_descriptions", ["Unknown"])[0]
    
    # return result
    result = (
            f"Weather in {city_name}, {country}:\n"
            f"Condition: {description}\n"
            f"Temperature: {temperature}°C\n"
            f"Feels like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind speed: {wind_speed} km/h"
        )

    return result
  
  # except block
  except requests.exceptions.Timeout:
    return "Weather API request timed out."
  
  except requests.exceptions.RequestException as e:
    return f"Weather API request failed: {e}"
  
  except Exception as e:
    return f"Unexpected error while getting weather: {e}"
  
  # create google gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0,
    google_api_key=GEMINI_API_KEY
)
  
# register tools 
tools = [
  get_weather_data
]

# create the agent
agent = create_agent(
  model=llm,
  tools=tools,
  system_prompt=(
    "You are a helpful weather assistant. "
    "When the user asks about current weather, "
    "always use the get_weather_data tool. "
    "Do not guess weather information. "
    "After receiving the tool result, explain it clearly "
    "to the user."
  )
)

# run the agent
if __name__ == "__main__":
  user_input = input("You:")
  result = agent.invoke(
    {
      "messages": [
      { 
        "role": "user",
        "content": user_input
        }
      ]
    }
  )
  
  # print the result
  print("Agent:", result["messages"][-1].content)
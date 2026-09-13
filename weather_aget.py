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

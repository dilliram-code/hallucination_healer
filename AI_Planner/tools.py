from datetime import datetime
import secrets
import string 
import random 

def get_current_time():
  """Return the current time."""
  
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def generate_password(length=12):
  """Generate a random password."""
  
  characters = string.ascii_letters + string.digits + "!@#$%^&*"
  password = "".join(
    secrets.choice(characters) for _ in range(length)
  )
  
  return password
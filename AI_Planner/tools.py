from datetime import datetime
import secrets
import string 
import random 

def get_current_time():
  """Return the current time."""
  
  return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


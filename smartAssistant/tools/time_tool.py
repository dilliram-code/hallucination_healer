from datetime import datetime

def get_current_time():
  """Returns current date and time"""
  
  now = datetime.now()
  
  return now.strftime("%d %B %Y, %I:%M:%S %p")
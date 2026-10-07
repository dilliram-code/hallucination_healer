def choose_tool(user_input):
  
  user_input = user_input.lower()
  
  if "time" in user_input:
    return "get_current_time"
  
  elif "password" in user_input:
    return "generate_password"
  
  elif "dice" in user_input or "roll" in user_input:
    return "roll_dice"
  
  else:
    return "none"
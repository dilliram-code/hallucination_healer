from planner import choose_tool

from tools import (
  get_current_time,
  generate_password,
  roll_dice
)

def run_assistant(user_input):
  
  tool_name = choose_tool(user_input)
  
  if tool_name == 'get_current_time':
    result = get_current_time()
  
  elif tool_name == 'generate_password':
    result = generate_password()
  
  elif tool_name == 'roll_dice':
    result = roll_dice()
  
  else:
    result = "I don't know how to handle that request."
  
  return result
  
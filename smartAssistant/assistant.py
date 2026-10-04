from tool_manager import ToolManager
from ai_model import get_ai_response


class Assistant:

    def __init__(self):
        self.tool_manager = ToolManager()

    def respond_to_user(self, user_input):

        tool_result = self.tool_manager.execute_tool(
            user_input
        )

        if tool_result:
            return tool_result

        return get_ai_response(user_input)
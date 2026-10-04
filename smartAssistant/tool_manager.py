from tools.time_tool import get_current_time
from tools.calculator_tool import calculate
from tools.student_tool import get_student_info

class ToolManager:
    def execute_tool(self, user_input):
        """
        Determine whether a tool should handle the user input.

        Returns:
            str | None:
                Tool result if a tool was used.
                None if no tool matches.
        """

        user_input = user_input.lower()

        if "time" in user_input:
            return get_current_time()

        if "calculate" in user_input:
            expression = user_input.replace("calculate", "").strip()

            return calculate(expression)

        if "student" in user_input:
            return get_student_info(101)

        return None
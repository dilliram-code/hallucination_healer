import ast

def calculate(expression):
    """
    Calculate a basic mathematical expression safely.
    """
    try:
        # ast.literal_eval only evaluates safe literals, preventing malicious code execution
        result = ast.literal_eval(expression)
        return str(result)
    except Exception:
        return "Sorry, I could not calculate that."

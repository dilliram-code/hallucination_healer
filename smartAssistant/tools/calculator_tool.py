def calculate(expression):
    """
    Calculate a basic mathematical expression.

    Example:
        calculate("10 + 20")
    """

    try:
        result = eval(expression)

        return str(result)

    except Exception:
        return "Sorry, I could not calculate that."
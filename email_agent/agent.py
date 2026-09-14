import os
import json

from dotenv import load_dotenv
from google import genai

from email_tool import send_email


load_dotenv()


# ---------------------------------------------------------
# 1. Create Gemini client
# ---------------------------------------------------------

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ---------------------------------------------------------
# 2. Define the tool
# ---------------------------------------------------------

send_email_tool = {
    "type": "function",

    "name": "send_email",

    "description": (
        "Send an email to a recipient. "
        "Use this function only when the user explicitly "
        "asks to send an email."
    ),

    "parameters": {
        "type": "object",

        "properties": {

            "recipient": {
                "type": "string",
                "description": (
                    "The recipient's email address."
                )
            },

            "subject": {
                "type": "string",
                "description": (
                    "The subject line of the email."
                )
            },

            "body": {
                "type": "string",
                "description": (
                    "The complete email body."
                )
            }
        },

        "required": [
            "recipient",
            "subject",
            "body"
        ]
    }
}


# ---------------------------------------------------------
# 3. System instructions
# ---------------------------------------------------------

SYSTEM_INSTRUCTION = """
You are an Email Writing and Sending Agent.

Your job is to help the user write professional emails
and send them when requested.

You have access to one tool:

send_email

Rules:

1. Help the user write clear and natural emails.

2. If the user only asks you to WRITE an email,
   do not send it.

3. If the user explicitly asks you to SEND an email,
   use the send_email tool.

4. Never invent a recipient email address.

5. If the user wants to send an email but has not
   provided a recipient email address, ask for it.

6. Create an appropriate subject if the user has not
   provided one.

7. Keep emails natural and professional.

8. Before sending an email, make sure you have:
   - recipient
   - subject
   - body

9. After the tool successfully sends the email,
   clearly tell the user that it was sent.

10. Never expose API keys, passwords, or other secrets.
"""


# ---------------------------------------------------------
# 4. Available Python functions
# ---------------------------------------------------------

available_functions = {
    "send_email": send_email
}


# ---------------------------------------------------------
# 5. Agent function
# ---------------------------------------------------------

def run_agent(user_input: str):

    interaction = client.interactions.create(

        model="gemini-3.6-flash",

        system_instruction=SYSTEM_INSTRUCTION,

        input=user_input,

        tools=[
            send_email_tool
        ]
    )

    # -----------------------------------------------------
    # Check whether Gemini requested a tool call
    # -----------------------------------------------------

    function_results = []

    for step in interaction.steps:

        if step.type == "function_call":

            print(
                f"\nTool requested: {step.name}"
            )

            print(
                f"Arguments: {step.arguments}"
            )

            # Get the actual Python function
            function = available_functions.get(
                step.name
            )

            if function is None:

                result = {
                    "error": f"Unknown tool: {step.name}"
                }

            else:

                # Arguments returned by Gemini
                arguments = step.arguments

                # Execute Python function
                result = function(
                    **arguments
                )

            # Send result back to Gemini
            function_results.append({

                "type": "function_result",

                "name": step.name,

                "call_id": step.id,

                "result": [
                    {
                        "type": "text",
                        "text": json.dumps(result)
                    }
                ]
            })

    # -----------------------------------------------------
    # If Gemini called a tool, continue the interaction
    # -----------------------------------------------------

    if function_results:

        final_interaction = client.interactions.create(

            model="gemini-3.6-flash",

            previous_interaction_id=interaction.id,

            input=function_results,

            tools=[
                send_email_tool
            ]
        )

        return final_interaction.output_text

    # -----------------------------------------------------
    # Otherwise just return Gemini's answer
    # -----------------------------------------------------

    return interaction.output_text
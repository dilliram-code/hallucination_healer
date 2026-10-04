from assistant import Assistant


def main():

    assistant = Assistant()

    print("=" * 40)
    print("       SMART ASSISTANT")
    print("=" * 40)

    print("Available examples:")
    print("- What is the time?")
    print("- Calculate 10 + 20")
    print("- Show student information")
    print("- What is Python?")
    print("- Type 'exit' to quit.")

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Assistant: Goodbye!")
            break

        response = assistant.respond_to_user(
            user_input
        )

        print(f"Assistant: {response}")


if __name__ == "__main__":
    main()
from agent import run_agent


def main():

    print("=" * 60)
    print("        GEMINI EMAIL AGENT")
    print("=" * 60)

    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:

            response = run_agent(user_input)

            print("\nAgent:")
            print(response)
            print()

        except Exception as e:

            print("\nError:")
            print(e)


if __name__ == "__main__":
    main()
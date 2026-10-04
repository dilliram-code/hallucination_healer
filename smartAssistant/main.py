from assistant import Assistant


def main():

    assistant = Assistant()

    print("Smart Assistant")
    print("Type 'exit' to quit.")

    while True:

        user_input = input("\nYou: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = assistant.respond_to_user(
            user_input
        )

        print("Assistant:", response)


if __name__ == "__main__":
    main()
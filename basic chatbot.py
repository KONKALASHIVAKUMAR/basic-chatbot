def chatbot_response(user_input):
    user_input = user_input.lower()

    # Predefined responses
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I'm just a chatbot, but I'm here to help you!",
        "what's your name": "I'm Chatbot, your virtual assistant!",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! Let me know if you need anything else.",
    }

    # Fallback response for unrecognized input
    fallback_response = "I'm not sure I understand. Can you please clarify?"

    # Match user input to responses
    return responses.get(user_input, fallback_response)


def main():
    print("Chatbot: Hello! I'm here to chat with you. Type 'bye' to end the conversation.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()

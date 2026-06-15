import re

RESPONSES = [
    (r"\b(hi|hello|hey|good\s*(morning|afternoon|evening))\b", "Hello! How can I help you today?"),
    (r"\b(what\s*is\s*your\s*name|who\s*are\s*you)\b", "I'm a simple chatbot built to answer common questions."),
    (r"\b(how\s*are\s*you|how's\s*it\s*going)\b", "I'm just code, but I'm doing great! What can I help you with?"),
    (r"\b(weather|temperature|forecast)\b", "I don't have live weather data, but I can still chat with you."),
    (r"\b(time|current\s*time)\b", "I don't track the clock, but I can help answer questions."),
    (r"\b(thank(s| you)|thanks)\b", "You're welcome! Let me know if you have another question."),
    (r"\b(bye|goodbye|see you|farewell)\b", "Goodbye! Have a great day!"),
]

DEFAULT_RESPONSE = (
    "I'm not sure about that yet. "
    "Try asking about greetings, my name, or say 'bye' to exit."
)


def find_response(user_text: str) -> str:
    """Choose a response based on simple pattern matching."""
    normalized = user_text.strip().lower()
    for pattern, response in RESPONSES:
        if re.search(pattern, normalized):
            return response
    return DEFAULT_RESPONSE


def main() -> None:
    print("Simple Chatbot")
    print("Type a message and press Enter. Type 'quit' or 'exit' to stop.")

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            print("Bot: Please enter a message so I can respond.")
            continue

        if re.search(r"\b(quit|exit|bye|goodbye)\b", user_input.lower()):
            print("Bot: Goodbye! It was nice chatting with you.")
            break

        response = find_response(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()

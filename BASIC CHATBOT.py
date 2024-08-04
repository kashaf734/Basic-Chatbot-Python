import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data
nltk.download('punkt')

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"what is your name?",
        ["I am a bot created by you. You can call me Chatbot.",]
    ],
    [
        r"how are you?",
        ["I am doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that. How can I help you?",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon.",]
    ],
    [
        r"(.*) (location|city) ?",
        ['I am just a computer program, so I do not have a location.']
    ],
    [
        r"(.*) created (.*)",
        ["I was created by a user using Python and NLTK.",]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I am not sure about the weather, but it's always sunny in the virtual world.",]
    ],
    [
        r"what is (.*) ?",
        ["I am not sure, but you can search it online."]
    ],
]

# Creating a chatbot instance
chatbot = Chat(pairs, reflections)

def chatbot_interface():
    print("Hi, I am your chatbot. How can I assist you today?")
    print("Type 'quit' to exit the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Bye, take care. See you soon.")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot_interface()

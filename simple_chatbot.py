def chatbot_reply(user_message):

    user_message = user_message.lower().strip()

    greetings = ["hello", "hi", "hey"]
    how_are_you = ["how are you", "how are you doing"]
    name_questions = ["what is your name", "who are you"]
    thanks_words = ["thanks", "thank you"]
    bye_words = ["bye", "goodbye", "exit"]

    if user_message in greetings:
        return "Hello!"

    elif user_message in how_are_you:
        return "I'm fine, thanks for asking!"

    elif user_message in name_questions:
        return "I am SimpleBot, your Python chatbot."

    elif user_message == "help":
        return "You can say: hello, how are you, thanks, bye"

    elif user_message in thanks_words:
        return "You are welcome!"

    elif user_message in bye_words:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I don't understand that."


print(" --------- Welcome to SimpleBot --------- ")
print("Type 'bye' to stop the chat.\n")

while True:

    user_input = input("You: ")
    response = chatbot_reply(user_input)
    print("Bot:", response)

    if user_input.lower() in ["bye", "goodbye", "exit"]:
        break
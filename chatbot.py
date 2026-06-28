# CodeAlpha Task 4 - Basic Rule-based Chatbot
# Name: Pramela Naravkar
# Internship: CodeAlpha Python Programming

print("=" * 40)
print("   CodeAlpha Task 4 - Basic Chatbot")
print("=" * 40)
print("Chatbot: Hello! I'm your CodeAlpha Chatbot.")
print("Chatbot: Type 'bye' to exit the chat.\n")

while True:
    user_input = input("You: ").lower().strip()
    
    if user_input == "hello" or user_input == "hi" or user_input == "hey":
        print("Chatbot: Hi there! Nice to meet you 😊")
        
    elif user_input == "how are you" or user_input == "how are you?":
        print("Chatbot: I'm doing great, thanks for asking! How about you?")
        
    elif user_input == "what is your name" or user_input == "name":
        print("Chatbot: I'm CodeAlpha Bot, created for Task 4!")
        
    elif user_input == "bye" or user_input == "exit" or user_input == "quit":
        print("Chatbot: Goodbye! Thanks for chatting. Have a great day! 👋")
        break
        
    elif user_input == "":
        print("Chatbot: You didn't say anything. Type something!")
        
    else:
        print("Chatbot: Sorry, I don't understand. Try 'hello', 'how are you', or 'bye'")

print("\nChat ended.")

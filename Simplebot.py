def simple_chatbot(user_input):
    if "hello" in user_input.lower():
        return "Hi! How are you"

    elif "fine" in user_input.lower():
        return "Good,Whats happening your project"

    elif "still Processing" in user_input.lower():
        return "Great,Are you Applying Any job"
    
    elif "no" in user_input.lower():
        return "Apply fast"

    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Main loop
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break

    response = simple_chatbot(user_input)
    print("Chatbot:", response)


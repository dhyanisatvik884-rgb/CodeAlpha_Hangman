def chat_begin():
    print("\nGREETINGS!! Welcome to the Chatbot.")
    while True:
        state = input(">>>  ").lower()
        if state == "hello" or state == "hi":
            print("Hello, How are you??")
        elif state == "i am fine":
            print("Good to hear that.")
        elif state == "how are you":
            print("I am fine, thanks!")
        elif state == "bye" or state == "goodbye":
            print("Goodbye, See you later!!")
            break
        else:
            print("SORRY! I don't understand???")
chat_begin()
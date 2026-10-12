import pyjokes

for i in range(3):
    joke = pyjokes.get_joke()
    print(f"Joke {i + 1}: {joke}")

while True:
    user_input = input("Do you want to hear another joke? (yes/no): ").strip().lower()
    if user_input.lower() == "yes":
        joke = pyjokes.get_joke()
        print(f"Here's another joke: {joke}")
    elif user_input.lower() == "no":
        print("Okay, have a great day!")
        break
    else:
        print("Please answer with 'yes' or 'no'.")


import emoji

name = input("Enter your name: ")

print(emoji.emojize(f"Hello {name}! :smile:", language="alias"))
print(emoji.emojize("I love Python :heart:", language="alias"))

activity = input("What is your favorite activity? ")
print(emoji.emojize(f"Keep learning {activity}:thumbsup:", language="alias"))


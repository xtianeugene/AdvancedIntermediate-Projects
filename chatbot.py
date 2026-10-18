import re

RULES = [
    (r"\bhi\b|\bhello\b", "Hello there!"),
    (r"\bhow are you\b", "I'm just code, but thanks for asking."),
    (r"\byour name\b", "I'm Pybot."),
    (r"\bbye\b", "Goodbye!"),
]

def respond(text):
    for pattern, reply in RULES:
        if re.search(pattern, text, re.I):
            return reply
        return "I don't understand."

if __name__ == "__main__":
    while True:
        msg = input("You: ")
        print("Bot:", respond(msg))
        if re.search(r"\bbye\b", msg, re.I):
            break
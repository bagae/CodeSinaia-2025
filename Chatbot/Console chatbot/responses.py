import random

R_Eating = ["I don't like eating.", "I run on code, not food!", "Bots don't need to eat 😄"]
COLOURS = ["red", "blue", "green", "yellow", "purple", "orange"]
COLOURS_HEARTS = ["❤️", "💙", "💚", "💛", "💜", "🧡"]

def get_custom_response(topic):
    if topic == "eat":
        return random.choice(R_Eating)
    else:
        a = random.choice(COLOURS)
        return a + COLOURS_HEARTS[COLOURS.index(a)]
    return "Hmm... I don't know how to respond to that."

def unknown():
    responses = [
        "Could you please rephrase that?",
        "Hmm... I didn't quite get that.",
        "What does that mean? 🤔",
        "I'm not sure I understand."
    ]
    return random.choice(responses)
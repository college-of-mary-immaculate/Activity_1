import json
import random
import re


base_memory_file = "memory.json"


dict_responses = {  

    "cap": [
        "you lyin........ get out!",
        "shut up, that's a joke",
        "come one, spit something",
    ],

    "no cap" : [
        "Fr, For Real, Oh My God!",
        "No cap detected, Real Talk",
        "You didn't lie, my Friend",
        "Oh no! No Way!",
        "So Tru Brah"
    ],

    "bet" : [
        "Agreed to yo all",
        "I bet on that.......",
        "Cool, Ya Bruh I like that",
    ],
    
    "rizz": [
        "W rizz or L rizz? ",
        "Unspoken rizz right there.",
        "Bro thinks they have infinite rizz.",
    ],
    "slay": [
        "Ate and left no crumbs! ",
        "Absolute queen behavior.",
        "Slaying all day, everyday.",
        "Fire...............",
    ],
    "skibidi": [
        "Ohio moment...",
        "Please don't brainrot me further. ",
        "What in the sigma...",
    ],

    "mid" : [
        "not enough maxxing, average!",
        "is that your rizzing about?",
        "Meh, give a B............",
        "Is that it?",
    ],

    "gyatt": ["Bro is down astronomically. ", "Calm down, chill out!"],
    "delulu": [
        "Delulu is the solulu, I guess. ",
        "Manifesting for you, bestie.",
    ],
    "hello": [
        "Yo! What's good?",
        "Wassup bestie!",
        "Hey! Ready to chat or what?",
    ],
    
    "sus": [
        "You so......... weirdass",
        "Eeeee!!!!!!!!!! gross",
        "What the..........?",
    ]
        
}

def load_memory():
    try:
        with open(base_memory_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(base_memory_file, "w") as f:
            json.dump(dict_responses, f, indent=4)
        return dict_responses
    
def save_memory(memory):
    with open(base_memory_file, "w") as f:
        json.dump(memory, f, indent=4)


def clean_input(text):
    text = text.lower().strip()
    return re.sub(r"[^\w\s]", "", text)


def get_response(user_input, memory):
    cleaned = clean_input(user_input)


    if cleaned in memory:
        return random.choice(memory[cleaned])

    for key in memory:
        if key in cleaned:
            return random.choice(memory[key])

    return None


def main():
    memory = load_memory()
    print("🤖 Bot: Yo! I'm ready. Type 'quit' to exit.")
    print("--------------------------------------------------")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() == "quit":
            print("🤖 Bot: Peace out! ✌️")
            break

        response = get_response(user_input, memory)

        if response:
            print(f"🤖 Bot: {response}")
        else:
            print("🤖 Bot: I don't know how to respond to that. 🥺")
            teach = input("Teach me! What should I reply to that? ").strip()

            if teach:
                cleaned_key = clean_input(user_input)
                if cleaned_key not in memory:
                    memory[cleaned_key] = []

                memory[cleaned_key].append(teach)
                save_memory(memory)
                print("🤖 Bot: Bet! I learned it. Try asking me again!")


if __name__ == "__main__":
    main()

import json
import os
import random
import re


base_memory_file = "memory.json"


dict_responses = {  

    "cap": [
        "you lyin........ get out!",
        "shut up, that's a joke",
        "come on, spit something",
    ],

    "no cap": [
        "Fr, For Real, Oh My God!",
        "No cap detected, Real Talk",
        "You didn't lie, my Friend",
        "Oh no! No Way!",
        "So Tru Brah"
    ],

    "bet": [
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

    "mid": [
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

    "hi": [
        "Yo!",
        "Hey there!",
        "Wassup!",
    ],

    "how are you": [
        "Living my best life!",
        "Just vibing, what about you?",
        "All good here, ready to chat!"
    ],

    "bye": [
        "Peace out! ✌️",
        "Catch ya later!",
        "Bye bestie, stay safe!"
    ],

    "thanks": [
        "Anytime! 🫡",
        "No problem at all!",
        "You know it, anytime!"
    ],

    "sus": [
        "You so......... weirdass",
        "Eeeee!!!!!!!!!! gross",
        "What the..........?",
    ],

    "default": [
        "That's wild! Tell me more.",
        "Hmm, interesting! What else is on your mind?",
        "I hear you, bestie!",
        "Say less, keep going!",
        "Not sure about that one, but I'm listening!",
        "Oh really? That's crazy."
    ]
}


def clear_screen():
    """Clears the console screen using OS-specific commands."""
    os.system("cls" if os.name == "nt" else "clear")


def load_memory():
    """Robust memory loading using the os library to check file existence and size."""
    if os.path.exists(base_memory_file) and os.path.getsize(base_memory_file) > 0:
        try:
            with open(base_memory_file, "r") as f:
                data = json.load(f)
                updated = False
                for k, v in dict_responses.items():
                    if k not in data:
                        data[k] = v
                        updated = True
                if updated:
                    save_memory(data)
                return data
        except json.JSONDecodeError:
            print("⚠️ Memory file was corrupted. Re-initializing default memory...")

    # Create/reset memory file if missing or corrupted
    save_memory(dict_responses)
    return dict_responses
    

def save_memory(memory):
    """Saves memory back to JSON file."""
    with open(base_memory_file, "w") as f:
        json.dump(memory, f, indent=4)


def clean_input(text):
    text = text.lower().strip()
    return re.sub(r"[^\w\s]", "", text)


def get_response(user_input, memory):
    cleaned = clean_input(user_input)
    
    if cleaned in memory and cleaned != "default":
        return random.choice(memory[cleaned])
    
    sorted_keys = sorted(memory.keys(), key=len, reverse=True)

    for key in sorted_keys:
        if key == "default":
            continue
        # Use word boundaries so "cap" doesn't match inside "caption"
        pattern = r"\b" + re.escape(key) + r"\b"
        if re.search(pattern, cleaned):
            return random.choice(memory[key])

    if "default" in memory and memory["default"]:
        return random.choice(memory["default"])

    return None


def main():
    memory = load_memory()
    print("🤖 Bot: Yo! I'm ready. Type 'quit' to exit, 'teach' to train me, or 'clear' to clean screen.")
    print("-----------------------------------------------------------------------------------")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit"]:
            print("🤖 Bot: Peace out! ✌️")
            break

        if user_input.lower() in ["clear", "cls"]:
            clear_screen()
            print("🤖 Bot: Screen cleared! What's next?")
            print("--------------------------------------------------")
            continue

        if user_input.lower() == "teach":
            phrase = input("🤖 Bot: What phrase should I learn? ").strip()
            if phrase:
                reply = input(f"🤖 Bot: What should I reply when someone says '{phrase}'? ").strip()
                if reply:
                    cleaned_key = clean_input(phrase)
                    if cleaned_key not in memory:
                        memory[cleaned_key] = []
                    memory[cleaned_key].append(reply)
                    save_memory(memory)
                    print("🤖 Bot: Bet! I learned it. Try asking me again!")
            continue

        response = get_response(user_input, memory)

        if response:
            print(f"🤖 Bot: {response}")
        else:
            print("🤖 Bot: I don't know how to respond to that. 🥺")


if __name__ == "__main__":
    main()

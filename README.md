Keyword Chatbot:
Keyword Chatbot is a rule-based, learning chatbot designed to respond to slang/keywords (e.g., "rizz", "slay", "sus"). If the user types something the bot doesn't recognize, the bot asks the user to teach it a response, saving newly learned words and answers persistently to a JSON file (memory.json

Tech Stack:

1. json - Handles data serialization and persistence. It reads from and writes to memory.json so learned phrases survive program restarts.
2. random - Used for response variety via random.choice(), picking a random response when multiple answers exist for a keyword.
3. re - Python's Regular Expressions engine. Used to sanitize user input by stripping away punctuation

Data Structures & Globals
a. base_memory_file - A string ("memory.json") storing the path to the persistent storage file.
b. dict_responses - A dictionary (dict[str, list[str]]) containing the default knowledge base of slang terms mapped to lists of potential replies.

Core Objectives

1. Rule-Based Slang Chatbot 
a. Recognizes specific internet slang and common keywords (e.g., "rizz", "no cap", "slay", "skibidi").
b. Delivers randomized, context-relevant replies to keep conversations dyna

2. Self-Learning / Dynamic Knowledge Base:
When given a phrase or keyword it does not recognize, it prompts the user to teach it what to say.
Learns new responses in real-time during the conversation.

3. Data Persistence
Automatically saves new words and responses to memory.json so the bot retains everything it learned even after the program restarts.

4. Input Sanitization
Cleans punctuation and normalizes user input to make keyword matching flexible and fault-tolerant.

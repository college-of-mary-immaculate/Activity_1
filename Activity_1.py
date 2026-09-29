import json
import os
import random
import re
import sys



base_memory_file = "memory.json"


dict_responses = {
    # --- Greetings & Basics ---
    "hello": [
        "Yo gamer! Ready to drop some frame-perfect Tekken knowledge or what?",
        "Wassup bestie! Ready to hit the lab and cook in Tekken?",
        "Yo! Welcome to the Tekken 8 Dojo fr fr!"
    ],
    "hi": [
        "Yo! Let's talk Tekken!",
        "Wassup! What Tekken guide or FYI do you need today?",
        "Hey! Ready to stop mashing and start punishing?"
    ],
    "how are you": [
        "Living my best life in the lab! How's your win streak looking?",
        "Just vibing and wavedashing! What about you?",
        "All good here! Ready to lab some frame data fr!"
    ],
    "bye": [
        "Peace out! ✌️ Go hit rank and take those Ws!",
        "Catch ya later! Don't mash on negative frames!",
        "Bye bestie, stay safe and keep blocking low!"
    ],
    "thanks": [
        "Anytime! 🫡 Go slay in Tekken online!",
        "No problem at all! W gamer behavior!",
        "You know it, anytime! Let me know if you need more frame data FYIs!"
    ],

    # --- Tekken Core Concepts & Guides ---
    "tekken": [
        "Tekken is the ultimate 3D fighting game fr! Highs, Mids, Lows, and 3D sidestepping. What topic do you wanna learn? (frames, heat, punish, characters, combos)",
        "Tekken 8 is pure aggression and high hype! Ask me about frame data, heat system, rage arts, or specific character guides!"
    ],
    "guide": [
        "Tekken Starter Guide: 1) Learn your character's block punishers, 2) Don't press buttons on negative frames, 3) Use Heat System to force mixups fr fr!",
        "Quick Tekken starter pack: Highs hit standing (duckable), Mids hit ducking (block standing!), Lows hit standing (block crouching!). Ask me about 'frames' or 'punish'!"
    ],
    "frames": [
        "Frame data is real talk, no cap! If a move is -10 or more on block, it's unsafe and can be block punished. If you're positive (+), it's your turn to cook!",
        "Frames dictate turn-taking in Tekken. + frames mean you keep attacking, - frames mean stop mashing or you get launch punished for real!"
    ],
    "frame data": [
        "Frame data breakdown: Startup frames = how fast a move comes out (fastest jab is i10). Block frames = turn advantage (+ is good, - is unsafe). No cap, check replay mode!"
    ],
    "punish": [
        "Block punishing is key! When your opp throws out an unsafe move, hit your fast punisher (like 1,2 Jab for i10 or a launcher for -15 moves). Don't let them free!",
        "Punishment guide: -10 to -14 moves get Jab/Mid punishers. -15 or worse gets a FULL LAUNCH COMBO! Ate and left no crumbs!"
    ],
    "heat": [
        "Heat System is peak Tekken 8 aggression! Enter Heat with Heat Engager or Heat Burst for chip damage, Heat Dashes (+ frames), and Heat Smash mixups!",
        "Heat state empowers your character with special moves, armor, and chip damage fr fr. Activate it to turn into an absolute menace!"
    ],
    "heat system": [
        "Tekken 8 Heat System gives you 1 Heat activation per round. Use Heat Dash to extend combos or close distance with massive + frames on block!"
    ],
    "rage art": [
        "Rage Art is your low health (under 30%) power crush armor move! Deals huge damage, but if the opponent blocks it, it's -15 or worse and you DIE no cap!",
        "Rage Art tip: Don't just raw press it! Use it on opponent whiff, during enemy mash, or end of combo fr fr."
    ],
    "ewgf": [
        "Electric Wind God Fist (EWGF): Mishima holy grail! Input: f, n, d, df+2 (frame perfect df and 2). +5 on block, i14 launcher fr! Absolute unspoken rizz!",
        "EWGF is +5 on block, high launcher, fast as lightning! Miss the frame sync and you get a mid/high regular Wind God Fist which is unsafe on block!"
    ],
    "electric": [
        "Electrics are the ultimate flex in Tekken! Frame-perfect EWGF input gives +5 block advantage and launches on hit. Keep practicing that d, df+2 timing!"
    ],
    "wavedash": [
        "Wavedashing is crouch dash canceling (f, n, d, df, f...). Spams mental pressure & mixups between Hellsweep (Low) and EWGF/Mid launcher fr!",
        "Wavedash lets Mishimas and Armor King realign, close distance fast, and force ducking reactions from opponents!"
    ],
    "oki": [
        "Okizeme (oki) is wake-up pressure on a knocked down opponent! Use tech catches, low pokes, or mid launchers to cook them as they get up fr!",
        "Oki tip: Watch how your opponent gets up! If they roll back, run up; if they spring kick, block and launch punish!"
    ],
    "okizeme": [
        "Okizeme guide: Force your opponent into 50/50 guessing games when they are grounded. Don't let them breathe for free!"
    ],
    "mixup": [
        "A 50/50 Mixup forces your opp to guess between a dangerous Mid (beats ducking) and a strong Low (beats standing block). Guess wrong = HUGE damage cook!",
        "Mixup strategy: Establish fast low pokes to make them duck, then unleash heavy mid launchers for max damage fr fr."
    ],
    "sidestep": [
        "Sidestepping (tap Up or Down) dodges linear moves into 3D space! Know your opponent's weak side (e.g. step Mishimas to the LEFT) to get easy back turned combos!",
        "Sidestep guide: If they spam linear moves, tap SS to step into their side and hit a launcher fr fr!"
    ],
    "launcher": [
        "A Launcher launches the opponent airborne for a juggle combo! Typical launchers are hopkicks (uf4), df2, or EWGF. Ate and left no crumbs!",
        "Launchers hit airborne for 60-80+ combo damage! Make sure your launcher isn't blocked, cause most are -12 to -15 on block!"
    ],
    "combo": [
        "Tekken Combo structure: 1) Launcher -> 2) Fillers -> 3) Tornado/Bound move -> 4) Enders / Wall splat! Keep combos consistent fr!",
        "Combo guide: Don't drop your combos for flashy style! Consistency > dropping max damage fr fr."
    ],
    "counter hit": [
        "Counter Hit (CH) occurs when your attack interrupts the opponent's attack startup! Triggers extra stun, crumple, or launchers fr!"
    ],

    # --- Character FYIs ---
    "kazuya": [
        "Kazuya Mishima: The 50/50 mixup king! EWGF + Hellsweep = mental damage fr. Requires top tier execution, zero panic buttons!",
        "Kazuya FYI: +5 EWGF on block, devastating vortex wavedash. Absolute sigma Mishima energy!"
    ],
    "jin": [
        "Jin Kazama: Main character energy! Incredible parries, f4 counter-hit poke, electrics, and insane Heat mixups. Ultimate all-rounder fr!",
        "Jin FYI: Zen stance mixups and high combo damage make him top tier. Very balanced with high ceiling."
    ],
    "reina": [
        "Reina: New Mishima queen in Tekken 8! Stance dance, fast aggression, and EWGF access. Absolute boss energy slay behavior!",
        "Reina FYI: Sentai & Heavens Wrath stances keep opponents guessing non-stop fr fr!"
    ],
    "king": [
        "King: The grab god! Giant Swing, Shining Wizard, and Chain Throws will break your opp's sanity. Learn grab breaks (1, 2, 1+2) or get cooked!",
        "King FYI: Has armor moves, high damage grabs, and hopkick. Don't crouch blindly or his mid knee will launch you fr!"
    ],
    "bryan": [
        "Bryan Fury: Counter-hit demon! 3,1,6 and b1 pressure. Taunt Jet Upper (f, b+2) at the wall is peak flex if you have God execution!",
        "Bryan FYI: Wait for opponent to press buttons, then counter-hit launch them for 80+ damage fr!"
    ],
    "paul": [
        "Paul Phoenix: Deathfist (qcf+2) goes BOOM! Takes 50% health bar off one mid read. Simple, effective, big brain damage fr!",
        "Paul FYI: Mix up Deathfist (Mid) and Demolition Man (Low) at close range to obliterate health bars!"
    ],
    "law": [
        "Marshall Law: Fast nunchaku, 3-ring circus, dragon stance! Great for aggressive pressure, but watch out for duckable high string enders!",
        "Law FYI: DSS stance allows fast mixups and high pressure. W behavior if executed clean!"
    ],
    "hwoarang": [
        "Hwoarang: Taekwondo stance machine! Flamingo stance pressure locks opponents in blockstun forever. Learn to duck his highs or get brainrot!",
        "Hwoarang FYI: Endless pressure! Opponents must know when to dickdash (d+1) or duck the high kicks fr."
    ],
    "xiaoyu": [
        "Ling Xiaoyu: Art of Phoenix (AoP) stance ducks under mids like a ghost! Super slippery evasive gameplay, absolute troll slay energy!",
        "Xiaoyu FYI: Very evasive! Use low-hitting mid attacks or low pokes to hit her out of AoP stance fr fr."
    ],
    "yoshimitsu": [
        "Yoshimitsu: The sword party master! Flash (i6 frame panic move), Harakiri, helicopter stance. Unpredictable brainrot energy fr!",
        "Yoshimitsu FYI: Flash can interrupt strings that leave slight advantage. Don't press mindlessly into Yoshimitsu!"
    ],

    # --- Gen Z Slang Integration ---
    "cap": [
        "Saying frame data doesn't matter is pure CAP fr! Check replay mode to see why you got launched!",
        "That matchup knowledge is cap! Hit training mode and set bot to block all!"
    ],
    "no cap": [
        "No cap fr fr, labbing block punishers for 10 mins a day boosts your rank exponentially!",
        "No cap detected! Real talk, Tekken defense wins games!"
    ],
    "rizz": [
        "Landing a frame-perfect Just Frame EWGF in tournament clutch? Absolute unspoken Tekken rizz!",
        "W rizz or L rizz? Executing a 100 damage combo at the wall is W rizz!"
    ],
    "slay": [
        "Ate that rank promotion match and left no crumbs! Pure slay behavior!",
        "Slaying all day in ranked online! Keep cooking!"
    ],
    "skibidi": [
        "Mashing raw Rage Art in neutral is peak skibidi brainrot energy... but hey, if it hits, it hits!",
        "What in the sigma... don't brainrot me with raw hopkicks fr fr!"
    ],
    "mid": [
        "Calling a move 'mid' in Tekken? Mids are essential because they hit opponents who crouch block! High tier move type no cap!",
        "If your defense is mid, opponents will mix you up all day! Lab those low breaks!"
    ],
    "cook": [
        "Let him cook! Hit that launcher, wall splat, and unleash Heat Dash for max damage!",
        "You're cooking now! Keep the oki pressure on their get-up!"
    ],
    "sus": [
        "Mashing power crush on -9 block? That's kinda sus bro... get ready to get punished!",
        "Evasive stance ducking under my mid move? Extremely sus behavior fr!"
    ],
    "bet": [
        "Bet! Lab those frames, hit ranked online, and claim those Ws!",
        "Bet! I'm here to give you all the Tekken tips and frame FYIs!"
    ],
    "delulu": [
        "Thinking you can mash out of +6 block advantage is pure delulu fr fr!",
        "Delulu is not solulu when you're in negative frames! Hold block!"
    ],
    "gyatt": [
        "The damage on that 100% wall break combo is HUGE gyatt energy fr!",
        "Calm down! Save that hype energy for tournament top 8!"
    ],

    # --- Fallback / Default ---
    "default": [
        "That's wild! Tekken tip: When in doubt, check frame data in Practice Mode or check replay tips fr!",
        "Hmm, interesting! Ask me about 'frames', 'punish', 'heat', 'electric', 'characters' (like Kazuya, Jin, King), or Tekken slang!",
        "Say less, keep labbing! Got questions about combos, oki, wavedash, or block punishing?",
        "Not sure about that move, bestie! But remember: don't press buttons on negative frames fr fr!"
    ]
}


def clear_screen():
    """Clears the console screen using OS-specific commands."""
    os.system("cls" if os.name == "nt" else "clear")


def load_memory():
    """Robust memory loading using the os library to check file existence and size."""
    if os.path.exists(base_memory_file) and os.path.getsize(base_memory_file) > 0:
        try:
            with open(base_memory_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    updated = False
                    for k, v in dict_responses.items():
                        if k not in data:
                            data[k] = v
                            updated = True
                    if updated:
                        save_memory(data)
                    return data
        except (json.JSONDecodeError, UnicodeDecodeError):
            print("⚠️ Memory file was corrupted. Re-initializing default memory...")

    # Create/reset memory file if missing or corrupted
    save_memory(dict_responses)
    return dict_responses


def save_memory(memory):
    """Saves memory back to JSON file."""
    with open(base_memory_file, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)


def clean_input(text):
    text = text.lower().strip()
    cleaned = re.sub(r"[^\w\s]", "", text)
    return re.sub(r"\s+", " ", cleaned).strip()


def get_response(user_input, memory):
    cleaned = clean_input(user_input)
    if not cleaned:
        return None
    
    if cleaned in memory and cleaned != "default":
        return random.choice(memory[cleaned])
    
    sorted_keys = sorted(memory.keys(), key=len, reverse=True)

    for key in sorted_keys:
        if key == "default" or not key.strip():
            continue
        # Use word boundaries so "cap" doesn't match inside "caption"
        pattern = r"\b" + re.escape(key) + r"\b"
        if re.search(pattern, cleaned):
            return random.choice(memory[key])

    if "default" in memory and memory["default"]:
        return random.choice(memory["default"])

    return None


def main():
    # Ensure console handles UTF-8 emojis on Windows
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stdin, "reconfigure"):
        sys.stdin.reconfigure(encoding="utf-8", errors="replace")

    memory = load_memory()
    print("🥊 Tekken Bot: Yo! I'm your Tekken Guides & FYI Coach (Gen Z style). Type 'quit' to exit, 'teach' to train me, or 'clear' to clean screen.")
    print("---------------------------------------------------------------------------------------------------")

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n🥊 Tekken Bot: Peace out! ✌️ Go slay in ranked online!")
            break

        if not user_input:
            continue

        if user_input.lower() in ["quit", "exit"]:
            print("🥊 Tekken Bot: Peace out! ✌️ Go slay in ranked online!")
            break

        if user_input.lower() in ["clear", "cls"]:
            clear_screen()
            print("🥊 Tekken Bot: Screen cleared! What Tekken topic or slang is next?")
            print("------------------------------------------------------------------")
            continue

        if user_input.lower() == "teach":
            phrase = input("🥊 Tekken Bot: What Tekken term or phrase should I learn? ").strip()
            if phrase:
                cleaned_key = clean_input(phrase)
                if not cleaned_key:
                    print("🥊 Tekken Bot: That term has no valid words to learn! Teaching cancelled.")
                    continue
                reply = input(f"🥊 Tekken Bot: What should I reply when someone says '{phrase}'? ").strip()
                if reply:
                    if cleaned_key not in memory:
                        memory[cleaned_key] = []
                    memory[cleaned_key].append(reply)
                    save_memory(memory)
                    print("🥊 Tekken Bot: Bet! I learned it. Try asking me again!")
                else:
                    print("🥊 Tekken Bot: No reply entered. Teaching cancelled.")
            else:
                print("🥊 Tekken Bot: No term entered. Teaching cancelled.")
            continue

        response = get_response(user_input, memory)

        if response:
            print(f"🥊 Tekken Bot: {response}")
            if response in memory.get("default", []):
                print("🥊 Tekken Bot: I don't know how to respond specifically to that Tekken query yet. Type 'teach' to train me! 🥺")
        else:
            print("🥊 Tekken Bot: I don't know how to respond to that Tekken query yet. Type 'teach' to train me! 🥺")


if __name__ == "__main__":
    main()

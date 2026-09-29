# Keyword Chatbot: Tekken & Gen Z Slang Coach

**Keyword Chatbot** is an interactive, rule-based, self-learning Python chatbot designed to respond to fighting game terms (specifically Tekken 8) and Gen Z internet slang (e.g., *"rizz"*, *"slay"*, *"no cap"*, *"skibidi"*).

The chatbot features **real-time self-learning** and **persistent memory**: if the bot encounters a term it does not recognize, the user can teach it a custom response, which is automatically saved to disk (`memory.json`) and retained across program restarts.

---

## 🛠️ Tech Stack & Dependencies

The project relies strictly on Python standard libraries without external dependencies:

1. **`json`**: Handles data serialization and persistence. Reads from and writes to `memory.json` using UTF-8 encoding so learned phrases survive program restarts.
2. **`random`**: Provides response variety via `random.choice()`, picking a random response when multiple answers exist for a single keyword.
3. **`re`** (Regular Expressions): Powers input sanitization (stripping punctuation, normalizing whitespace) and intelligent word-boundary pattern matching (`\bkey\b`).
4. **`os`**: Interacts with the operating system to check file existence (`os.path.exists`), verify file sizes (`os.path.getsize`), and issue cross-platform console clearing commands (`cls` on Windows, `clear` on Unix/Linux/macOS).
5. **`sys`**: Configures standard I/O stream encoding (`sys.stdout.reconfigure`, `sys.stdin.reconfigure`) to ensure cross-platform UTF-8 emoji rendering (e.g., 🥊, ✌️, 🫡) on Windows consoles without encoding crashes.

---

## 📊 Data Structures & Globals

* **`base_memory_file`** (`str`): Stores the file path (`"memory.json"`) used for persistent storage.
* **`dict_responses`** (`dict[str, list[str]]`): The built-in default knowledge base mapping keywords and phrases to lists of potential replies. Categories include:
  * **Greetings & Basics**: `hello`, `hi`, `how are you`, `bye`, `thanks`
  * **Tekken Core Concepts**: `tekken`, `guide`, `frames`, `frame data`, `punish`, `heat`, `rage art`, `ewgf`, `electric`, `wavedash`, `oki`, `mixup`, `sidestep`, `launcher`, `combo`, `counter hit`
  * **Character FYIs**: `kazuya`, `jin`, `reina`, `king`, `bryan`, `paul`, `law`, `hwoarang`, `xiaoyu`, `yoshimitsu`
  * **Gen Z Slang**: `cap`, `no cap`, `rizz`, `slay`, `skibidi`, `mid`, `cook`, `sus`, `bet`, `delulu`, `gyatt`
  * **Default Fallbacks**: `default` (General Tekken advice when no exact or keyword match is found)

---

## ⚙️ Function Breakdown & Technical Details

### 1. `clear_screen()`
* **Purpose**: Clears the terminal output screen for a clean user interface.
* **Details**: Executes `os.system("cls")` when running on Windows (`os.name == "nt"`), otherwise executes `os.system("clear")`.

### 2. `load_memory()` -> `dict`
* **Purpose**: Loads persistent memory from `memory.json` into a Python dictionary.
* **Details**:
  * Checks if `memory.json` exists and is non-empty (`os.path.getsize > 0`).
  * Opens the file with explicit UTF-8 encoding (`encoding="utf-8"`).
  * Safely parses JSON data and verifies structure with `isinstance(data, dict)`.
  * Merges any newly added default keys from `dict_responses` into `data` without overwriting user-taught responses.
  * Catches `json.JSONDecodeError` and `UnicodeDecodeError`. If corruption is detected, it logs a warning and restores default memory via `save_memory(dict_responses)`.

### 3. `save_memory(memory: dict)`
* **Purpose**: Writes the current memory dictionary back to `memory.json`.
* **Details**: Uses `open(..., "w", encoding="utf-8")` and `json.dump(memory, f, indent=4, ensure_ascii=False)` to format JSON cleanly while preserving UTF-8 emojis directly in the file.

### 4. `clean_input(text: str)` -> `str`
* **Purpose**: Sanitizes and normalizes user input for consistent pattern matching.
* **Details**:
  1. Converts text to lowercase and strips leading/trailing whitespace (`text.lower().strip()`).
  2. Removes punctuation and special characters using `re.sub(r"[^\w\s]", "", text)`.
  3. Collapses multiple internal spaces into a single space using `re.sub(r"\s+", " ", cleaned).strip()`.

### 5. `get_response(user_input: str, memory: dict)` -> `str | None`
* **Purpose**: Processes the sanitized user input through a prioritized matching pipeline.
* **Pipeline Logic**:
  1. **Empty Check**: If sanitized input is empty, returns `None`.
  2. **Step A — Exact Match**: Checks if the full sanitized string exists as a key in `memory` (excluding `"default"`). If found, returns a random choice from its reply list.
  3. **Step B — Prioritized Word-Boundary Match**:
     * Sorts memory keys in descending order by length (`sorted(..., key=len, reverse=True)`). This guarantees multi-word phrases (e.g., `"no cap"`, `"frame data"`) are checked before shorter substrings (e.g., `"cap"`, `"frame"`).
     * Uses regex word boundaries `r"\b" + re.escape(key) + r"\b"` to prevent false positive partial matches (e.g., matching `"cap"` inside `"caption"`).
  4. **Step C — Default Fallback**: If no exact or word-boundary match is found, picks a randomized response from `memory["default"]` (or returns `None` if missing).

### 6. `main()`
* **Purpose**: Controls the main interactive command loop.
* **Details**:
  * Configures UTF-8 encoding for standard output and input streams.
  * Calls `load_memory()` to initialize bot memory.
  * Processes commands:
    * `quit` / `exit`: Terminates the program cleanly with a farewell message.
    * `clear` / `cls`: Clears the console output screen.
    * `teach`: Enters interactive learning mode, validating phrase inputs (preventing empty/punctuation-only key pollution), recording custom replies, and saving updates immediately to `memory.json`.
  * For queries triggering a default fallback response, prints the fallback response and informs the user how to use the `teach` command to train the bot.
  * Handles `KeyboardInterrupt` (Ctrl+C) and `EOFError` (Ctrl+D) gracefully.

---

## 🚀 Getting Started

### Requirements
* **Python**: Python 3.7+ (No third-party packages required).

### Running the Chatbot
Run the script directly from your terminal or command prompt:

```bash
python Activity_1.py
```
*(On Windows systems with Python launcher, you can also run: `py Activity_1.py`)*

### Interactive Commands
* Type any word or phrase (e.g., `ewgf`, `what is frame data`, `rizz`) to get a reply.
* Type `teach` to train the chatbot with a new keyword and response.
* Type `clear` or `cls` to clear the terminal screen.
* Type `quit` or `exit` to close the chatbot.

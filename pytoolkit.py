#!/usr/bin/env python3
"""
PyToolkit - A Multi-Utility Python Project
==========================================
A collection of 7 mini-apps in one clean menu-driven program.
Perfect for beginners/intermediates to learn from and demo to friends!

Features:
1. Password Generator
2. Smart Calculator with History
3. Quick Notes (saves to file)
4. Roll Dice
5. Flip Coin
6. Countdown Timer
7. Number Guessing Game

Author: You
"""

import random
import string
import time
import os
from datetime import datetime

# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def clear_screen():
    """Clear the terminal screen for a clean look."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Print a fancy header for each tool."""
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)

def pause():
    """Wait for user to press Enter before continuing."""
    input("\nPress Enter to return to menu...")

# ============================================================
# 1. PASSWORD GENERATOR
# ============================================================

def password_generator():
    print_header("🔐 PASSWORD GENERATOR")

    try:
        length = int(input("Enter password length (8-50): "))
        if length < 8 or length > 50:
            print("❌ Please choose between 8 and 50.")
            pause()
            return
    except ValueError:
        print("❌ Invalid input. Using default: 12")
        length = 12

    # Ask what to include
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Build character pool
    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation

    if not chars:
        print("❌ You must select at least one character type!")
        pause()
        return

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))

    print("\n" + "-" * 40)
    print(f"Your Password: {password}")
    print("-" * 40)
    print(f"Strength: {'Strong 💪' if length >= 12 and use_symbols else 'Medium 👍' if length >= 8 else 'Weak ⚠️'}")

    # Save to file option
    save = input("\nSave this password to passwords.txt? (y/n): ").lower()
    if save == 'y':
        with open("passwords.txt", "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {password}\n")
        print("✅ Saved to passwords.txt")

    pause()

# ============================================================
# 2. SMART CALCULATOR WITH HISTORY
# ============================================================

def calculator():
    print_header("🧮 SMART CALCULATOR")
    print("Operations: +  -  *  /  //  %  **")
    print("Type 'history' to see past calculations")
    print("Type 'quit' to exit calculator\n")

    history = []

    while True:
        expr = input("calc> ").strip()

        if expr.lower() == 'quit':
            break
        elif expr.lower() == 'history':
            if not history:
                print("No history yet.")
            else:
                print("\n--- History ---")
                for i, h in enumerate(history[-10:], 1):
                    print(f"{i}. {h}")
                print("---------------")
            continue

        try:
            # Safe evaluation - only allow math operations
            allowed = {"__builtins__": None}
            result = eval(expr, allowed, {})
            entry = f"{expr} = {result}"
            history.append(entry)
            print(f"= {result}")
        except Exception as e:
            print(f"❌ Error: Invalid expression")

    pause()

# ============================================================
# 3. QUICK NOTES
# ============================================================

def quick_notes():
    print_header("📝 QUICK NOTES")
    print("1. Write a new note")
    print("2. Read all notes")
    print("3. Delete all notes")
    print("4. Back")

    choice = input("\nChoose (1-4): ").strip()

    if choice == '1':
        note = input("Enter your note: ").strip()
        if note:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            with open("mynotes.txt", "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {note}\n")
            print("✅ Note saved!")
        else:
            print("❌ Empty note not saved.")

    elif choice == '2':
        if not os.path.exists("mynotes.txt"):
            print("📭 No notes found.")
        else:
            with open("mynotes.txt", "r", encoding="utf-8") as f:
                notes = f.read()
            if not notes.strip():
                print("📭 No notes found.")
            else:
                print("\n--- YOUR NOTES ---")
                print(notes)
                print("------------------")

    elif choice == '3':
        confirm = input("Are you sure? Type 'yes' to delete all: ")
        if confirm.lower() == 'yes' and os.path.exists("mynotes.txt"):
            os.remove("mynotes.txt")
            print("🗑️ All notes deleted.")
        else:
            print("Cancelled.")

    pause()

# ============================================================
# 4. ROLL DICE
# ============================================================

def roll_dice():
    print_header("🎲 ROLL THE DICE")

    try:
        sides = int(input("Number of sides (default 6): ") or "6")
        rolls = int(input("How many dice? (default 1): ") or "1")
    except ValueError:
        print("❌ Invalid input. Using defaults.")
        sides = 6
        rolls = 1

    print("\nRolling...")
    time.sleep(0.5)

    results = [random.randint(1, sides) for _ in range(rolls)]
    total = sum(results)

    # ASCII dice faces for 6-sided
    dice_faces = {
        1: ["┌─────┐", "│     │", "│  ●  │", "│     │", "└─────┘"],
        2: ["┌─────┐", "│ ●   │", "│     │", "│   ● │", "└─────┘"],
        3: ["┌─────┐", "│ ●   │", "│  ●  │", "│   ● │", "└─────┘"],
        4: ["┌─────┐", "│ ● ● │", "│     │", "│ ● ● │", "└─────┘"],
        5: ["┌─────┐", "│ ● ● │", "│  ●  │", "│ ● ● │", "└─────┘"],
        6: ["┌─────┐", "│ ● ● │", "│ ● ● │", "│ ● ● │", "└─────┘"],
    }

    if sides == 6 and rolls <= 3:
        # Print ASCII art side by side
        for line_idx in range(5):
            line = ""
            for r in results:
                line += dice_faces[r][line_idx] + "  "
            print(line)
    else:
        print(f"Results: {results}")

    print(f"\nTotal: {total}")

    if rolls >= 2:
        avg = total / rolls
        print(f"Average: {avg:.1f}")

    pause()

# ============================================================
# 5. FLIP COIN
# ============================================================

def flip_coin():
    print_header("🪙 COIN FLIP")

    try:
        flips = int(input("How many flips? (default 1): ") or "1")
    except ValueError:
        flips = 1

    heads = 0
    tails = 0

    print("\nFlipping...")
    for i in range(flips):
        time.sleep(0.2)
        result = random.choice(["HEADS", "TAILS"])
        if result == "HEADS":
            heads += 1
            print(f"Flip {i+1}: 🪙 HEADS")
        else:
            tails += 1
            print(f"Flip {i+1}: 🪙 TAILS")

    print(f"\n📊 Results: {heads} Heads, {tails} Tails")
    if flips > 1:
        print(f"Heads: {(heads/flips)*100:.1f}% | Tails: {(tails/flips)*100:.1f}%")

    pause()

# ============================================================
# 6. COUNTDOWN TIMER
# ============================================================

def countdown_timer():
    print_header("⏱️ COUNTDOWN TIMER")

    try:
        minutes = int(input("Minutes: ") or "0")
        seconds = int(input("Seconds: ") or "0")
        total = minutes * 60 + seconds
        if total <= 0:
            print("❌ Please enter a positive time.")
            pause()
            return
    except ValueError:
        print("❌ Invalid input.")
        pause()
        return

    print(f"\n⏳ Starting {minutes}m {seconds}s timer...")
    print("Press Ctrl+C to stop early\n")

    try:
        for remaining in range(total, 0, -1):
            mins, secs = divmod(remaining, 60)
            # Simple progress bar
            progress = int(((total - remaining) / total) * 20)
            bar = "█" * progress + "░" * (20 - progress)
            print(f"\r[{bar}] {mins:02d}:{secs:02d}", end="", flush=True)
            time.sleep(1)

        print("\n\n⏰ TIME'S UP!")
        print("🔔 DING DING DING!")
    except KeyboardInterrupt:
        print("\n\n⏹️ Timer stopped.")

    pause()

# ============================================================
# 7. NUMBER GUESSING GAME
# ============================================================

def guessing_game():
    print_header("🎯 NUMBER GUESSING GAME")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")

    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
        except ValueError:
            print("❌ Please enter a number.")
            continue

        attempts += 1

        if guess < secret:
            print("📈 Too low! Try higher.")
        elif guess > secret:
            print("📉 Too high! Try lower.")
        else:
            print(f"\n🎉 CORRECT! The number was {secret}.")
            print(f"⭐ You guessed it in {attempts} attempts!")

            # Score rating
            if attempts <= 3:
                print("🏆 Rating: LEGENDARY!")
            elif attempts <= 5:
                print("👍 Rating: Great!")
            else:
                print("👌 Rating: Good job!")

            pause()
            return

        # Give hint when running out
        if attempts == max_attempts - 2:
            hint = "even" if secret % 2 == 0 else "odd"
            print(f"💡 Hint: The number is {hint}.")

    print(f"\n💀 Game Over! The number was {secret}.")
    print("Better luck next time!")
    pause()

# ============================================================
# MAIN MENU
# ============================================================

def show_menu():
    clear_screen()
    print("=" * 50)
    print("   🐍 PYTOOLKIT - Your Python Multi-Utility App")
    print("=" * 50)
    print("\n  [1] 🔐 Password Generator")
    print("  [2] 🧮 Smart Calculator")
    print("  [3] 📝 Quick Notes")
    print("  [4] 🎲 Roll Dice")
    print("  [5] 🪙 Flip Coin")
    print("  [6] ⏱️ Countdown Timer")
    print("  [7] 🎯 Number Guessing Game")
    print("  [0] ❌ Exit")
    print("\n" + "=" * 50)

def main():
    """Main program loop."""
    while True:
        show_menu()
        choice = input("Enter your choice (0-7): ").strip()

        if choice == '1':
            password_generator()
        elif choice == '2':
            calculator()
        elif choice == '3':
            quick_notes()
        elif choice == '4':
            roll_dice()
        elif choice == '5':
            flip_coin()
        elif choice == '6':
            countdown_timer()
        elif choice == '7':
            guessing_game()
        elif choice == '0':
            print("\n👋 Thanks for using PyToolkit! Keep coding!\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")
            time.sleep(1)

# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
PyToolkit - A Multi-Utility Python Project
==========================================
A collection of 7 mini-apps in one clean menu-driven program.
Perfect for beginners/intermediates to learn from and demo to friends!

Features:
1. Password Generator
2. Smart Calculator with History
3. Quick Notes (saves to file)
4. Roll Dice
5. Flip Coin
6. Countdown Timer
7. Number Guessing Game

Author: You
"""

import random
import string
import time
import os
from datetime import datetime

# ============================================================
# UTILITY FUNCTIONS
# ============================================================

def clear_screen():
    """Clear the terminal screen for a clean look."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """Print a fancy header for each tool."""
    print("\n" + "=" * 50)
    print(f"  {title}")
    print("=" * 50)

def pause():
    """Wait for user to press Enter before continuing."""
    input("\nPress Enter to return to menu...")

# ============================================================
# 1. PASSWORD GENERATOR
# ============================================================

def password_generator():
    print_header("🔐 PASSWORD GENERATOR")

    try:
        length = int(input("Enter password length (8-50): "))
        if length < 8 or length > 50:
            print("❌ Please choose between 8 and 50.")
            pause()
            return
    except ValueError:
        print("❌ Invalid input. Using default: 12")
        length = 12

    # Ask what to include
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Build character pool
    chars = ""
    if use_upper: chars += string.ascii_uppercase
    if use_lower: chars += string.ascii_lowercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation

    if not chars:
        print("❌ You must select at least one character type!")
        pause()
        return

    # Generate password
    password = ''.join(random.choice(chars) for _ in range(length))

    print("\n" + "-" * 40)
    print(f"Your Password: {password}")
    print("-" * 40)
    print(f"Strength: {'Strong 💪' if length >= 12 and use_symbols else 'Medium 👍' if length >= 8 else 'Weak ⚠️'}")

    # Save to file option
    save = input("\nSave this password to passwords.txt? (y/n): ").lower()
    if save == 'y':
        with open("passwords.txt", "a") as f:
            f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] {password}\n")
        print("✅ Saved to passwords.txt")

    pause()

# ============================================================
# 2. SMART CALCULATOR WITH HISTORY
# ============================================================

def calculator():
    print_header("🧮 SMART CALCULATOR")
    print("Operations: +  -  *  /  //  %  **")
    print("Type 'history' to see past calculations")
    print("Type 'quit' to exit calculator\n")

    history = []

    while True:
        expr = input("calc> ").strip()

        if expr.lower() == 'quit':
            break
        elif expr.lower() == 'history':
            if not history:
                print("No history yet.")
            else:
                print("\n--- History ---")
                for i, h in enumerate(history[-10:], 1):
                    print(f"{i}. {h}")
                print("---------------")
            continue

        try:
            # Safe evaluation - only allow math operations
            allowed = {"__builtins__": None}
            result = eval(expr, allowed, {})
            entry = f"{expr} = {result}"
            history.append(entry)
            print(f"= {result}")
        except Exception as e:
            print(f"❌ Error: Invalid expression")

    pause()

# ============================================================
# 3. QUICK NOTES
# ============================================================

def quick_notes():
    print_header("📝 QUICK NOTES")
    print("1. Write a new note")
    print("2. Read all notes")
    print("3. Delete all notes")
    print("4. Back")

    choice = input("\nChoose (1-4): ").strip()

    if choice == '1':
        note = input("Enter your note: ").strip()
        if note:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            with open("mynotes.txt", "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {note}\n")
            print("✅ Note saved!")
        else:
            print("❌ Empty note not saved.")

    elif choice == '2':
        if not os.path.exists("mynotes.txt"):
            print("📭 No notes found.")
        else:
            with open("mynotes.txt", "r", encoding="utf-8") as f:
                notes = f.read()
            if not notes.strip():
                print("📭 No notes found.")
            else:
                print("\n--- YOUR NOTES ---")
                print(notes)
                print("------------------")

    elif choice == '3':
        confirm = input("Are you sure? Type 'yes' to delete all: ")
        if confirm.lower() == 'yes' and os.path.exists("mynotes.txt"):
            os.remove("mynotes.txt")
            print("🗑️ All notes deleted.")
        else:
            print("Cancelled.")

    pause()

# ============================================================
# 4. ROLL DICE
# ============================================================

def roll_dice():
    print_header("🎲 ROLL THE DICE")

    try:
        sides = int(input("Number of sides (default 6): ") or "6")
        rolls = int(input("How many dice? (default 1): ") or "1")
    except ValueError:
        print("❌ Invalid input. Using defaults.")
        sides = 6
        rolls = 1

    print("\nRolling...")
    time.sleep(0.5)

    results = [random.randint(1, sides) for _ in range(rolls)]
    total = sum(results)

    # ASCII dice faces for 6-sided
    dice_faces = {
        1: ["┌─────┐", "│     │", "│  ●  │", "│     │", "└─────┘"],
        2: ["┌─────┐", "│ ●   │", "│     │", "│   ● │", "└─────┘"],
        3: ["┌─────┐", "│ ●   │", "│  ●  │", "│   ● │", "└─────┘"],
        4: ["┌─────┐", "│ ● ● │", "│     │", "│ ● ● │", "└─────┘"],
        5: ["┌─────┐", "│ ● ● │", "│  ●  │", "│ ● ● │", "└─────┘"],
        6: ["┌─────┐", "│ ● ● │", "│ ● ● │", "│ ● ● │", "└─────┘"],
    }

    if sides == 6 and rolls <= 3:
        # Print ASCII art side by side
        for line_idx in range(5):
            line = ""
            for r in results:
                line += dice_faces[r][line_idx] + "  "
            print(line)
    else:
        print(f"Results: {results}")

    print(f"\nTotal: {total}")

    if rolls >= 2:
        avg = total / rolls
        print(f"Average: {avg:.1f}")

    pause()

# ============================================================
# 5. FLIP COIN
# ============================================================

def flip_coin():
    print_header("🪙 COIN FLIP")

    try:
        flips = int(input("How many flips? (default 1): ") or "1")
    except ValueError:
        flips = 1

    heads = 0
    tails = 0

    print("\nFlipping...")
    for i in range(flips):
        time.sleep(0.2)
        result = random.choice(["HEADS", "TAILS"])
        if result == "HEADS":
            heads += 1
            print(f"Flip {i+1}: 🪙 HEADS")
        else:
            tails += 1
            print(f"Flip {i+1}: 🪙 TAILS")

    print(f"\n📊 Results: {heads} Heads, {tails} Tails")
    if flips > 1:
        print(f"Heads: {(heads/flips)*100:.1f}% | Tails: {(tails/flips)*100:.1f}%")

    pause()

# ============================================================
# 6. COUNTDOWN TIMER
# ============================================================

def countdown_timer():
    print_header("⏱️ COUNTDOWN TIMER")

    try:
        minutes = int(input("Minutes: ") or "0")
        seconds = int(input("Seconds: ") or "0")
        total = minutes * 60 + seconds
        if total <= 0:
            print("❌ Please enter a positive time.")
            pause()
            return
    except ValueError:
        print("❌ Invalid input.")
        pause()
        return

    print(f"\n⏳ Starting {minutes}m {seconds}s timer...")
    print("Press Ctrl+C to stop early\n")

    try:
        for remaining in range(total, 0, -1):
            mins, secs = divmod(remaining, 60)
            # Simple progress bar
            progress = int(((total - remaining) / total) * 20)
            bar = "█" * progress + "░" * (20 - progress)
            print(f"\r[{bar}] {mins:02d}:{secs:02d}", end="", flush=True)
            time.sleep(1)

        print("\n\n⏰ TIME'S UP!")
        print("🔔 DING DING DING!")
    except KeyboardInterrupt:
        print("\n\n⏹️ Timer stopped.")

    pause()

# ============================================================
# 7. NUMBER GUESSING GAME
# ============================================================

def guessing_game():
    print_header("🎯 NUMBER GUESSING GAME")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?\n")

    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
        except ValueError:
            print("❌ Please enter a number.")
            continue

        attempts += 1

        if guess < secret:
            print("📈 Too low! Try higher.")
        elif guess > secret:
            print("📉 Too high! Try lower.")
        else:
            print(f"\n🎉 CORRECT! The number was {secret}.")
            print(f"⭐ You guessed it in {attempts} attempts!")

            # Score rating
            if attempts <= 3:
                print("🏆 Rating: LEGENDARY!")
            elif attempts <= 5:
                print("👍 Rating: Great!")
            else:
                print("👌 Rating: Good job!")

            pause()
            return

        # Give hint when running out
        if attempts == max_attempts - 2:
            hint = "even" if secret % 2 == 0 else "odd"
            print(f"💡 Hint: The number is {hint}.")

    print(f"\n💀 Game Over! The number was {secret}.")
    print("Better luck next time!")
    pause()

# ============================================================
# MAIN MENU
# ============================================================

def show_menu():
    clear_screen()
    print("=" * 50)
    print("   🐍 PYTOOLKIT - Your Python Multi-Utility App")
    print("=" * 50)
    print("\n  [1] 🔐 Password Generator")
    print("  [2] 🧮 Smart Calculator")
    print("  [3] 📝 Quick Notes")
    print("  [4] 🎲 Roll Dice")
    print("  [5] 🪙 Flip Coin")
    print("  [6] ⏱️ Countdown Timer")
    print("  [7] 🎯 Number Guessing Game")
    print("  [0] ❌ Exit")
    print("\n" + "=" * 50)

def main():
    """Main program loop."""
    while True:
        show_menu()
        choice = input("Enter your choice (0-7): ").strip()

        if choice == '1':
            password_generator()
        elif choice == '2':
            calculator()
        elif choice == '3':
            quick_notes()
        elif choice == '4':
            roll_dice()
        elif choice == '5':
            flip_coin()
        elif choice == '6':
            countdown_timer()
        elif choice == '7':
            guessing_game()
        elif choice == '0':
            print("\n👋 Thanks for using PyToolkit! Keep coding!\n")
            break
        else:
            print("\n❌ Invalid choice. Please try again.")
            time.sleep(1)

# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()

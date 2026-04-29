# Caesar Cipher - PRODIGY_CS_01
# Task 1 | Prodigy InfoTech Cybersecurity Internship
#
# This program encrypts and decrypts messages using
# the Caesar Cipher technique by shifting letters
# by a given number of positions.


def encrypt(message, shift):
    """Encrypts a message using Caesar Cipher."""
    encrypted_text = ""

    for char in message:
        if char.isalpha():  # Only shift letters, not symbols or numbers
            # Check if the letter is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')

            # Shift the letter and wrap around using modulo 26
            shifted = (ord(char) - base + shift) % 26 + base
            encrypted_text += chr(shifted)
        else:
            # Keep spaces, numbers, punctuation as they are
            encrypted_text += char

    return encrypted_text


def decrypt(message, shift):
    """Decrypts a message using Caesar Cipher (reverse shift)."""
    # Decryption is just encryption with a negative shift
    return encrypt(message, -shift)


def display_menu():
    """Displays the main menu to the user."""
    print("\n" + "=" * 45)
    print("       CAESAR CIPHER - Prodigy InfoTech")
    print("=" * 45)
    print("  1. Encrypt a message")
    print("  2. Decrypt a message")
    print("  3. Exit")
    print("=" * 45)


def get_shift_value():
    """Asks the user for a valid shift value (1-25)."""
    while True:
        try:
            shift = int(input("Enter shift value (1 to 25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("  ⚠ Please enter a number between 1 and 25.")
        except ValueError:
            print("  ⚠ Invalid input. Please enter a whole number.")


# ============================================================
# MAIN PROGRAM - runs in a loop until user exits
# ============================================================
print("\nWelcome to the Caesar Cipher Tool!")
print("Developed for Prodigy InfoTech Cybersecurity Internship")

while True:
    display_menu()
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == "1":
        # --- ENCRYPTION ---
        print("\n[ ENCRYPT MODE ]")
        message = input("Enter your message: ")
        shift = get_shift_value()

        result = encrypt(message, shift)

        print("\n--- Result ---")
        print(f"  Original  : {message}")
        print(f"  Shift     : {shift}")
        print(f"  Encrypted : {result}")

    elif choice == "2":
        # --- DECRYPTION ---
        print("\n[ DECRYPT MODE ]")
        message = input("Enter the encrypted message: ")
        shift = get_shift_value()

        result = decrypt(message, shift)

        print("\n--- Result ---")
        print(f"  Encrypted : {message}")
        print(f"  Shift     : {shift}")
        print(f"  Decrypted : {result}")

    elif choice == "3":
        # --- EXIT ---
        print("\nThank you for using Caesar Cipher Tool. Goodbye!\n")
        break

    else:
        print("\n  ⚠ Invalid choice. Please enter 1, 2, or 3.")

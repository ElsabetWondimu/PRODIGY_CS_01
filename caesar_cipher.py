"""
Caesar Cipher — Encrypt and Decrypt text with a shift value.
"""


def caesar_shift(text: str, shift: int, mode: str) -> str:
    """
    Shift each letter in `text` by `shift` positions.
    mode: 'encrypt' or 'decrypt'
    Non-letter characters (spaces, punctuation, numbers) are left unchanged.
    """
    if mode == "decrypt":
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26
            result.append(chr(shifted + base))
        else:
            result.append(char)

    return "".join(result)


def encrypt(text: str, shift: int) -> str:
    return caesar_shift(text, shift, "encrypt")


def decrypt(text: str, shift: int) -> str:
    return caesar_shift(text, shift, "decrypt")


def main():
    print("=== Caesar Cipher ===")
    while True:
        choice = input("\nChoose an option — (E)ncrypt, (D)ecrypt, (Q)uit: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in ("e", "d"):
            print("Invalid choice. Please enter E, D, or Q.")
            continue

        message = input("Enter your message: ")

        try:
            shift = int(input("Enter shift value (integer): "))
        except ValueError:
            print("Shift value must be an integer.")
            continue

        if choice == "e":
            output = encrypt(message, shift)
            print(f"Encrypted message: {output}")
        else:
            output = decrypt(message, shift)
            print(f"Decrypted message: {output}")


if __name__ == "__main__":
    main()

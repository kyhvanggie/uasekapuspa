def encrypt_caesar(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.isupper():
                result += chr((shifted - 65) % 26 + 65)
            else:
                result += chr((shifted - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt_caesar(text, key):
    return encrypt_caesar(text, -key)

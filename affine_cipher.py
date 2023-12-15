def encrypt_affine(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                result += chr((key * (ord(char) - 65) + 65) % 26 + 65)
            else:
                result += chr((key * (ord(char) - 97) + 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt_affine(ciphertext, key):
    # Calculate modular multiplicative inverse
    def mod_inverse(a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        return None

    result = ""
    mod_inv = mod_inverse(key, 26)
    if mod_inv is not None:
        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    result += chr((mod_inv * (ord(char) - 65) + 65) % 26 + 65)
                else:
                    result += chr((mod_inv * (ord(char) - 97) + 97) % 26 + 97)
            else:
                result += char
    else:
        result = "Error: Inverse does not exist for the given key."
    return result

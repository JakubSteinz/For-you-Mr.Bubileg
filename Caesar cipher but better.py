def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift)% 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift)% 26 + 97)
        elif char.isdigit():
            result += str((int(char) + shift) % 10)
        else:
            result += char
    return result

zpráva = "Hello my lovely device 2"
shift = 5
encodovaná_zpráva = caesar_cipher(zpráva, shift)
print("Zašifrovaná zpráva:", encodovaná_zpráva)

decodovaná_zpráva = caesar_cipher(encodovaná_zpráva, -shift)
print("Rozšifrovaná zpráva:", decodovaná_zpráva)
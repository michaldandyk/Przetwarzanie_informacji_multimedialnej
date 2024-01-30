def ceasar_cipher(text):
    encrypted_text = ""

    # zamiana małych liter na duże, oraz szyfrowanie kodem cezara
    for char in text:
        char = char.upper()
        if 'A' <= char <= 'Z':
            encrypted_text += chr((ord(char) - 62) % 26 + 65)
        else:
            encrypted_text += char

    return encrypted_text


if __name__ == "__main__":
    # wpisywanie przez użytkownika tekstu do zaszyfrowania 
    s = input("Podaj tekst do zaszyfrowania: ")

    encrypted_text = ceasar_cipher(s)

    # wyświetlenie szyfru
    print(encrypted_text)

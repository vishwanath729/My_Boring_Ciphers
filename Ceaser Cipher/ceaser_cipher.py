message = input('Enter the word/sentence you want to encrypt\n')
key = int(input('Enter the key\n'))
mode = input('Enter encrypt/decrypt\n').lower()


# Possible symbols
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated = ''


def cipher(message = message, key = key, mode =mode):
    global translated
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            # Performing encryption or decryption
            if mode == 'encrypt':
                translatedIndex = symbolIndex + key
            else:
                translatedIndex = symbolIndex - key

            # Handle wraparound if needed:
            if translatedIndex > len(SYMBOLS):
                translatedIndex = translatedIndex - len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            translated += SYMBOLS[translatedIndex]
        else:
            # Append symbol without encrypting or decrypting
            translated += symbol
    return translated


# Only symbols in SYMBOLS can be encrypted/decrypted
cipher()

print(translated)
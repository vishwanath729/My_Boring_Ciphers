message = input('Enter the encrypted message to bruteforce\n')
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

for key in range(len(SYMBOLS)):
    translated = ''
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            if translatedIndex < 0:
                translatedIndex += len(SYMBOLS)

            translated += SYMBOLS[translatedIndex]

        else:
            translated += symbol

    print(f'key #{key}:  {translated}')

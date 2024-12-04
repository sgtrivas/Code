""" VIGNERE Cipher, by Al Swigart"""

try:
    import pyperclip
    import pyinputplus as pyip
except ImportError:
    print("please install the necessary modules! Syntax: pip3 install <module>")
    pass

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    while True:
        response = pyip.inputStr('Do you want to encrypt or decrypt> ')
        if response.startswith('e'):
            Mode = 'encrypt'
            break
        elif response.startswith('d'):
            Mode = 'decrypt'
            break
        else:
            print("please enter the letter e or d")

    while True:
        print("""Please specify the key to use.
        It can be a word or a combination of strings. """)
        response = pyip.inputStr('> ').upper()
        if response.isalpha():
            myKey = response
            break

    myMessage = pyip.inputStr(f'Enter the message to {Mode}> ')
    
    #  perform encryption/decryption
    if Mode == 'encrypt':
        translated = encryptMessage(myMessage,myKey)
    elif Mode == 'decrypt':
        translated = decryptMessage(myMessage,myKey)

    print(f'{Mode.title()}ed message: ')
    print(translated)

    try:
        pyperclip.copy(translated)
        print(f'Full {Mode}ed text copied to clipboard.')
    except:
        pass


def encryptMessage(message,key):
    return translateMessage(message,key,'encrypt')
    
    
def decryptMessage(message,key):
    return translateMessage(message,key,'decrypt')


def translateMessage(message,key,mode):
    translated = []
    keyIndex = 0
    key = key.upper()

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        #print(symbol)
        #print(f'the first letter of message is{num}')
        if num != -1: #  -1 means that symbol.upper() was not in LETTERS.
            if mode == 'encrypt':
                #  add if encrypting
                num += LETTERS.find(key[keyIndex])
                #print(f'the intersecting letter is {num}')
            elif mode == 'decrypt':
                #  subtract if decrypting
                num -= LETTERS.find(key[keyIndex])

            num %= len(LETTERS) #  handles the potential wrap around
            print(num)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
            print(translated)
            keyIndex += 1 #  move to the next letter
            if keyIndex == len(key):
                keyIndex = 0
        else:
            translated.append(symbol)
    return ''.join(translated)
    
if __name__=='__main__':
    main()


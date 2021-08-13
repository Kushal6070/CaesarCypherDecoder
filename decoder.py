#Symbols 

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789'

#Print game intro

print('''Welcome to Caesar Cypher Decoder by Kushal.

        We help you encode and decode your messages.''')

#Ask user mode

while True:
    print()
    print('''Select mode: 
    
            E to encrypt. 

            D to decrypt.''')

    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please select d or e.')

#Ask user key
while True:
    maxKey = len(SYMBOLS) - 1
    print(f'Enter a key between 1 to {maxKey} to continue')
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

#Ask user input
print(f'Enter a message to {mode}.')
phrase = input('> ')

#Caesar cipher only works on uppercase letters:
phrase = phrase.upper()

#translated string 
translated = ''

#Logic for encoding
for symbol in phrase:
    if symbol in SYMBOLS:

        #Get the encrypted or decrypted number for this symbol
        num = SYMBOLS.find(symbol) #Getting the number of symbol

        if mode == 'encrypt':
            num =num+ key
        elif mode == 'decrypt':
            num = num - key
        
        #if the num is larger than len(SYMBOLS)
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
        
        translated = translated + SYMBOLS[num]
    else:

        #just add the symbol without encrypting/decrypting
        translated = translated + symbol

#Print the result
print(translated)



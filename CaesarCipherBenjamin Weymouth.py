#1: Caesar Cipher. (Encrypt and Decrypt a String)

#encrypt operation
# The string to be encrypted:
#input_text = 'The magic words are squeamish ossifrage'
#decrypt operation
# The string to be decrypted:
input_text = 'aolDthnpjD4vykzDhylDzx2lhtpzoDvzzpmyhnl'
#the key represents how many steps to move the original character by
key = 7
#this can be changed from encrypt to decrypt
#to perform multiple operations with the code
#mode = 'encrypt'
mode = 'decrypt'

#list of possible symbols (will not work for symbols outside of this list)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

#after translation this holds the result
after_translation = ''

#loop that goes through each character in the string input_text
for symbol in input_text:
    #check the SYMBOLS string to see if the symbol exists
    if symbol in SYMBOLS:

        symbolIndex = SYMBOLS.find(symbol)

        # check mode, then shift index of item
        if mode == 'encrypt':
            shifted_Index = symbolIndex + key
        elif mode == 'decrypt':
            shifted_Index = symbolIndex - key
        # allows for negative indexing
        if shifted_Index >= len(SYMBOLS):
            shifted_Index = shifted_Index - len(SYMBOLS)
        elif shifted_Index < 0:
            shifted_Index = shifted_Index + len(SYMBOLS)

        after_translation = after_translation + SYMBOLS[shifted_Index]
    else:
        # Append the symbol without encrypting/decrypting:
        after_translation = after_translation + symbol

# Output the translated string:
print(f"The result of your encrypt / decrypt operation is: \n {after_translation}")


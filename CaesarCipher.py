#Author: Gloria Ngan
#CaesarCipher.py
# This is a program designed to recieve input then encrypt it with two
# Caesar Ciphers, one for the odd chracters and one for even.

#NOTE: ord() turns a character into ASCII and chr() converts it back

print"---------This is a Caesar Cipher program---------"

#Global variables for the key values.
evenKey = 0
oddKey = 0
maxKey = 94
message = ""

#Function to reset variables, allowing the program to be looped.
def resetKey():
    global evenKey
    global oddKey
    global message
    evenKey = 0
    oddKey = 0
    message = ""

def getKey():
    #Prompts user for the key to shift with.
    print""
    print"The max key (amount by which a character is shifted) size is 94."
    global evenKey
    global oddKey
    while evenKey == 0 and oddKey == 0:
        evenKey = int(input("Enter the shift key for even chracters. This must be a nonzero integer."))
        #Evaluates input
        if evenKey >= 1 and evenKey <= maxKey:
            print evenKey
        #If the user enters an int greater than the max or other chracters, an error message is generated and setKey() is called again
        else:
            print "Error. I didn't quite get that."

        oddKey = int(input("Enter the shift key for odd chracters. This must be a nonzero integer.")) #Ensures that input is an int
        if oddKey >= 1 and oddKey <= maxKey:
            print oddKey
        #Error message
        else:
            print "Error. I didn't quite get that."
            getKey()
       
#Method to take input and get the mode (decrypt/encrypt).
def getMessage():
    global message
    message = raw_input("Enter the message.")
    return message

#This is the function for encrypting or decrypting.
def caesarCipher(message, oddKey, evenKey):
    index = 0
    translated = ""     #Empty string to store new message.
    
    #Loops until the program evaluates all the chracters of the message.
    #This function is applied to the evven characters.
    for char in message:
        if message.find(char)%2 == 0:     #Determines if char is even or odd.
            num = ord(char)
            num += evenKey
            if num > 126:
                num -= 94
            elif num < 32:
                num += 94
            translated += chr(num)
        #This function is applied to the odd characters.
        else:
            num = ord(char)
            num += oddKey
            if num > 126:
                num -= 94
            elif num < 32:
                num += 94
            translated += chr(num)
    print"The message is now", translated  + "."

#Sets mode of program to encrypt or decrypt.
def setMode():
    global evenKey
    global oddKey
    mode = raw_input("Do you want to encrypt or decrypt this? Enter 'e' or 'd'?")
    
    if mode == "e":
        #Nothing needs to be done to the keys for encyrption.
        print "encryption"  
        caesarCipher(message, oddKey, evenKey)
            
    elif mode == "d":
        #For decryption, the negative of the key is used to reverse the encryption.
        oddKey = -oddKey 
        evenKey = -evenKey
        print "decryption"
        caesarCipher(message, oddKey, evenKey)
        
    #Error message. In the event that the user mistypes, the program asks again.
    else:
        print"I'm sorry, I didn't quite get that."
        mode = raw_input("Do you want to encrypt or decrypt this? Enter 'e' or 'd'?")
        print mode
        
def startProgram():
    while True:
        print ""
        init = raw_input("Hit 'y' to start the program and 'n' if you want to exit.")
        #Allows program to be run again from the shell.
        if init == "y":
            resetKey()
            getKey()
            getMessage()
            setMode()
        elif init == "n":
            break

startProgram()

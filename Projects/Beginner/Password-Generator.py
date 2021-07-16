import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122)) #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) #Generate a random Uppercase letter (based on ASCII code)
digit1= str(random.randint(0,9)) # Generate a random number(integer) (based on ASCII code)
digit2= str(random.randint(0,9)) # Generate a random number(integer) (based on ASCII code)
punctuationSign1= chr(random.randint(33,152)) # Generate a random Punctuation Sign (based on ASCII code)
punctuationSign2= chr(random.randint(33,152)) # Generate a random Punctuation Sign (based on ASCII code)


#Generate password using all the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2

password = shuffle(password)

#Ouput
print(password)

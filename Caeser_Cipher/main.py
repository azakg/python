alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
correct_request = False
while not correct_request == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        correct_request = True
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
cryp_text =[]
decrypt_text =[]

def encrypt(plain_text, shift_amount):
  for i in range(len(plain_text)):
    for b in range(len(alphabet)):
      if plain_text[i] == alphabet[b]:
        if b+shift_amount <= len(alphabet)-1:
          cryp_text.append(alphabet[b+shift_amount])
        else:
          cryp_text.append(alphabet[b+shift_amount-len(alphabet)])
  myString = ''.join(cryp_text)
  print(myString)

def decrypt(plain_text, shift_amount):
  for i in range(len(plain_text)):
    for b in range(len(alphabet)):
      if plain_text[i] == alphabet[b]:
        if b-shift_amount <= len(alphabet)-1 and b-shift_amount >=0:
          decrypt_text.append(alphabet[b-shift_amount])
        else:
          decrypt_text.append(alphabet[b-shift+len(alphabet)])
  myString = ''.join(decrypt_text)
  print(myString)

if direction == "encode":
  encrypt(text, shift)
else:
  decrypt(text, shift)
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
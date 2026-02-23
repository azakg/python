import string
alphabet = list(string.ascii_lowercase)
def encode(text, shift):
    encoded_text = ""
    for ch in text:
        if ch.lower() in alphabet:
            idx = alphabet.index(ch.lower())
            new_ch = alphabet[(idx + int(shift)) % 26]
            if ch.isupper():
                new_ch = new_ch.upper()
            encoded_text += new_ch
        else:
            encoded_text += ch
    print(f"Here's encoded result: {encoded_text}")

def decode(text, shift):
    decoded_text = ""
    for ch in text:
        if ch.lower() in alphabet:
            idx = alphabet.index(ch.lower())
            new_ch = alphabet[(idx - int(shift)) % 26]
            if ch.isupper():
                new_ch = new_ch.upper()
            decoded_text += new_ch
        else:
            decoded_text += ch
    print(f"Here's decoded result: {decoded_text}")

quit = "True"
while quit != "False":
    action_type = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    if action_type == 'encode':
        message = input("Type message: \n")
        shift = input("Type shift: \n")
        encode(message, shift)
    elif action_type == 'decode':
        message = input("Type message: \n")
        shift = input("Type shift: \n")
        decode(message, shift)
    elif action_type == 'quit':
        quit = "False"
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
new_message = ''
message = input('please enter a message:')
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position + key) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    else:
        new_message += character
print("your encrypted  message is ", new_message)


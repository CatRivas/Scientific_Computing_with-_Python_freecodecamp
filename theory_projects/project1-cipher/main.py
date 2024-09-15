import sys

def main():
    select_cipher = input('Chosse cipher, press 1 for Caesar or press 2 for Vigenere: ').strip()
    
    cipher_modes = ['1','2']
    if select_cipher not in cipher_modes:
        sys.exit('Invalid choice. Please enter 1 for Caesar or 2 for Vigenere.')

    text, variable, mode = get_user_input(select_cipher)
    
    if select_cipher == '1':
        result = caesar(text, variable, mode)
    
    elif select_cipher == '2':
        result = vigenere(text, variable, mode)

    print(f'Result: {result}')


def get_user_input(cipher):
    cipher_modes = {
        'encrypt': 1,
        'decrypt': -1,
    }

    text = input('Type the text to cipher: ').strip()
    mode = input('Type the mode: "encrypt" or "decrypt": ').strip().lower()

    if mode not in cipher_modes:
        sys.exit('Invalid mode. Please choose between "encrypt" or "decrypt".')

    if cipher == '1': #Caesar cipher
        shift = input('Type the shift number: ').strip()
        if not shift.isdigit(): 
            sys.exit('Shift must be a number.')
        else:
            return text, int(shift), cipher_modes[mode]
        
    elif cipher == '2': #Vigenere cipher
        key = input('Type the key: ').strip()

        return text, key, cipher_modes[mode]


## Caesar Cipher
def caesar(message, offset, caesar_type):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_text = ''

    for char in message.lower():
        if char.isalpha():
            current_index = alphabet.find(char)
            new_index = (current_index + int(offset)*caesar_type) % len(alphabet)
            new_text += alphabet[new_index]
        else:
            new_text += char

    return new_text



## Vigenere Cipher
def vigenere(message, key, type = 1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_text = []
    key_index = 0

    for char in message.lower():
    
        # Append space or non-alphabetic characters to the message
        if not char.isalpha():
            new_text.append(char)
        else:        
            current_index = alphabet.find(char)

            # Find the right key character to encode
            key_char = key[key_index % len(key)]

            # Define the offset and calculate the new index based on encryption or decryption
            offset = alphabet.index(key_char)

            new_index = (current_index + int(offset)*type) % len(alphabet)
            
            new_text.append(alphabet[new_index])

            key_index += 1

    return ''.join(new_text)
    


if __name__ == '__main__':
    main()
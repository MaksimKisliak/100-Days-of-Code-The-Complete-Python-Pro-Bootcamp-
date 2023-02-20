alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
active = True

print("""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  

8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ''
    for char in start_text:
            if cipher_direction == 'encode':
                if char in alphabet:
                    cipher_text_letter_shifted_encoded = alphabet[alphabet.index(char)+shift_amount]
                    end_text += cipher_text_letter_shifted_encoded
                else:
                    end_text += char
            elif cipher_direction == 'decode':
                if char in alphabet:
                    cipher_text_letter_shifted_decoded = alphabet[alphabet.index(char) + shift_amount * -1]
                    end_text += cipher_text_letter_shifted_decoded
                else:
                    end_text += char
    print(f'{cipher_direction}d text is {end_text.replace(" ", "")}')

while active:
    direction = ''
    while direction != 'encode' and direction != 'decode':
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            if direction == 'encode' or direction == 'decode':
                text = input("Type your message:\n").lower()
                shift = int(input("Type the shift number:\n")) % 26
                caesar(text, shift, direction)
            else:
                print('You have typed the wrong answer')

    answer = 'not defined'
    while answer == 'not defined':
        answer = input(f'Type \'yes\' if you want to go again. Otherwise type \'no\'').lower()
        if answer == 'no':
            active = False
        elif answer == 'yes':
            active = True
        else:
            print('Please provide the answer yes or not')
            answer = 'not defined'

from cryptography import SubstitutionCipher
from cryptography import TranspositionCiper
from collections import Counter

def execute_substitution_cipher():
    print("Substitution Cipher...")
    text = input("Input the text: ")
    
    k = input("Input the dislocation k (integer): ")
    while not k.isdigit():
        k = input("Invalid input. Input the dislocation k (integer): ")

    operation = input("Do you want to encode (e) or decode (d)? ")
    while (operation != "e") and (operation != "d"):
        operation = input("Invalid input. Input e or d:")
    
    cipher = SubstitutionCipher(int(k))

    if operation == "d":
        result = cipher.decode(text)
    else:
        result = cipher.encode(text)
    
    print("The result is: " + result)

def execute_transposition_cipher():
    print("Transposition Cipher...")
    text = input("Input the text: ")

    key = input("The key must have no repeating characters and it's lenght should be divisible by the text lenght.\nInput the key: ")
    repeating_char_list = [i for i,j in Counter(key).items() if j>1]
    while repeating_char_list or (len(text) % len(key) != 0):
        key = input("Invalid key. Input the key: ")
        repeating_char_list = [i for i,j in Counter(key).items() if j>1]

    operation = input("Do you want to encode (e) or decode (d)? ")
    while (operation != "e") and (operation != "d"):
        operation = input("Invalid input. Input e or d:")
    
    cipher = TranspositionCiper(key)

    if operation == "d":
        result = cipher.decode(text)
    else:
        result = cipher.encode(text)

    print("The result is: " + result)

def main():
    choice = input("Select your cipher:\n1 - Substitution Cipher\n2 - Transposition Cipher\n")
    while (choice != "1") and (choice != "2"):
        choice = input("Select your cipher:\n1 - Substitution Cipher\n2 - Transposition Cipher\n")
    
    if choice == "1":
        execute_substitution_cipher()
    elif choice == "2":
        execute_transposition_cipher()


if __name__ == "__main__":
    main()

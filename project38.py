import random 
import string 
print("Welcome to the Password Generator!")
len_pass = int (input("Enter the total number of characters in the Password: "))
letters = int (input ("Enter the number of letters in the password: "))
numbers = int (input ("Enter the number of number in the password: "))
symbols = int (input ("Enter the number of symbols in the password: "))
total = letters + numbers + symbols 
if len_pass == total:
    letters_1 = random.choices(string.ascii_letters, k=letters)
    numbers_1 = random.choices(string.digits, k=numbers) 
    symbols_1 = random.choices (string.punctuation, k=symbols)
    Shuffle = letters_1+ numbers_1 + symbols_1
    random.shuffle(Shuffle)
    password = "".join(Shuffle)
    print(f"Generated password:{password}")

else:
    print("Invalid input. The sum of letters, numbers, and symbols dosn't match the password")    
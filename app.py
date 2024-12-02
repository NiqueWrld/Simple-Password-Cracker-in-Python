import itertools

# Prompt the user for their password
u_pwd = input("Enter your password: ")

# Define the possible characters
pwd_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
             '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' , '@']

# Brute force the password
print("Cracking password... Please wait.")

for length in range(1, len(u_pwd) + 1):
    for guess in itertools.product(pwd_chars, repeat=length):
        # Join the guess tuple into a string
        guess_pwd = ''.join(guess)
        if guess_pwd == u_pwd:
            print("Your password is:", guess_pwd)
            exit()

# This message is just a fallback; it should not be reached.
print("Failed to crack the password.")

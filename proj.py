import random
import string

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    all_chars = lowercase + uppercase + digits + special_chars

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    return ''.join(password)

def main():
    print("Welcome to the Secure Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8 characters.")
                continue
            
            num_passwords = int(input("Enter the number of passwords to generate: "))
            if num_passwords < 1:
                print("Number of passwords must be at least 1.")
                continue
            
            break
        except ValueError:
            print("Please enter valid numbers.")

    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        password = generate_password(length)
        print(f"{i+1}. {password}")

if __name__ == "__main__":
    main()

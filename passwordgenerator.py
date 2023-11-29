import random
import string

def get_password(length):
    char = string.ascii_lowercase +string.ascii_uppercase + string.digits + string.punctuation
    pwd = ''.join(random.choice(char) for _ in range(length))
    return pwd

def main():
    num = int(input("Enter the number of passwords to generate: "))
    length = int(input("Enter the length of each password: "))

    list = []
    for _ in range(num):
        password = get_password(length)
        list.append(password)

    print("\nGenerated Passwords:")
    for i, password in enumerate(list, start=1):
        print(f"Password {i}: {password}")

if __name__ == "__main__":
    main()
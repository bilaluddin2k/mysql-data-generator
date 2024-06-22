import random
import string
import time

def generate_random_name():
    first_names = ["John", "Jane", "Alex", "Chris", "Katie", "Laura", "Robert", "Linda", "Michael", "Sarah"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Hernandez"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_random_age():
    return random.randint(18, 70)

def generate_random_email(name):
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "aol.com", "mail.com"]
    name_part = name.lower().replace(" ", ".")
    return f"{name_part}@{random.choice(domains)}"

def generate_random_username(name):
    name_part = name.lower().replace(" ", "_")
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits + "_-", k=4))
    return f"{name_part}{suffix}"

def generate_random_phone_number():
    return f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

def main():
    while True:
        name = generate_random_name()
        age = generate_random_age()
        email = generate_random_email(name)
        username = generate_random_username(name)
        phone_number = generate_random_phone_number()
        
        print(f"Name: {name}, Age: {age}, Email: {email}, Username: {username}, Phone Number: {phone_number}")
        time.sleep(0.5)  # Sleep for half a second to slow down the output a bit

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nData generation stopped by user.")

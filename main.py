from cryptography.fernet import Fernet


def main():

    master_pwd = input("What is the master password? ")
    key = load_key() + master_pwd.encode()
    fer = Fernet(key)


    while True:
        mode = input("Would you like to add a new password or view existing one (add, view, q)? ").strip().lower()
        
        if mode == "q":
            break
        
        if mode == "view":
            view(fer)
        elif mode == "add":
            add(fer)
        else:
            print("Invalid mode.")
            continue
    

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
        return key


def view(fer: Fernet) -> None:
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pw = data.split("|")
            print(f"User: {user}, Password: {fer.decrypt(pw.encode())}")


def add(fer: Fernet) -> None:
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open("passwords.txt", "a") as f:
        f.write(f"{name}|{fer.encrypt(pwd.encode()).decode()}\n")
    
    print("Password successfully added.")


if __name__ == "__main__":
    main()
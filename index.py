import bcrypt

users = {}

def register_user():
    username = input("Enter a username: ")
    while username in users:
        print("Username already taken. Try a different one.")
        username = input("Enter a username: ")

    password = input("Enter a password: ")
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    users[username] = hashed_password
    print("Registration successful!")


def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and bcrypt.checkpw(password.encode("utf-8"), users[username]):
        print("Login successful! Welcome, ", username)
        # Implement secured page content here for authenticated users
    else:
        print("Invalid username or password. Please try again.")


if __name__ == "__main__":
    while True:
        print("1. Register\n2. Login\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

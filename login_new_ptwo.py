
users = [
    {
        "username": "ayaan77@gmail.com",
        "password": "test123",
        "firtName": "Ayaan",
        "lastName": "Ahmad"
    }
]

def create_user():
    print("Create a new user account")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    for user in users:
        if user["username"] == username:
            print("Username already exists. Please choose a different username.")
            return

    new_user = {
        "username": username,
        "password": password,
        "firstName": first_name,
        "lastName": last_name
    }
    users.append(new_user)
    print("Account created successfully!")


def login(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return True

    return False

def login_page():
    print("Welcome to my blog!")
    while True:
        print("1. Login")
        print("2. Create a new account")
        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")

            if login(username, password):
                print("Welcome, " + username + "!")
                break
            else:
                print("Please try again.")
        elif choice == "2":
            create_user()
        else:
            print("Invalid choice.")

login_page()
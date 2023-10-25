users = [
    {
        "username": "ayaan77@gmail.com",
        "password": "test123",
        "firstName": "Ayaan",
        "lastName": "Ahmad"
    }
]

posts = []

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

def home_page(username):
    print("Welcome to my blog, " + username + "!")
    print("Recent Posts:")
    for post in posts:
        print("User: " + post["username"])
        print("Content: " + post["content"])
    print("Would you like to make a post? If so, type 1. If not, type 2.")
    choice2 = input("Enter your choice (1/2): ")
    if choice2 == "1":
        create_post(username)

def create_post(username):
    post_content = input("Speak your mind: ")
    post = {
        "username": username,
        "content": post_content
    }
    posts.append(post)
    print("Post created successfully!")
    home_page(username)

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
                home_page(username)
                
            else:
                print("Please try again.")
        elif choice == "2":
            create_user()
        else:
            print("Invalid choice.")

login_page()
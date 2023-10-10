#user_login = {
#    'Ayaan': 'Ahmad',
#    'Faraz': 'Ahmad',
#    'Harris': 'Warsi'
#}

# Defintion
groceries = ["apples", "bannana", "graps"]
# Accessing by Its index
print(groceries[1])

if "apples" in groceries:
    print("YES")

student = [12, 3.4, 167]

# Defintion
user_login = {
    "username": "ayaan77@gmail.com",
    "password": "test123",
    "firtName": "Ayaan",
    "lastName": "Ahmad"
}
# Access an item by its key
print(user_login["username"])

logins = [
    {
        'name': 'Faraz',
        'date_of_birth': '5-01-1763',
        'profile_picture': 'Faraz picture',
        'email': 'Faraz@gmail.com',
    },
    {
        'name': 'Ayaan',
        'date_of_birth': '03-21-06',
        'profile_picture': 'Ayaan picture',
        'email': 'Ayaan@gmail.com'
    },
    {
     
        'name': 'Harris',
        'date_of_birth': '6-09-1463',
        'profile_picture': 'harris [icture]',
        'email': 'harris@gmail..com'
    }
]

# This type of loop user is a item in the array
for user in logins:
    print(user["name"])

# Manually Access each item
user1Name = logins[0]["name"]
user2Name = logins[1]["name"]
user3Name = logins[2]["name"]

# This type of loop i is the index
for i in range(0, len(logins)):
    currentName = logins[i]["name"]
    print(currentName)

    if currentName == "Faraz":
        print("YEAHHHH!")
    else:
        print("NOOO")

def login(username, password):
    if user_login["username"] == username and user_login["password"] == password:
        return True
    else:
        return False

def login_page():
    print("Welcome to my blog!")
    while True:
        username = input("Username: ")
        password = input("Password: ")

        if login(username, password):
            print("Welcome, " + username + "!")
            break
        else:
            print("Please try again.")




login_page()

"""
user_profile = 
    
        'name': 'Faraz',
        'date_of_birth': '5-01-1763',
        'profile_picture': 'Faraz picture',
        'email': 'Faraz@gmail.com'
    
    
        'name': 'Ayaan',
        'date_of_birth': '03-21-06',
        'profile_picture': 'Ayaan picture',
        'email': 'Ayaan@gmail.com'
    
     
        'name': 'Harris',
        'date_of_birth': '6-09-1463',
        'profile_picture': 'harris [icture]',
        'email': 'harris@gmail..com'

        """
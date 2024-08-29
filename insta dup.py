class User:
    def __init__(self, userName, password, fullName):
        self.userName = userName 
        self.password = password
        self.fullName = fullName
        self.followers = []
        self.following = []
        self.followRequestsSent = []
        self.followRequestsReceived = []
 
 
dataStore = {}
 
def displayAndHandleMainMenu():
    print("-----------------------------------------------------")
    print("1 - Put follow requests")
    print("2 - Accept follow requests")
    print("3 - Post something")
    print("4 - Logout")
    option = int(input("Choose the option:"))
    print("-----------------------------------------------------")
 
    if option == 1:
        print("Handle Put follow requests")
    elif option == 2:
        print("Handle Accept follow requests")
    elif option == 3:
        print("Handle Posts")
    elif option == 4:
        print("Handle Logout")
    else:
        print("Choose appropriate option")
 
 
def handleLogin():
    print("Enter your login details")
    userName = input("Enter your user-name:")
    password = input("Enter your password:")
    if userName not in dataStore:
        print("Please sign-up first before logging in")
    else:
        print("Logged-in Successfully")
        displayAndHandleMainMenu()
 
def handleSignup():
    print("Enter your details to create an account")
    fullName = input("Enter your full-name:")
    userName = input("Enter your user-name:")
    password = input("Enter your password:")
    if userName not in dataStore:
        newUser = User(userName, password, fullName)
        dataStore[userName] = newUser
        print("Account created Successfully")
    else:
        print("User-Name already exists")
 
 
 
while True:
    print("-----------------------------------------------------")
    print("1 - Login")
    print("2 - Singup")
    print("3 - Exit")
    option = int(input("Choose the option:"))
    print("-----------------------------------------------------")
 
    if option == 1: 
        handleLogin() 
    elif option == 2:
        handleSignup()
    else:
        print("Thanks for using Instagram")
        exit(0)
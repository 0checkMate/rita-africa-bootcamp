# USER LOGIN SYSTEM

#Actual login credentials
stored_username = "Group 2" #saved username
stored_password = "The winning group"  #saved password

#Login system
username = str(input("USERNAME: "))
password = str(input("PASSWORD: "))

#Verifying login credentials
if stored_username == username and stored_password == password:
    print("Login successful")
else:
    print("User login credentials not correct")
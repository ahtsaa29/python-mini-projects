print("create account")

user_create = input("Enter a user name: ")
pass_create = input("Create a user Password: ")

print("account created successfully \n Login Now!!")

user_login = input("Enter a user name: ")
pass_login = input("Enter a user Password: ")


if user_create == user_login and pass_create == pass_login:
    print("login success")
else:
    print("wrong credentials")

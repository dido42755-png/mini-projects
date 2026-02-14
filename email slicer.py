
email = input("Enter your email: ")

index = email.index("@")
username = email[:index]
print(f"Your username is: {username}")
domain = email[index+1:]
print(f"Your domain is: {domain}")
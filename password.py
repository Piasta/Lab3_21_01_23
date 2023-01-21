import passlib.pwd as pwd


def generate_secure_password(user_input):
    password = pwd.genword(length=user_input, charset="ascii_72")
    return password


try:
    user_length = int(input("Enter the length of password.\n(8 is minimum)\n"))
    if user_length > 7:
        result = generate_secure_password(user_length)
        print(result)
    else:
        print("Password length should be higher than 7.")
except ValueError:
    print("Please enter a number.")
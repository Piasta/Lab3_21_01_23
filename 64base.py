import base64


def encrypt_base64(text):
    text_bytes = text.encode('utf-8')
    encoded_text = base64.b64encode(text_bytes)
    return encoded_text.decode('utf-8')


def decrypt_base64(text):
    text_bytes = text.encode('utf-8')
    decoded_text = base64.b64decode(text_bytes)
    return decoded_text.decode('utf-8')


print("Write a text.")
user_text = input()

print("What do you want to do?\n 1.Encrypt \n 2.Decrypt \nPress the number.")
user_choice = input()

if user_choice == '1':
    encrypted_text = encrypt_base64(user_text)
    print(encrypted_text)
elif user_choice == '2' and len(user_text) > 3:
    decrypted_text = decrypt_base64(user_text)
    print(decrypted_text)
else:
    print("Incorrect choice or your text doesn't match to base64 standards.")
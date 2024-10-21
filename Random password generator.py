import random
import string
def password_genrator():
    length_of_password = int(input("Enter the length of password :"))
    #check the length of password is shorter than 8 or not
    if length_of_password < 8:
        print("Error: Passwords shorter than 8 characters are not allowed.")
        return

    # By using string module we decide the  type letters that are allowed in our password
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    special_letters = string.punctuation

    #combine all the letter of password
    all_charaters = upper_case+special_letters + lower_case + digits

    #password creation
    password = ''.join(random.choice(all_charaters) for _ in range(length_of_password))

    # Print the password On the screen
    print(f"The password is :{password}")

password_genrator()

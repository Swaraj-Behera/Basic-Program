import string
import random
def random_string(length = 7):
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Invalid input. Using default length of 7.")
        length = 7
    l=string.ascii_letters + string.digits + string.punctuation
    if length < 5 :
        print("Password lenght should be more than 5 ")
    else:
        return ''.join(random.choice(l) for i in range(length))
if __name__ == "__main__":
    print("Your Password is: ", random_string())

def passwordgeneration():
    import os,sys,random,string
    n = int(input("Enter the length of the password: "))
    password = ''
    for i in range(0, n):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    with open('savedPassword.txt', 'a') as file:
        file.write(password + '\n')
        os.path.abspath('savedPassword.txt')
        print(f"Password saved in {os.path.abspath('savedPassword.txt')}")
    return password 
print(passwordgeneration())

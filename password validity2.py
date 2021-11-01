import re
T=True
while T:
    A=input("Enter strong Password:")
    if not len(A)>6 and not len(A)<16:
        print("Invalid Password 1")
        continue
    if not re.search("[a-z]",A):
        print("Invalid password 2")
        continue
    if not re.search("[A-Z]",A):
        print("Invalid Password 3")
        continue
    if not re.search("[0-9]",A):
        print("Invalid Password 4")
        continue
    if not re.search("[@#$]",A):
        print("Invalid Password 5")
        continue
    else:
        print("Your have succesfully created a strong password.")
        break

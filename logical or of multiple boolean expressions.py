def is_voter(age,register):
    if age>=18 or register=='yes':
        return True
    else:
        return false
age=int(input("enter the age:"))
register=input("are you registered>?(yes/no):").strip().lower()
if is_voter(age,register):
    print("you are eligible to vote!")
else:
    print("you are not eligible to vote")
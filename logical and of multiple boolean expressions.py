def is_voter(age,citizen,register):
    if age>=18 and citizen=='yes' and register=='yes':
        return True
    else:
        return false
age=int(input("enter the age:"))
citizen=input("are you a citizen>?(yes/no):").strip().lower()
register=input("are you registered>?(yes/no):").strip().lower()
if is_voter(age,citizen,register):
    print("you are eligible to vote!")
else:
    print("you are not eligible to vote")
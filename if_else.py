age = input("Enter Your Age : ")

age = int(age)
# age = 20

if age >= 12 and age < 18:
    print("You are an Teenager")
    print("You are still can not Vote")

elif age >= 18:
    print("You are an Adult")
    print("You can Vote")

else:
    print("!!! You can not Vote !!!")

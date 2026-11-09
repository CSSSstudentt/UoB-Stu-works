number = float(input("namber:"))

if float(number) == 0:
    print("This number is zero")
if float(number) > 0:
    print("This number is positive")
if float(number) < 0:
    print("This number is negative")


while True:
    score = float(input("grade:"))
    if float(score) > 0:
        break

grade = "Broken"

if float(score) >= 0 and float(score) <= 39:
    grade = "F"
elif float(score) >= 40 and float(score) <= 49:
    grade = "3rd"
elif float(score) >= 50 and float(score) <= 59:
    grade = "2.2"
elif float(score) >= 60 and float(score) <= 69:
    grade = "2.2"
elif float(score) >= 70 and float(score) <= 100:
    grade = "1st"
print(grade)


year = int(input("Enter the year:"))
if (int(year) % 4 == 0):
    if (int(year) % 100 == 0):
        if (int(year)% 400 == 0):
            print("it is a leap year")
else:
    print("it is not a leap year")

age = int(input("enter age:"))
if (int(age) < 18):
    print("You can't vote")
else:
    print("vote, whatever, don't care")

number2 = int(input("Enter number:"))
if (int(number2) % 5 == 0):
    if(int(number2)% 11 == 0):
        print("The number is divisible by 5 and 11")
else:
    print("it is not divisible by 5 or 11")

electric = int(input("Enter electric:"))

if int(electric) <= 100:
    print(electric * 0.5)
if int(electric) > 101 and int(electric) < 200:
    print(electric * 0.75)
if int(electric) > 201 and int(electric) < 300:
    print(electric * 1.2)
if int(electric) > 300:
    print(electric * 1.5)
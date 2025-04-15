'''Q1..... Write a program that takes a person's age and prints the ticket price:
Age < 5: Free
Age 5-18: ₹100
Age 19-60: ₹200
Age > 60: ₹150'''

age = int(input("Enter your age: "))
print("Ticket price according to age:")

if age < 5:
    print("Ticket is free")
elif age <= 18:
    print("Ticket price is 100rs per person")
elif age <= 60:
    print("Ticket price is 200rs per person")
else:
    print("Ticket price is 150rs per person")



'''Q2........Write a program to check login credentials. If username is "admin" and password is "1234", print "Login successful", else "Invalid credentials".'''
username = input("\n\nEnter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


'''3.Question: Write a program to take marks as input and print grade:
≥90: A
≥80: B
≥70: C
≥60: D
<60: F'''
marks = int(input("\n\nEnter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")



'''4.Take three numbers from the user and print the largest one.'''
num1 = float(input("\n\nEnter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)



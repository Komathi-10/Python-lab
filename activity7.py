
'''Q1.....Write a Python program to generate an invoice for a customer using their name, product, and price details.'''

customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
subtotal = price * quantity
tax_rate = 0.08  
tax = subtotal * tax_rate
total = subtotal + tax
print("==========================================")
print("INVOICE")
print("==========================================")
print(f"Customer: {customer_name}")
print(f"Product : {product_name}")
print(f"Price   : ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total   : ${total:.2f}")
print("==========================================")
print("Thank you....!")


'''Q2......Take a student’s name and grade, and print a formatted report like:'''

student_name = input("\n\nEnter student name: ")
grade = input("Enter student grade: ")
print("\n" + "="*30)
print("STUDENT GRADE REPORT")
print("="*30)
print(f"Name : {student_name}")
print(f"Grade: {grade}")
print("="*30)
print("Keep up the good work!")   

'''Q3.....Write a program that removes extra spaces from a user-entered message.'''

message = input("\n\nEnter your message: ")
cleaned_message = " ".join(message.split())
print("\nCleaned Message:")
print(cleaned_message)  

'''Q4....Take a feedback string and count how many times the word “good” appears in it (case-insensitive).'''

feedback = input("\n\nEnter your feedback: ")
count = feedback.lower().count("good")
print(f'\nThe word "good" appears {count} time(s) in the feedback.')    

'''Q5....Check if a password contains at least 1 uppercase letter, 1 lowercase letter, 1 digit, and is at least 8 characters long.'''

password = input("\n\nEnter your password: ")

if (len(password) >= 8 and
    any(c.isupper() for c in password) and
    any(c.islower() for c in password) and
    any(c.isdigit() for c in password)):
    print("Strong password ")
else:
    print("Weak password ")





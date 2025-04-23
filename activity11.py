'''Q1.Create a dictionary with student names as keys and their marks as values.Allow the user to input a name and display the student's marks.
If the student doesn't exist, show an appropriate message.'''

student_marks = {
    "Priya": 85,
    "Pooja": 78,
    "Ram": 92,
    "Kayal": 88
}
name = input("Enter the student's name: ")
if name in student_marks:
    print(f"{name}'s marks are: {student_marks[name]}")
else:
    print("Student not found in the record.")


'''Q2.Given a list of names, group them into a dictionary where the key is the first letter of each name and the value is a list of names that start with that letter.'''

names = ["Simron", "Sam", "shree", "Aishu", "Ameer", "Riya", "Rose", "jack", "jessy", "Ammu"]
grouped_names = {}
for name in names:
    first_letter = name[0].upper()
    if first_letter not in grouped_names:
        grouped_names[first_letter] = []
    grouped_names[first_letter].append(name)
print("\nGrouped names by first letter:")
for letter, name_list in grouped_names.items():
    print(f"{letter}: {name_list}")

'''Q3.Build a simple inventory system where each item and its quantity is stored in a dictionary.Ask the user to enter an item name and quantity to sell.
Update the dictionary and show the remaining stock or a message if there's not enough.'''

inventory = {
    "milk": 30,
    "bread": 20,
    "eggs": 15,
    "chocolate": 25
}
print("\nCurrent Inventory:")
for item, qty in inventory.items():
    print(f"{item}: {qty} in stock")
item_name = input("\nEnter the item name to sell: ").lower()
sell_quantity = int(input("Enter the quantity to sell: "))
if item_name in inventory:
    if inventory[item_name] >= sell_quantity:
        inventory[item_name] -= sell_quantity
        print(f"\nSold {sell_quantity} {item_name}(s).")
        print(f"Remaining stock of {item_name}: {inventory[item_name]}")
    else:
        print(f"\nNot enough stock of {item_name}. Only {inventory[item_name]} available.")
else:
    print(f"\nItem '{item_name}' not found in inventory.")


'''Q4.Create a contact book using a dictionary where the name is the key and phone number is the value. Allow the user to input a name and phone number.
If the name exists, update the number; otherwise, insert a new contact.'''

contact_book = {
    "Geetha": "1234567890",
    "Diya": "9876543210",
    "Vijay": "5551234567"
}
print("\nCurrent Contact Book:")
for name, number in contact_book.items():
    print(f"{name}: {number}")
name = input("\nEnter the contact name: ")
phone_number = input("Enter the phone number: ")
if name in contact_book:
    contact_book[name] = phone_number
    print(f"\nUpdated {name}'s phone number to {phone_number}.")
else:
    contact_book[name] = phone_number
    print(f"\nAdded new contact: {name} - {phone_number}")
print("\nUpdated Contact Book:")
for name, number in contact_book.items():
    print(f"{name}: {number}")







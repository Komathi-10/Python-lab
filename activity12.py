'''Q1.Write a program that asks the user for a list index and prints the value at that index from a predefined list. Handle the IndexError and ValueError exceptions.'''

my_list = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter the index of the item you want to access: "))
    print(f"Value at index {index} is: {my_list[index]}")

except IndexError:
    print("Error: Index out of range. Please enter a valid index.")

except ValueError:
    print("Error: Invalid input. Please enter an integer.")


'''Q2. Create a program to validate exam scores entered by the user. Use a custom exception to handle invalid scores.'''

class InvalidScoreError(Exception):
    def __init__(self, message="Score must be between 0 and 100."):
        self.message = message
        super().__init__(self.message)


def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError(f"Invalid score: {score}. Score must be between 0 and 100.")
    return f"Score {score} is valid."

try:
    user_input = input("Enter your exam score: ")
    score = float(user_input)  
    result = validate_score(score)
    print(result)

except InvalidScoreError as e:
    print("Error:", e)

except ValueError:
    print("Error: Please enter a numeric value.")



'''Q3.You have a dictionary. Ask the user to enter a key and display the corresponding value. Handle the KeyError.'''

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

try:
    key = input("Enter a key (e.g., name, age, city): ")
    print(f"The value for '{key}' is: {my_dict[key]}")

except KeyError:
    print(f"Error: '{key}' is not a valid key.")


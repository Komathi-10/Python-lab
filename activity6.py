'''Q1..... Print a Pyramid Pattern of Stars:
Write a program to print a pyramid pattern using stars (*).

Input: An integer n representing the number of rows.
Output: Print the following pyramid pattern:

    *
   ***
  *****
 *******
*********'''
def print_pyramid(n):
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
rows = 5
print_pyramid(rows)

'''Q2..... Count Even and Odd Numbers
Write a program to count the even and odd numbers in a list.
Input: A list of integers.
Output: Print the count of even and odd numbers.

Input: [1, 2, 3, 4, 5, 6]  
Output: Even numbers: 3, Odd numbers: 3'''
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"Even numbers: {even_count}, Odd numbers: {odd_count}")
input_list = [1, 2, 3, 4, 5, 6,7,8,9]
count_even_odd(input_list)

'''Q3.... Calculate the Sum of Even Numbers
Write a program to calculate the sum of all even numbers in a given range.
Input: Two integers start and end.
Output: The sum of even numbers in the range [start, end].

Input: start = 1, end = 10
Output: 30 (2 + 4 + 6 + 8 + 10)'''
def sum_of_evens(start, end):
    total = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total += num
    return total
start = 1
end = 20
result = sum_of_evens(start, end)
print(result) 

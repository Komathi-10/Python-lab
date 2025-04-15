'''1. Function to Remove Specific Character from a String
Write a function remove_char(s, char) that removes all occurrences of a specific character from a string.

Input: A string s and a character char (e.g., "hello", 'l').
Output: The string without the specified character (e.g., "heo").'''

def remove_char(s, char):
    return s.replace(char, '')
result = remove_char("hello", 'l')
print(result)


'''2. Function to Count Occurrences of a Character in a String
Write a function count_char_occurrences(s, char) that counts how many times a specific character char appears in the string s.

Input: A string s and a character char (e.g., "hello", 'l').
Output: The count of occurrences of char in s (e.g., 2).'''

def count_char_occurrences(s, char):
    return s.count(char)
result = count_char_occurrences("hello", 'l')
print(result)  



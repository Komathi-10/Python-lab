'''Q1.... Write a Python program to sum all the items in a list. '''
lst=[1,2,3,4,5,6]
result=sum(lst)
print("sum of list:",result)

'''Q2.... Write a Python program to get the largest and smallest number from a list without builtin functions. '''
l=[2,15,33,70,98]
smallest_no = l[0]
largest_no =l[0]
for num in l[1:]:
    if num < smallest_no:
        smallest_no = num
    if num > largest_no:
        largest_no = num
print("\nSmallest number:", smallest_no)
print("Largest number:", largest_no)

  
'''Q3.... Write a Python program to find duplicate values from a list and display those.'''
def find_duplicates(lst):
    duplicates = []
    for i in lst:
        if lst.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates
print("\nDuplicate values in the list : ",find_duplicates([1, 1, 2, 3, 4, 4, 5, 1,6,6,7,8,8]))


'''Q4.... Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
Original list: [1, 1, 2, 3, 4, 4, 5, 1] Length of the first part of the list: 3 Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1]) '''
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
part1 = original_list[:3]
part2 = original_list[3:]
print("\nFirst part:", part1)
print("Second part:", part2)
print("\n")


'''Q5.... Write a Python program to traverse a given list in reverse order,
and print the elements with the original index. Original list: ['red', 'green', 'white', 'black']
Traverse the said list in reverse order: black white green red'''
def reverse_traverse(lst):
    for i in range(len(lst)-1, -1, -1):
        print(f"Index: {i}, Value: {lst[i]}")

colors = ['red', 'green', 'white', 'black']
reverse_traverse(colors)

# Substring Occurrence Counter

This program takes an input string and a substring, then counts the number of times the given substring occurs in the input string. The string traversal takes place from left to right and is case-sensitive.

## Input Format

- The first line of input contains the original string.
- The second line contains the substring.

## Constraints

- Each character in the string is an ASCII character.

## Output Format

The program outputs an integer indicating the total number of occurrences of the substring in the original string.

## Sample Input
 ABCDCDC
 
 CDC


## How It Works

The program uses a loop to traverse through the original string and checks for occurrences of the substring. It counts the occurrences and then outputs the count.

Here's a simple example of how it works in Python:

```python
def count_substring(string, substring):
    count = 0
    for i in range(len(string) - len(substring) + 1):
        if string[i:i + len(substring)] == substring:
            count += 1
    return count

# Input
string = input("Enter the string: ")
substring = input("Enter the substring: ")

# Count and print the number of occurrences
result = count_substring(string, substring)
print("Number of occurrences:", result)

```

This program demonstrates how to count substring occurrences in a case-sensitive manner, and it's particularly useful when working with string processing and text analysis tasks.
🚀 Happy coding!

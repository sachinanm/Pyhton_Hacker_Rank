# Python Tuple Hashing 🐍

This repository contains a simple Python code hacker rank question that demonstrates how to create a tuple, calculate its hash value, and print the result. The code snippet uses the `hash()` function to compute the hash value of a tuple containing two integers.
In hacker rank select pypy3 only to run as there is some issue in python3 for this code, if there is any particular reason you know let me know also.
## Code Snippet 📝🔍

```python
if __name__ == '__main__':
    n = int(input())  # Read the number of elements in the tuple
    t = tuple(map(int, input().split()[:2]))  # Read two space-separated integers and create a tuple
    print(hash(t))  # Calculate and print the hash value of the tuple


```
After running the script, the hash value of the tuple will be calculated and displayed.
The provided Python code snippet reads the number of elements in the tuple and then reads two space-separated integers to create a tuple. The hash value of the tuple is then calculated using the `hash()` function and printed to the console.
Feel free to customize the text to provide more information or context about the code snippet and its functionality.

# Contributing 🤝❤️
Contributions are welcome! If you have improvements, bug fixes, or additional examples related to Python, feel free to fork this repository, make changes, and create a pull request.

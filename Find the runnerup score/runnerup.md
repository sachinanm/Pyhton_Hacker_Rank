# Runner-Up Score Finder 🏃‍♀️

This repository contains a simple Python code example that finds the runner-up score from a list of participant scores. 

# Question
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  n scores. Store them in a list and find the score of the runner-up.
# Input Format

The first line contains n . The second line contains an array  A[] of n integers each separated by a space.

# Output Format

Print the runner-up score.

Constraints
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  n scores. Store them in a list and find the score of the runner-up.
## Code Snippet 📝🔍

```python
if __name__ == '__main__':
    n = int(input())  # Read the number of participants
    arr = map(int, input().split())  # Read space-separated scores
    arr = list(set(arr))  # Convert set to list to remove duplicates
    arr.sort()  # Sort the list in ascending order
    print(arr[-2])  # Print the second highest score (runner-up)
```

# Contributing 🤝❤️
Contributions are welcome! If you have improvements, bug fixes, or additional examples related to finding the runner-up score, feel free to fork this repository, make changes, and create a pull request.

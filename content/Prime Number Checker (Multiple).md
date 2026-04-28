---
title: Prime Number Checker (Multiple)
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
tasks = []

def add_task():
    t = input("Enter task: ")
    tasks.append(t)
    print("Task added")

def view_tasks():
    if len(tasks) == 0:
        print("No tasks")
    else:
        i = 1
        for t in tasks:
            print(i, ".", t)
            i += 1

def delete_task():
    view_tasks()
    if len(tasks) > 0:
        num = int(input("Enter task number: "))
        if num >= 1 and num <= len(tasks):
            removed = tasks.pop(num - 1)
            print("Removed:", removed)
        else:
            print("Invalid number")

while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_task()
    elif ch == "2":
        view_tasks()
    elif ch == "3":
        delete_task()
    elif ch == "4":
        break
    else:
        print("Invalid")
```

    
    1.Add 2.View 3.Delete 4.Exit
    

    Choice:  1
    Enter task:  complete assignment
    

    Task added
    
    1.Add 2.View 3.Delete 4.Exit
    

    Choice:  4
    


```python
def check_palindrome():
    text = input("Enter a string: ")

    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text

    print("Reversed:", reversed_text)

    if text == reversed_text:
        print("It is a palindrome")
    else:
        print("Not a palindrome")

def multiple_check():
    n = int(input("How many words to check: "))
    for i in range(n):
        print("\nCheck", i+1)
        check_palindrome()

while True:
    print("\n1.Check Palindrome 2.Multiple Check 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        check_palindrome()
    elif ch == "2":
        multiple_check()
    elif ch == "3":
        break
    else:
        print("Invalid choice")
```

    
    1.Check Palindrome 2.Multiple Check 3.Exit
    

    Choice:  1
    Enter a string:  mam
    

    Reversed: mam
    It is a palindrome
    
    1.Check Palindrome 2.Multiple Check 3.Exit
    

    Choice:  3
    


```python
def is_prime(n):
    if n <= 1:
        return False

    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1

    return True

def check_primes():
    count = int(input("How many numbers: "))
    nums = []

    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        nums.append(num)

    for n in nums:
        if is_prime(n):
            print(n, "is Prime")
        else:
            print(n, "is Not Prime")

check_primes()
```

    How many numbers:  3
    Enter number 1:  1
    Enter number 2:  2
    Enter number 3:  4
    

    1 is Not Prime
    2 is Prime
    4 is Not Prime
    


```python

```


---
**Score: 0**
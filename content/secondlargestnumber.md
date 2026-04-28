---
title: Secondlargestnumber
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
def factorial():
    num = int(input("Enter number: "))

    if num < 0:
        print("Invalid")
        return

    fact = 1
    i = 1

    while i <= num:
        fact *= i
        i += 1

    print("Factorial:", fact)

while True:
    print("\n1.Find 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        factorial()
    elif ch == "2":
        factorial()
    elif ch == "3":
        print("Skipped")
    elif ch == "4":
        break
    else:
        print("Invalid")
```

    
    1.Find 2.Again 3.Skip 4.Exit
    

    Choice:  1
    Enter number:  5
    

    Factorial: 120
    
    1.Find 2.Again 3.Skip 4.Exit
    

    Choice:  4
    


```python
def remove_duplicates():
    n = int(input("Enter count: "))
    arr = []
    result = []

    for i in range(n):
        val = int(input("Enter number: "))
        arr.append(val)

    for num in arr:
        if num not in result:
            result.append(num)

    print("After removing duplicates:", result)

while True:
    print("\n1.Remove 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        remove_duplicates()
    elif ch == "2":
        remove_duplicates()
    elif ch == "3":
        print("Skip")
    elif ch == "4":
        break
    else:
        print("Invalid")
```

    
    1.Remove 2.Again 3.Skip 4.Exit
    

    Choice:  4
    


```python
def second_largest():
    n = int(input("Enter count: "))

    if n < 2:
        print("Need at least 2 numbers")
        return

    arr = []
    for i in range(n):
        val = int(input(f"Enter element {i+1}: "))
        arr.append(val)

    largest = arr[0]
    second = arr[0]

    for num in arr:
        if num > largest:
            second = largest
            largest = num

    for num in arr:
        if num > second and num != largest:
            second = num

    print("Second largest:", second)

while True:
    print("\n1.Find 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1" or ch == "2":
        second_largest()
    elif ch == "3":
        print("Skip")
    elif ch == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
```

    
    1.Find 2.Again 3.Skip 4.Exit
    

    Choice:  1
    Enter count:  3
    Enter element 1:  12 
    Enter element 2:  34
    Enter element 3:  67
    

    Second largest: 34
    
    1.Find 2.Again 3.Skip 4.Exit
    

    Choice:  4
    

    Program exited
    


```python

```


---
**Score: 0**
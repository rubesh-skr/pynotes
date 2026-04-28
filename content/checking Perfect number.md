---
title: Checking Perfect Number
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
def simple_interest():
    p = float(input("Enter principal: "))
    r = float(input("Enter rate: "))
    t = float(input("Enter time: "))

    si = (p * r * t) / 100

    print("Simple Interest:", si)

while True:
    print("\n1.Calculate 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1" or ch == "2":
        simple_interest()
    elif ch == "3":
        print("Skip")
    elif ch == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
```

    
    1.Calculate 2.Again 3.Skip 4.Exit
    

    Choice:  1
    Enter principal:  3
    Enter rate:  89000
    Enter time:  3
    

    Simple Interest: 8010.0
    
    1.Calculate 2.Again 3.Skip 4.Exit
    

    Choice:  4
    

    Program exited
    


```python
def reverse_number():
    num = int(input("Enter number: "))
    temp = num
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10

    print("Original:", num)
    print("Reversed:", rev)

while True:
    print("\n1.Reverse 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1" or ch == "2":
        reverse_number()
    elif ch == "3":
        print("Skipped")
    elif ch == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
```

    
    1.Reverse 2.Again 3.Skip 4.Exit
    

    Choice:  1
    Enter number:  45
    

    Original: 45
    Reversed: 54
    
    1.Reverse 2.Again 3.Skip 4.Exit
    

    Choice:  4
    

    Program exited
    


```python
def perfect_number():
    num = int(input("Enter number: "))
    total = 0

    i = 1
    while i < num:
        if num % i == 0:
            total += i
        i += 1

    print("Sum of factors:", total)

    if total == num:
        print("Perfect number")
    else:
        print("Not a perfect number")

while True:
    print("\n1.Check 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1" or ch == "2":
        perfect_number()
    elif ch == "3":
        print("Skipped")
    elif ch == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
```

    
    1.Check 2.Again 3.Skip 4.Exit
    

    Choice:  1
    Enter number:  3
    

    Sum of factors: 1
    Not a perfect number
    
    1.Check 2.Again 3.Skip 4.Exit
    

    Choice:  4
    

    Program exited
    


```python

```


---
**Score: 0**
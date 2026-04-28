---
title: Sum Of Array
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
def count_words():
    text = input("Enter sentence: ")
    words = text.split()

    count = 0
    for w in words:
        count += 1

    print("Word count:", count)

while True:
    print("\n1.Count 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1" or ch == "2":
        count_words()
    elif ch == "3":
        print("Skip")
    elif ch == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
```

    
    1.Count 2.Again 3.Skip 4.Exit
    

    Choice:  1
    Enter sentence:  hello world
    

    Word count: 2
    
    1.Count 2.Again 3.Skip 4.Exit
    

    Choice:  4
    

    Program exited
    


```python
def armstrong():
    num = int(input("Enter number: "))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit * digit * digit
        temp = temp // 10

    if total == num:
        print("Armstrong number")
    else:
        print("Not Armstrong")

while True:
    print("\n1.Check 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1" or ch == "2":
        armstrong()
    elif ch == "3":
        print("Skip")
    elif ch == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
```

    
    1.Check 2.Again 3.Skip 4.Exit
    

    Choice:  1
    Enter number:  5
    

    Not Armstrong
    
    1.Check 2.Again 3.Skip 4.Exit
    

    Choice:  4
    

    Program exited
    


```python
def sum_array():
    n = int(input("Enter count: "))
    total = 0

    for i in range(n):
        val = int(input(f"Enter element {i+1}: "))
        total += val

    print("Sum:", total)

while True:
    print("\n1.Sum 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1" or ch == "2":
        sum_array()
    elif ch == "3":
        print("Skip")
    elif ch == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
```

    
    1.Sum 2.Again 3.Skip 4.Exit
    

    Choice:  1
    Enter count:  2
    Enter element 1:  23
    Enter element 2:  56
    

    Sum: 79
    
    1.Sum 2.Again 3.Skip 4.Exit
    


```python

```


---
**Score: 0**
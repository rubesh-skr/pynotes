---
title: Simple Menu Based System
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
def count_digits():
    num = int(input("Enter number: "))

    if num == 0:
        print("Digits: 1")
        return

    count = 0
    temp = num

    while temp != 0:
        temp = temp // 10
        count += 1

    print("Number:", num)
    print("Digits count:", count)

while True:
    print("\n1.Count 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1" or ch == "2":
        count_digits()
    elif ch == "3":
        print("Skipped")
    elif ch == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
```


```python
def find_minimum():
    n = int(input("Enter count: "))

    if n <= 0:
        print("Invalid count")
        return

    arr = []

    for i in range(n):
        val = int(input(f"Enter element {i+1}: "))
        arr.append(val)

    minimum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num

    print("List:", arr)
    print("Minimum value:", minimum)

while True:
    print("\n1.Find 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1" or ch == "2":
        find_minimum()
    elif ch == "3":
        print("Skipped")
    elif ch == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
```


```python
balance = 0

def deposit():
    global balance
    amt = float(input("Enter amount to deposit: "))
    if amt > 0:
        balance += amt
        print("Deposited successfully")
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amt = float(input("Enter amount to withdraw: "))
    if amt <= balance:
        balance -= amt
        print("Withdraw successful")
    else:
        print("Insufficient balance")

def check_balance():
    print("Current balance:", balance)

while True:
    print("\n1.Deposit 2.Withdraw 3.Check Balance 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        deposit()
    elif ch == "2":
        withdraw()
    elif ch == "3":
        check_balance()
    elif ch == "4":
        print("Thank you! Program exited")
        break
    else:
        print("Invalid choice")
```


```python

```


---
**Score: 0**
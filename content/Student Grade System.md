---
title: Student Grade System
date: 2026-04-28
author: Your Name
cell_count: 9
score: 5
---

```python
students = {}

def add_student():
    name = input("Enter name: ")
    marks = []
    n = int(input("Enter number of subjects: "))

    for i in range(n):
        m = int(input(f"Enter mark {i+1}: "))
        marks.append(m)

    students[name] = marks
    print("Student added!")

def view_students():
    if len(students) == 0:
        print("No data available")
    else:
        for name in students:
            total = 0
            for m in students[name]:
                total += m
            avg = total / len(students[name])
            print(name, "->", students[name], "Average:", avg)

def delete_student():
    name = input("Enter name to delete: ")
    if name in students:
        del students[name]
        print("Deleted successfully")
    else:
        print("Student not found")

while True:
    print("\n1.Add 2.View 3.Delete 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        add_student()
    elif ch == "2":
        view_students()
    elif ch == "3":
        delete_student()
    elif ch == "4":
        break
    else:
        print("Invalid choice")
```

    
    1.Add 2.View 3.Delete 4.Exit
    

    Choice:  1
    Enter name:  ravi
    Enter number of subjects:  3
    Enter mark 1:  80
    Enter mark 2:  90
    Enter mark 3:  80
    

    Student added!
    
    1.Add 2.View 3.Delete 4.Exit
    

    Choice:  2
    

    ravi -> [80, 90, 80] Average: 83.33333333333333
    
    1.Add 2.View 3.Delete 4.Exit
    

    Choice:  4
    


```python

```


```python
history = []

def calculate():
    a = float(input("Enter first number: "))
    op = input("Enter operator (+ - * /): ")
    b = float(input("Enter second number: "))

    if op == "+":
        res = a + b
    elif op == "-":
        res = a - b
    elif op == "*":
        res = a * b
    elif op == "/":
        if b != 0:
            res = a / b
        else:
            print("Division by zero not allowed")
            return
    else:
        print("Invalid operator")
        return

    print("Result:", res)
    history.append(str(a) + " " + op + " " + str(b) + " = " + str(res))

def show_history():
    if len(history) == 0:
        print("No history")
    else:
        for item in history:
            print(item)

while True:
    print("\n1.Calculate 2.History 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        calculate()
    elif ch == "2":
        show_history()
    elif ch == "3":
        break
    else:
        print("Invalid")
```

    
    1.Calculate 2.History 3.Exit
    

    Choice:  1
    Enter first number:  10
    Enter operator (+ - * /):  +
    Enter second number:  10
    

    Result: 20.0
    
    1.Calculate 2.History 3.Exit
    

    Choice:  3
    


```python

```


```python
number = 25   # fixed number (since no random import)
attempts = 0
max_attempts = 5

print("Guess the number (1-50)")

while attempts < max_attempts:
    guess = int(input("Enter guess: "))
    attempts += 1

    if guess == number:
        print("Correct! You win!")
        break
    elif guess < number:
        print("Too low")
    else:
        print("Too high")

    print("Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Game over! Number was", number)
```

    Guess the number (1-50)
    

    Enter guess:  20
    

    Too low
    Attempts left: 4
    

    Enter guess:  25
    

    Correct! You win!
    


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
    Enter number 1:  2
    Enter number 2:  4
    Enter number 3:  7
    

    2 is Prime
    4 is Not Prime
    7 is Prime
    


```python

```


---
**Score: 5**
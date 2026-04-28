---
title: Markprog
date: 2026-04-28
author: Your Name
cell_count: 2
score: 0
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
    Enter name:  rubi
    Enter number of subjects:  3
    Enter mark 1:  90
    Enter mark 2:  80
    Enter mark 3:  90
    

    Student added!
    
    1.Add 2.View 3.Delete 4.Exit
    

    Choice:  4
    


```python

```


---
**Score: 0**
---
title: Bubblesort
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
def linear_search():
    n = int(input("Enter number of elements: "))
    arr = []

    for i in range(n):
        val = int(input("Enter number: "))
        arr.append(val)

    key = int(input("Enter number to search: "))
    found = False

    for i in range(len(arr)):
        if arr[i] == key:
            print("Found at position", i + 1)
            found = True
            break

    if not found:
        print("Not found")

while True:
    print("\n1.Search 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        linear_search()
    elif ch == "2":
        linear_search()
    elif ch == "3":
        print("Skipping...")
    elif ch == "4":
        break
    else:
        print("Invalid")
```

    
    1.Search 2.Again 3.Skip 4.Exit
    

    Choice:  4
    


```python
def bubble_sort():
    n = int(input("Enter count: "))
    arr = []

    for i in range(n):
        arr.append(int(input("Enter number: ")))

    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j += 1
        i += 1

    print("Sorted list:", arr)

while True:
    print("\n1.Sort 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        bubble_sort()
    elif ch == "2":
        bubble_sort()
    elif ch == "3":
        print("Skipped")
    elif ch == "4":
        break
    else:
        print("Invalid")
```

    
    1.Sort 2.Again 3.Skip 4.Exit
    

    Choice:  4
    


```python
def count_even_odd():
    n = int(input("Enter count: "))
    even = 0
    odd = 0

    for i in range(n):
        num = int(input("Enter number: "))
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even:", even)
    print("Odd:", odd)

while True:
    print("\n1.Count 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        count_even_odd()
    elif ch == "2":
        count_even_odd()
    elif ch == "3":
        print("Skip")
    elif ch == "4":
        break
    else:
        print("Invalid")
```

    
    1.Count 2.Again 3.Skip 4.Exit
    

    Choice:  5
    

    Invalid
    
    1.Count 2.Again 3.Skip 4.Exit
    

    Choice:  4
    


```python

```


---
**Score: 0**
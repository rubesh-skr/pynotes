---
title: Rube5
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
# Program 9: Positive/Negative
def main():
    num = int(input("Enter number: "))
    
    print("Checking...")
    
    if num >= 0:
        print("Positive number")
    else:
        print("Negative number")

main()
```

    Enter number:  2
    

    Checking...
    Positive number
    


```python
# Program 10: Sum of N numbers
def main():
    n = int(input("Enter value: "))
    
    total = 0
    
    for i in range(1, n+1):
        total += i
    
    print("Sum is:", total)

main()
```

    Enter value:  24
    

    Sum is: 300
    


```python
# Program 11: Multiplication Table
def main():
    num = int(input("Enter number: "))
    
    print("Multiplication Table:")
    
    for i in range(1, 11):
        result = num * i
        print(num, "x", i, "=", result)

main()
```

    Enter number:  2
    

    Multiplication Table:
    2 x 1 = 2
    2 x 2 = 4
    2 x 3 = 6
    2 x 4 = 8
    2 x 5 = 10
    2 x 6 = 12
    2 x 7 = 14
    2 x 8 = 16
    2 x 9 = 18
    2 x 10 = 20
    


```python

```


---
**Score: 0**
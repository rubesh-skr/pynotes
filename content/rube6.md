---
title: Rube6
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
# Program 12: Factorial
def main():
    n = int(input("Enter number: "))
    
    fact = 1
    
    for i in range(1, n+1):
        fact = fact * i
    
    print("Factorial is:", fact)

main()
```

    Enter number:  3
    

    Factorial is: 6
    


```python
# Program 13: Reverse Number
def main():
    num = int(input("Enter number: "))
    
    rev = 0
    
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    
    print("Reversed number:", rev)

main()
```

    Enter number:  5
    

    Reversed number: 5
    


```python
# Program 14: Count Digits
def main():
    num = int(input("Enter number: "))
    
    count = 0
    
    while num > 0:
        count = count + 1
        num = num // 10
    
    print("Total digits:", count)

main()
```

    Enter number:  4
    

    Total digits: 1
    


```python

```


---
**Score: 0**
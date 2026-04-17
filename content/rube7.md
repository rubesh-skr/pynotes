---
title: Rube7
date: 2026-04-17
author: Your Name
cell_count: 4
score: 0
---

```python
# Program 15: Sum of Digits
def main():
    num = int(input("Enter number: "))
    
    total = 0
    
    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10
    
    print("Sum of digits:", total)

main()
```

    Enter number:  12
    

    Sum of digits: 3
    


```python
# Program 16: Palindrome Number
def main():
    num = int(input("Enter number: "))
    
    original = num
    reverse = 0
    
    while num > 0:
        reverse = reverse * 10 + num % 10
        num = num // 10
    
    if original == reverse:
        print("Palindrome")
    else:
        print("Not Palindrome")

main()
```

    Enter number:  33
    

    Palindrome
    


```python
# Program 17: Fibonacci Series
def main():
    n = int(input("Enter terms: "))
    
    a = 0
    b = 1
    
    for i in range(n):
        print(a)
        temp = a + b
        a = b
        b = temp

main()
```

    Enter terms:  2
    

    0
    1
    


```python

```


---
**Score: 0**
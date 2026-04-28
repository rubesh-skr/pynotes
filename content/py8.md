---
title: Py8
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
# Program 18: Prime Check
def main():
    num = int(input("Enter number: "))
    
    flag = 0
    
    for i in range(2, num):
        if num % i == 0:
            flag = 1
    
    if flag == 0 and num > 1:
        print("Prime number")
    else:
        print("Not prime")

main()
```

    Enter number:  23
    

    Prime number
    


```python
# Program 19: GCD
def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    while b != 0:
        temp = b
        b = a % b
        a = temp
    
    print("GCD is:", a)

main()
```

    Enter first number:  7
    Enter second number:  9
    

    GCD is: 1
    


```python
# Program 20: LCM
def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    if a > b:
        greater = a
    else:
        greater = b
    
    while True:
        if greater % a == 0 and greater % b == 0:
            print("LCM is:", greater)
            break
        greater += 1

main()
```

    Enter first number:  6
    Enter second number:  9
    

    LCM is: 18
    


```python

```


---
**Score: 0**
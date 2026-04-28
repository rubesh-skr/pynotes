---
title: Number Palindrome (Integer)
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
def fibonacci():
    n = int(input("Enter number of terms: "))

    a = 0
    b = 1

    if n <= 0:
        print("Invalid input")
        return

    print("Fibonacci Series:")

    i = 0
    while i < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        i += 1

    print()

fibonacci()
```

    Enter number of terms:  6
    

    Fibonacci Series:
    0 1 1 2 3 5 
    


```python
def number_palindrome():
    num = int(input("Enter number: "))
    temp = num
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10

    print("Reversed:", rev)

    if num == rev:
        print("Palindrome Number")
    else:
        print("Not a Palindrome")

def repeat_check():
    n = int(input("How many numbers: "))
    for i in range(n):
        number_palindrome()

repeat_check()
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Cell In[3], line 23
         19     n = int(input("How many numbers: "))
         20     for i in range(n):
         21         number_palindrome()
         22 
    ---> 23 repeat_check()
    

    Cell In[3], line 19, in repeat_check()
         18 def repeat_check():
    ---> 19     n = int(input("How many numbers: "))
         20     for i in range(n):
         21         number_palindrome()
    

    File ~\miniconda3\Lib\site-packages\ipykernel\kernelbase.py:1403, in Kernel.raw_input(self, prompt)
       1401     msg = "raw_input was called, but this frontend does not support input requests."
       1402     raise StdinNotImplementedError(msg)
    -> 1403 return self._input_request(
       1404     str(prompt),
       1405     self._get_shell_context_var(self._shell_parent_ident),
       1406     self.get_parent("shell"),
       1407     password=False,
       1408 )
    

    File ~\miniconda3\Lib\site-packages\ipykernel\kernelbase.py:1448, in Kernel._input_request(self, prompt, ident, parent, password)
       1445 except KeyboardInterrupt:
       1446     # re-raise KeyboardInterrupt, to truncate traceback
       1447     msg = "Interrupted by user"
    -> 1448     raise KeyboardInterrupt(msg) from None
       1449 except Exception:
       1450     self.log.warning("Invalid Message:", exc_info=True)
    

    KeyboardInterrupt: Interrupted by user



```python
def table():
    num = int(input("Enter number: "))
    limit = int(input("Enter limit: "))

    i = 1
    print("Multiplication Table:")

    while i <= limit:
        result = num * i
        print(num, "x", i, "=", result)
        i += 1

def multiple_tables():
    n = int(input("How many tables: "))
    for i in range(n):
        print("\nTable", i+1)
        table()

multiple_tables()
```

    How many tables:  5
    

    
    Table 1
    

    Enter number:  7
    Enter limit:  8
    

    Multiplication Table:
    7 x 1 = 7
    7 x 2 = 14
    7 x 3 = 21
    7 x 4 = 28
    7 x 5 = 35
    7 x 6 = 42
    7 x 7 = 49
    7 x 8 = 56
    
    Table 2
    


```python

```


---
**Score: 0**
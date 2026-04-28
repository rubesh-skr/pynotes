---
title: Pattern Printing (Triangle
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
username = "admin"
password = "1234"

def login():
    u = input("Enter username: ")
    p = input("Enter password: ")

    if u == username and p == password:
        print("Login Successful")
    else:
        print("Invalid credentials")

def attempts():
    tries = 3

    while tries > 0:
        login()
        tries -= 1
        print("Attempts left:", tries)

attempts()
```

    Enter username:  admin
    Enter password:  1234
    

    Login Successful
    Attempts left: 2
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Cell In[1], line 21
         17         login()
         18         tries -= 1
         19         print("Attempts left:", tries)
         20 
    ---> 21 attempts()
    

    Cell In[1], line 17, in attempts()
         13 def attempts():
         14     tries = 3
         15 
         16     while tries > 0:
    ---> 17         login()
         18         tries -= 1
         19         print("Attempts left:", tries)
    

    Cell In[1], line 5, in login()
          4 def login():
    ----> 5     u = input("Enter username: ")
          6     p = input("Enter password: ")
          7 
          8     if u == username and p == password:
    

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
def sum_digits():
    num = int(input("Enter number: "))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10

    print("Sum of digits:", total)

def repeat():
    n = int(input("How many numbers: "))
    for i in range(n):
        sum_digits()

repeat()
```

    How many numbers:  123
    Enter number:  1234
    

    Sum of digits: 10
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Cell In[2], line 17
         13     n = int(input("How many numbers: "))
         14     for i in range(n):
         15         sum_digits()
         16 
    ---> 17 repeat()
    

    Cell In[2], line 15, in repeat()
         12 def repeat():
         13     n = int(input("How many numbers: "))
         14     for i in range(n):
    ---> 15         sum_digits()
    

    Cell In[2], line 2, in sum_digits()
          1 def sum_digits():
    ----> 2     num = int(input("Enter number: "))
          3     total = 0
          4 
          5     while num > 0:
    

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
def pattern():
    n = int(input("Enter rows: "))

    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print("*", end=" ")
            j += 1
        print()
        i += 1

def repeat():
    t = int(input("How many patterns: "))
    for i in range(t):
        pattern()

repeat()
```

    How many patterns:  5
    Enter rows:  5
    

    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    


```python

```


---
**Score: 0**
---
title: Largestinlist
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python
def count_chars():
    text = input("Enter string: ")

    vowels = "aeiouAEIOU"
    v = 0
    c = 0

    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1

    print("Vowels:", v)
    print("Consonants:", c)

def repeat():
    n = int(input("How many times: "))
    for i in range(n):
        count_chars()

repeat()
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Cell In[4], line 23
         19     n = int(input("How many times: "))
         20     for i in range(n):
         21         count_chars()
         22 
    ---> 23 repeat()
    

    Cell In[4], line 19, in repeat()
         18 def repeat():
    ---> 19     n = int(input("How many times: "))
         20     for i in range(n):
         21         count_chars()
    

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
def reverse_words():
    text = input("Enter sentence: ")
    words = text.split()

    rev_sentence = ""

    i = len(words) - 1
    while i >= 0:
        rev_sentence += words[i] + " "
        i -= 1

    print("Reversed sentence:", rev_sentence)

def repeat():
    n = int(input("How many sentences: "))
    for i in range(n):
        reverse_words()

repeat()
```

    How many sentences:  python
    


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[6], line 19
         15     n = int(input("How many sentences: "))
         16     for i in range(n):
         17         reverse_words()
         18 
    ---> 19 repeat()
    

    Cell In[6], line 15, in repeat()
         14 def repeat():
    ---> 15     n = int(input("How many sentences: "))
         16     for i in range(n):
         17         reverse_words()
    

    ValueError: invalid literal for int() with base 10: 'python'



```python
def find_largest():
    n = int(input("Enter count: "))
    nums = []

    for i in range(n):
        val = int(input("Enter number: "))
        nums.append(val)

    largest = nums[0]

    for num in nums:
        if num > largest:
            largest = num

    print("Largest:", largest)

def repeat():
    t = int(input("How many times: "))
    for i in range(t):
        find_largest()

repeat()
```

    How many times:  4
    Enter count:  10
    Enter number:  50
    Enter number:  30
    Enter number:  20
    Enter number:  50
    Enter number:  50
    


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Cell In[7], line 22
         18     t = int(input("How many times: "))
         19     for i in range(t):
         20         find_largest()
         21 
    ---> 22 repeat()
    

    Cell In[7], line 20, in repeat()
         17 def repeat():
         18     t = int(input("How many times: "))
         19     for i in range(t):
    ---> 20         find_largest()
    

    Cell In[7], line 6, in find_largest()
          2     n = int(input("Enter count: "))
          3     nums = []
          4 
          5     for i in range(n):
    ----> 6         val = int(input("Enter number: "))
          7         nums.append(val)
          8 
          9     largest = nums[0]
    

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

```


---
**Score: 0**
---
title: Py9
date: 2026-04-17
author: Your Name
cell_count: 4
score: 0
---

```python
# Program 21: ASCII Value
def main():
    ch = input("Enter character: ")
    
    print("Character is:", ch)
    
    value = ord(ch)
    
    print("ASCII value is:", value)

main()
```

    Enter character:  f
    

    Character is: f
    ASCII value is: 102
    


```python
# Program 22: Alphabet Check
def main():
    ch = input("Enter character: ")
    
    print("Checking...")
    
    if ch.isalpha():
        print("It is an alphabet")
    else:
        print("Not an alphabet")

main()
```

    Enter character:  a
    

    Checking...
    It is an alphabet
    


```python
# Program 23: Count Vowels
def main():
    text = input("Enter string: ")
    
    count = 0
    
    for ch in text:
        if ch in "aeiouAEIOU":
            count += 1
    
    print("Vowel count:", count)

main()
```

    Enter string:  cricket
    

    Vowel count: 2
    


```python

```


---
**Score: 0**
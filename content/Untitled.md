---
title: Untitled
date: 2026-04-28
author: Your Name
cell_count: 2
score: 0
---

```python
def count_words():
    text = input("Enter sentence: ")
    words = text.split()

    count = 0
    for w in words:
        count += 1

    print("Word count:", count)

while True:
    print("\n1.Count 2.Again 3.Skip 4.Exit")
    ch = input("Choice: ")

    if ch == "1" or ch == "2":
        count_words()
    elif ch == "3":
        print("Skip")
    elif ch == "4":
        print("Program exited")
        break
    else:
        print("Invalid choice")
```

    
    1.Count 2.Again 3.Skip 4.Exit
    

    Choice:  1
    Enter sentence:  rbui
    

    Word count: 1
    
    1.Count 2.Again 3.Skip 4.Exit
    

    Choice:  4
    

    Program exited
    


```python

```


---
**Score: 0**
---
title: Rube2
date: 2026-04-28
author: Your Name
cell_count: 4
score: 0
---

```python

# Program : Reverse List
numbers = [1, 2, 3, 4]

reversed_list = numbers[::-1]   # better method (doesn't change original)

print("Reversed:", reversed_list)

```

    Reversed: [4, 3, 2, 1]
    


```python
# Program : Multiply All Elements
numbers = [2, 3, 4]

result = 1
for num in numbers:
    result *= num

print("Multiplication Result:", result)
```

    Multiplication Result: 24
    


```python
n = int(input())
flag = 0
for i in range(2, n):
    if n % i == 0:
        flag = 1
        break
if flag == 0:
    print("Prime")
else:
    print("Not Prime")
```


```python

```


---
**Score: 0**
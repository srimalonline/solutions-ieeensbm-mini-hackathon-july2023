# 1. Hello IEEE NSBM

## Problem

### Description

Give your name as input in the variable name and print `Hello I'm [YOUR NAME] from IEEE NSBM!`.

### Input Format

The line should contain a string.

### Input Constraints

`1 ≤ name.length ≤ 100`

### Output Format

The output should be `Hello I'm [YOUR NAME] from IEEE NSBM!` on 1 line.

### Sample Input

```
John
``` 

### Sample Output

```
Hello I'm John from IEEE NSBM!
```

## Answer Explanation

As the question states, we are required to get an input(User's Name) to the program and display a greeting text saying `Hello I'm {Name taken through input} from IEEE NSBM!`

For example, In the sample input `John` is given as the input, so then the output should display as `Hello I'm John from IEEE NSBM!`.

### Steps:

1. First, we should take an input to the code:
```python
name = input()
```
2. Next we should combine the name to the greeting text and display it.
```python
print(f"Hello I'm {name} from IEEE NSBM!")
```

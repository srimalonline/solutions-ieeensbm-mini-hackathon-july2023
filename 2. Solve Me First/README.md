# 2. Solve Me First

## Problem

### Description

Complete the function _solveMeFirst_ to compute the sum of two integers.

**Example**  
![equation](https://latex.codecogs.com/png.image?\bg{black}{\color{white}a=7})
![equation](https://latex.codecogs.com/png.image?\bg{black}{\color{white}b=3})
Return `10`.

**Function Description**

Complete the _solveMeFirst_ function in the editor below.

_solveMeFirst_ has the following parameters:

- _int a_: the first value
- _int b_: the second value

Returns  
- _int_: the sum _a_ of _b_ and

### Input Constraints

`1 ≤ a ≤ 1000`
`1 ≤ b ≤ 1000`

### Sample Input

```
a = 2
b = 3
``` 

### Sample Output

```
5
```

## Answer Explanation

In this question, we are required to complete the function _solveMeFirst_.

The program should get two number inputs and display the sum of these 2 numbers. So, in the question the code snippet for handling inputs and outputs are already given, we only need to complete the function _solveMeFirst_ which has got 2 arguments and should return the sum of the 2 numbers.

For example, In the sample input `2`  and `3` are the inputs of `a` and `b` respectively, so then the output should be `5` as `2+3=5`.

### Steps:

1. The easiest way to get this done is just return the sum directly :
```python
def solveMeFirst(a, b):
	return a+b
```

# 3. Staircase

## Problem

### Description

Staircase detail

This is a staircase of  ![equation](https://latex.codecogs.com/png.image?\bg{black}{\color{white}n=4}) size :

```
   #
  ##
 ###
####
```

Its base and height are both equal to  ![equation](https://latex.codecogs.com/png.image?\bg{black}{\color{white}n}) . It is drawn using `#` symbols and spaces. _The last line is not preceded by any spaces._

Write a program that prints a staircase of size  ![equation](https://latex.codecogs.com/png.image?\bg{black}{\color{white}n}).

### Function Description

Complete the _staircase_ function in the editor below.

staircase has the following parameter(s):

- _int n_: an integer

**Print**

Print a staircase as described above.

### Input Format

A single integer, ![equation](https://latex.codecogs.com/png.image?\bg{black}{\color{white}n}), denoting the size of the staircase.

### Input Constraints

- ![equation](https://latex.codecogs.com/svg.image?\bg{black}\bg{black}{\color{White}0<n\leq&space;100})

### Output Format

Print a staircase of size ![equation](https://latex.codecogs.com/png.image?\bg{black}{\color{white}n}) using `#` symbols and spaces.

**Note**: The last line must have 0 spaces in it.

### Sample Input

```
6 
```

### Sample Output

```
     #
    ##
   ###
  ####
 #####
######
```

## Answer Explanation

In this question, we are required to print a right-aligned staircase with `#` with a elevation of `n`.

For example, In the sample input `6` is given as n, so the output should be:
```
     #
    ##
   ###
  ####
 #####
######
```

So, if we look at the output it is clear that the line number of each stair and `n` can be used to create this staircase. For instance If we substitute `i` as the line number of each stair on the staircase, each line of the staircase should have `n-i` no.of spaces ` ` and `i` no of hashes `#`. 

Let's see an example, 
If `n=10`, The output is:
```
1.  |         #
2.  |        ##
3.  |       ###
4.  |      ####
5.  |     #####
6.  |    ######
7.  |   #######
8.  |  ########
9.  | #########
10. |##########
```

We have added the line numbers for our ease.  So if we pick **line 7** for the explanation, `i=7` in this case and we see **7** hashes `#` in the line(which is *equal to* `i`) followed by **3** spaces which is `10-7` (which also could be taken as `n-i`).

### Steps:

In this question we need to print a right-aligned staircase of height `n` . Our code should be on the staircase function.

In the solution we are going to use, We are iterating through the 

1. First, we should make a loop which iterates `n` times for each stair starting from `1 ... n` :
```python
def staircase(n):
	for i in range(1, n+1):
		# Iteration for each stair
```
2. Next, we could use the multiplication operation `*` on strings as python allows that. So, there should be `n-i` no.of spaces ` ` and `i` no.of hashes `#` next to it on each stair. In case you are using any other language multiplication operator `*` may not support strings, you may have to use another loop to prepare the string of each stair.
```python
def staircase(n):
	for i in range(1, n+1):
        print((" "*(n-i))+("#"*i))
```

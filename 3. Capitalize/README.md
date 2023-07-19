# 3. Capitalize!

## Problem

### Description

You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, `alison heck` should be capitalized correctly as `Alison Heck`.

![equation](https://latex.codecogs.com/svg.image?\bg{black}\bg{black}{\color{White}{\color{Red}a}lison&space;{\color{Red}h}eck\Rightarrow&space;Alison&space;Heck})

Given a full name, your task is to _capitalize_ the name appropriately.

### Input Format

A single line of input containing the full name, `S` .

### Input Constraints

- `0 < S.length < 1000`
- The string consists of alphanumeric characters and spaces.

**Note:** in a word only the first character is capitalized. Example `12abc` when capitalized remains `12abc`.

### Output Format

Print the capitalized string, `S`.

### Sample Input

```
chris alan
``` 

### Sample Output

```
Chris Alan
```

## Answer Explanation

In this question, we are required to display the capitalized version of the string `S` which is taken as input.

For example, In the sample input `chris alan` is given as the input, so then the output should display as `Chris Alan`. 

The question further explains the procedure, if something like `123sd` is give as input the word cannot be capitalized because it's a number in front of the word.

### Extra Info:

In python, there are many built-in functions for string formatting. When considering this the first idea we get for this question is using something like the `.title()` built-in function, but in this case it's not usable as the function will not produce the exact outputs we need. For example, If  `He'll finish his assignments today` is given as input the output in this problem should be `He'll Finish His Assignments Today`, but by using the `.title()` the output becomes `He'Ll Finish His Assignments Today` which is not the expected answer for this question. 

Also, the next option we found was the `string.capwords()` function from the `string` library, but still the `string.capwords()` function will produce an output which will not suit the expectations of the question in cases like use of abbreviations. For example, if `they're bill's friends from the UK` is the input the output given by the `string.capwords()` function will be `They're Bill's Friends From The Uk`  which is also not usable for our situation because as you see the `... UK` abbreviation became `... Uk` . So, we made our own way of doing this.

### Steps:

In this question we only need to complete the _solve()_ function in the given snippet as the code snippet for input & output handling is already given, the _solve()_ function gets a argument `s`, which is the input string.

So, the code should iterate through this string and sort out the words in the string and capitalize the first letter of each word. In order to sort out words in the string we could iterate through all characters in the string and detect the spaces, if a space is detected then the next character should be capitalized. The next question raised is if there is a number or a symbol next to the space? We are using the `.upper()` function to capitalize the individual character, so if there is a non-alphabetical character given to this function, it will just ignore the character and continue.

1. First, we should make a loop to iterate through the string `s` :
```python
# Complete the solve function below.
def solve(s):
	for i in range(len(s)):
		# String iteration
```
2. Inside the iteration we should detect the spaces in the string and capitalize the character next to the space :
```python
# Complete the solve function below.
def solve(s):
	for i in range(len(s)):
		if(s[i]==" "):
			s = s[:i+1]+s[i+1].upper()+s[i+2:]
```
3. Almost missed it!😬 We need to capitalize the first character of the string `s` ( because the first character of the string is the first character of the first word in the string and the first word of the string does not have a space before the first word ) :
```python
# Complete the solve function below.
def solve(s):
	for i in range(len(s)):
		if(i==0):
			s = s[0].upper()+s[1:]
		if(s[i]==" "):
			s = s[:i+1]+s[i+1].upper()+s[i+2:]
```
4. (Optional) Also we could reduce the no.of iterations in the loop by **1**, because the last character of the string is does not have a character next to it to be checked, which will always make it a useless iteration. 
```python
# Complete the solve function below.
def solve(s):
	for i in range(len(s)-1):
		if(i==0):
			s = s[0].upper()+s[1:]
		if(s[i]==" "):
			s = s[:i+1]+s[i+1].upper()+s[i+2:]
```
5. We should return the final result from the function. So, the program can handle the relevant operations to displaying the output
```python
# Complete the solve function below.
def solve(s):
	for i in range(len(s)-1):
		if(i==0):
			s = s[0].upper()+s[1:]
		if(s[i]==" "):
			s = s[:i+1]+s[i+1].upper()+s[i+2:]
return s
```
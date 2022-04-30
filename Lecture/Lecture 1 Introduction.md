[[CS61A]]
[CS61A Textbook](https://composingprograms.com/)

![[Lecture 1.pdf]]
# Introduction

## What is Computer Science?
+ Systems
+ Artificial Intelligence
+ Graphics
+ Security
+ Networking
+ Programming Languages
+ Theory
+ Scientific Computing

Common Enemy: complexity

## What is This Course About
+ A course about managing complexity
	+ Mastering abstraction
	+ Programming paradigms
	+ Not all about 0's and 1's
+ An introduction to Python
	+ Full understanding of language fundamentals
	+ Learning through implementation
	+ How computers interpret programming languages

## Expressions
### Type of expressions
An expression describes a computation and evaluates to a value

call expresion:
+ `max(1, 2)`
+ `min(2, 4)`

importing libraries & nesting structure:
`from operator import add, mul`

`add(2, mul(2, 4))`

### Anatomy of a Call Expression
`add(2,3)` Operators and operands

Evaluation procedure for call expressions:
1. Evaluate the operator and then the operand subexpressions
2. **Apply** the **function** that is the value of the operator subexpression to the **arguments** that are the values of the operand subexpression

**expression tree**:
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202204301553782.png)

## Functions, Objects and Interpreters
![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202204301559174.png)

![](https://cdn.jsdelivr.net/gh/YikunHan42/Image-Host/202204301602308.png)

## Colorful Algorithm

### Background and Objectives

We can break a number into different contiguous sub-subsequence parts. For example, the number 324 can be broken into parts like (3, 2, 4, 32, 24, 324). A colorful number is a number where the products of all the subsets of the digits are different. eg:

263 is a colorful number (2, 6, 3, 2x6, 6x3, 2x6x3) are all different
236 is not (2, 3, 6, 2x3, 3x6, 2x3x6) has 6 twice (6 and 2x3)

### Specs
The function `is_colorful` takes a single number n as an argument and returns a tuple (L, b) where b is a boolean saying if n is colorful and L is the list of all products of subsequences of n. 

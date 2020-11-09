# Test problem and solution

This repository contains the test problem and possible solution submitted by Ayan Chandra. 

## Problem 1

For a movie hall, given a seating arrangement of M rows and N columns, every person is seated such that, no one sits adjacent to him or her from front, behind, left, right and diagonally any direction also. An input K is given, based on which, it is to be decided if K persons can be accomodated in the hall using the above  rule. 

## Problem 2 
If K persons can be accomodated, in how many different ways they can be accomodated?

Prob1.py file contains the solution to the Problem 1. For this problem, I have given the complete solution. The idea was to break down the hall (matrix) into 2x2 boxes. 

For prob2.py, I am not able to provide any solution. It seemed really difficult to consider all cases.  
For K=1, number of ways f(1)= C\(mxn,1\) , where C is the combination. For k=2, number of ways f(2) = number of ways to choose 1 x number of ways to choose the second 2 given the first 1.   
f(2) = f(1) x number of ways to choose the second 2 given the first 1. Again, number of ways to choose the second 2 given the first 1 is a hard thing to calculate--> and, there is no exact pattern to be establish that I can generically put as f(k) = f(k-1) x g. Here, if g is dependent on any of the variables here or known values or prior values, the problem would have been solvable easily.    
The problem can be much simpler and we can use Backtracking like N-queens' problem if there had been a constraint like no two seats can be there in a single row or column.  
Alternatively, I can think of any approach where we do it like, Number of ways = (number of all possible ways to place k persons - number of ways where they are violating the rules)

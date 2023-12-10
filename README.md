# Advent Of Code 2023

Small project to work my python for Advent Of Code 2023 : https://adventofcode.com/

# Interesting solutions

## Day 6: Wait For It

Use of DataFrame to treat all the data simultaneously.

## Day 8

First approach was brute force and a loop was trying to rach the solution where all postion finish with a Z.
This was done with a recursion, but to many recursions lead to a system error.

With the help of reddit, I figure out that each path "--A" -> "--Z" is cyclic (always the same number of iteration).
So, step 1 is to identify the number of step of each cycle. And step 2 is to find the PPCM (Plus Petit Commun Multiple)

## Day 9

The chosen solution is a simple recursion, with an update of the input.
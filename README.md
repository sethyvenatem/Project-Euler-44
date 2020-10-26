# Project-Euler-44

I am starting to learn Python. I have decided to do this by solving problems from the project euler (https://projecteuler.net/) list.

My solution to problem 44 https://projecteuler.net/problem=44

This is a brute force solution, but is gets the job done. The code:
- runs over 'all' pairs of integer numbers k and k+r. In practice, it stops when k>10000 and r>10000
- computes the numbers n and m such that the sum and difference of the pentagonal numbers associated to k+r and k are possible pentagonal numbers associated to n and m: It computes n and m as functions of k and r by solving P_{k+r}+P_k = P_n and P_{k+r}-P_k = P_m
- checks is n and m are integers and stops if they are.

It's ok to stop when k>10000 and r>10000 because we are looking for a solution that minimises P_m. I trust that the people at project Euler are not evil. I can alway tweak these two stopping conditions if necessary.

I solved 3 unexpected problems:
- In python 4*4 is 4**2, not 4^2. The latter does however exist in python. I don't know what it does yet.
- When k an r get large, rounding errors creep in and spoil the solution. I solved this by requiring that abs(round(n)-n)<10**(-12) (and identically for m) instead of abs(round(n)-n)=0 for perfect integers.
- In nested loops, the second counter must be re-initialised at every outer loop.

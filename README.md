# Analytical-and-Computational

These codes focuses on building the algorithm for The Babylonian (or Heron's) Method for computing the square root of a real positive number, using iterative sequence (x_n), where x_0 is an arbitrary starting value and x_i for i > 0 is defined iteratively by x_(n+1) = (x_n +a/x_n)/2. There will be a successive values computed for x_n until a desirable accuracy is achived. For that we just we set a maximum error to be x, we stop when n = N, where N is smallest positive integer such that absolute value of (x_N)^2 - a is less then e.

* The function babylonian_square_root(a,e,x) where the parameter a is our value for which we are trying to find the square root for, also we assert for a to be greater then 0. The parameter e is the tolerance value, also we assert for e to be greater then 0. The value of x is just the initual point at we start our convergence x_0. The function primerarly uses a while for loop to find the square root of a number.

* The function babylonian_square_root_list(a,e,x) where the parameters are the same as function above except in this function it outputs a list of the approximations [x_0,x_1,...,x_n].


* The third part of the Coursework. I was assigned to build a plot to demenstrate the convergence of the Babylonian Method and how it converges to the actual square root of a given number for this case that they wanted us to look at was the square root of 2000. 

In conclusion this code uses the help of while function, assert, lists and append also the library math and pylab to help demistrate this algorithm. 

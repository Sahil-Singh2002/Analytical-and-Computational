# Babylonian Method for Square Root Approximation

This repository contains code that implements the Babylonian (or Heron's) Method for computing the square root of a positive real number ${ x_{n+1} = \frac{1}{2} \left( x_n + \frac{a}{x_n} \right) }$. The method uses an iterative sequence $x_n$, where $x_0$ is an arbitrary starting value and $x_i$ for $i > 0$ is defined iteratively by ${ x_{n+1} = (x_n + a/x_n) / 2 }$. The algorithm continues calculating successive values of $x_n$ until a desired accuracy is achieved.

$$\textbf{Code Explanation}$$

The repository includes two functions and a plot:

### `babylonian_square_root(a, e, x)`

This function calculates the square root of a number using the Babylonian method. It takes three parameters: $a$ (the number for which we want to find the square root), $e$ (the desired tolerance), and $x$ (the initial point of convergence, $x_0$. The function includes assertions to ensure that $a > 0$ and $e > 0$. The function iteratively calculates $x_{n+1}$ until the desired accuracy is achieved and returns the approximation $x$ and the number of iterations $N$.

### `babylonian_square_root_list(a, e, x)`

This function is similar to the previous one but returns a list of all the approximations obtained during the iteration process, i.e., $[x_0, x_1, ..., x_n]$.

$$\textbf{Plot}$$

The code also includes a plot to demonstrate the convergence of the Babylonian Method. It uses the `pylab` library to create a scatter plot of the approximations obtained from the `babylonian_square_root_list` function. The actual square root of $a$ is plotted as a red line for comparison.

$$\textbf{Usage}$$

To use the code and generate the plot, follow these steps:

1. Install the required dependencies by running `pip install matplotlib` in your terminal.

2. Clone this repository to your local machine.

3. Open the code file `babylonian_square_root.py` and modify the values of $a$, $e$, and $x$ according to your requirements.

4. Run the code using a Python interpreter or an integrated development environment (IDE) of your choice.

5. The plot will be displayed, showing the convergence of the Babylonian Method for the given input values.

Feel free to explore and modify the code as needed!

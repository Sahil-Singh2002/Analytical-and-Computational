import pylab
import math

def babylonian_square_root(a, e, x):
    assert a > 0
    assert e > 0
    N = 0
    x = abs(0.5 * (x + (a / x)))
    while abs(x * x - a) > e * a:
        x = 0.5 * (x + (a / x))
        N += 1
    return x, N

def babylonian_square_root_list(a, e, x):
    assert a > 0
    assert e > 0
    x_list = [x]
    while abs(x_list[-1] * x_list[-1] - a) > e * a:
        x_list.append(0.5 * (x_list[-1] + (a / x_list[-1])))
    return x_list

xy = babylonian_square_root_list(20000, 1e-10, 1)
xv = pylab.linspace(0, len(xy), len(xy))
vu = [math.sqrt(20000) for _ in range(len(xv))]
pylab.scatter(xv, xy, label='$x_n$')
pylab.plot(xv, vu, label="$\sqrt{20000}$", color="red")

pylab.legend(loc='lower left')
pylab.xlabel('$n$')
pylab.ylabel('$Approximation$')

pylab.show()

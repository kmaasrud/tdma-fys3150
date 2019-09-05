# Project 1 c)
## Modified algorithm

In this case we use our general algorithm derived in Project 1 b) and simply replace our variables $a_i, b_i \, \textrm{and}\, c_i \,\textrm{with respectively} -1, 2 \,\,\textrm{and} -1$.

$$\\
\mathbf{A}=\left[\begin{matrix}2 & -1 & 0 & \cdots & \cdots & \cdots\\-1 & 2 & -1 & 0 & &\\0 & -1 & 2 & -1 & 0 &\\\vdots&\vdots & \ddots& \ddots&\ddots &\vdots\\0 & & & -1 & 2 & -1\\0 & & &  & -1 & 2\end{matrix}\right] \left[\begin{matrix}v_1\\v_2\\ \cdots\\\cdots\\\cdots\\v_n\end{matrix}\right] = \left[\begin{matrix}d_1\\d_2\\ \cdots\\\cdots\\\cdots\\d_n\end{matrix}\right]
\\$$

## Forward substitution special case
$$\\
\tilde{b}_{i}=1\\
\tilde{c}_{1}=-\frac{1}{2}\\
\tilde c_i = -\frac{1}{2-(-1)a_{i-1}} = -\frac{1}{2 + \tilde c_{i-1}}\\
\tilde d_1 = \frac{d_1}{2}\\
\tilde d_i = \frac{d_i + \tilde d_{i-1}}{2+ \tilde c_{i-1}} \\
$$


## Backward substitution special case
In the backward substitution there will not have any differences from the one in Project 1 b), so

$$\\
v_n = \tilde d_i\\
v_{i}=\tilde{d}_{i}-\tilde{c}_{i}v_{i+1}
\\$$

For the general and special algorithm the flops will run as O(n).
By simplifying our algorithm the number of floating points, FLOPS, decreases from **9n** to **6n**.

The CPU time for the general algorithm:

<<<<<<< HEAD
The CPU time for special algorithm:
=======


$\\
2u_1 - u_2 = f_1 \\
\frac{3}{2}u_2 -u_3 = f_2 + \frac{1}{2}f_1\\
-u_2 + 2u_3 - u_4 = f_3\\
-u_3 + 2u_4 = f_4\\
\\$

set

$III + \frac{2}{3}\cdot II$

$\\
2u_1 - u_2 = f_1 \\
\frac{3}{2}u_2 -u_3 = f_2 + \frac{1}{2}f_1\\
\frac{4}{3}u_3 - u_4 = f_3 + \frac{2}{3}f_2 + \frac{1}{3}f_1 \\
-u_3 + 2u_4 = f_4\\
\\$


Last but not least ...

$IV + \frac{3}{4}\cdot III$

$\\
2u_1 - u_2 = f_1 \\
\frac{3}{2}u_2 -u_3 = f_2 + \frac{1}{2}f_1\\
\frac{4}{3}u_3 - u_4 = f_3 + \frac{2}{3}f_2 + \frac{1}{3}f_1 \\
\frac{5}{4}u_4 = f_4 + \frac{3}{4}f_3 + \frac{2}{4}f_2 + \frac{1}{4}f_1\\
\\$

###Generalized:
Right hand side

$\mathbf{Au} = x_i \frac {i+1}{i} = x_i\cdot i + x_i$

$\mathbf f =$

## FLOPS
>>>>>>> 02048f09f642aeccc835edbe1dac390ab42bebac

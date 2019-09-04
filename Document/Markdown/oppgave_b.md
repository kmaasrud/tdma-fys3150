# Project 1 b)
######General algorithm

We have a linear set of equations $\mathbf{Av = d}$

In the general case, we can express any tridiagonal matrix

$$\mathbf{A}=\left[\begin{matrix}b_1 & c_1 & 0 & \cdots & \cdots & 0 \\a_{1} & b_2 & c_2 & \ddots & \ddots &\vdots \\0 & a_{2} &b_3 & \ddots & \ddots &\vdots \\ \vdots& \ddots & \ddots& \ddots& c_{n-2} & 0 \\0 & \dots & 0 & a_{n-2} & b_{n-1} & c_{n-1}\\0 & \dots & \dots & 0 & a_{n-1} & b_n\end{matrix}\right]$$

just by the three vectors $a_, \, b \ \text{and} \, c$, where $b$ has length $n$, and $a$ and $c$ have length $n-1$.

## Forward substitution
Firstly, we want to eliminate the $a_{i}$'s.

$\mathbf{Av}=\mathbf{d}$ gives us these equations for the case of $i=1$ and $i=n$

$$b_{1}v_{1}+c_{1}v_{2}=d_{1},\ \ i=1 \ \ \ \ \ \ \ \ \ \ (1)$$
$$a_{n-1}v_{n-1}+b_{n}v_{n}=d_{n},\ \ i=n. \ \ \ \ \ \ \ \ \ \ (2)$$

For the rest, we get
$$a_{1}v_{1}+b_{2}v_{2}+c_{2}v_{3}=d_{2},\ \ i=2.  \ \ \ \ \ \ \ \ \ \ (3)$$
$$a_{i-1}v_{i-1}+b_{i}v_{i}+c_{i}v_{i+1}=d_{i},\ \ i=2,...,n-1.$$

We can then modify (3) by subtracting (1), like this
$$b_{1}\cdot (3)-a_{1}\cdot (1)$$

Which gives

$$(a_{1}v_{1}+b_{2}v_{2}+c_{2}v_{3})b_{1}-(b_{1}v_{1}+c_{1}v_{2})a_{1}=d_{2}b_{1}-d_{1}a_{1}$$
$$(b_{2}b_{1}-c_{1}a_{1})v_{2}+c_{2}b_{1}v_{3}=d_{2}b_{1}-d_{1}a_{1}.$$

Notice that $v_{1}$ has been eliminated (the first lower diagonal element has been eliminated).

This can be continued further - to eliminate all the $a_{i}$'s - and is what we call *forward substitution*.

Its apparent that the vector elements get more and more complicated. To solve this, we make modified vectors and find their elements recursively. Furthermore, we ensure that the $\tilde{b}_{i}$'s are 1 by normalizing with the modified diagonal elements.
$$\tilde{b}_{i}=1$$
$$\tilde{c}_{1}=\frac{c_{1}}{b_{1}}$$
$$\tilde{c}_{i}=\frac{c_{i}}{b_{i}-\tilde{c}_{i-1}a_{i-1}}$$
$$\tilde{d}_{1}=\frac{d_{1}}{b_{1}}$$
$$\tilde{d}_{i}=\frac{d_{i}-\tilde{d}_{i-1}a_{i-1}}{b_{i}-\tilde{c}_{i-1}a_{i-1}}$$

## Backward substitution
If we look at the coefficients defined above, we see that they give these equations for every $i$:
$$v_{n}=\tilde{d}_{n}$$
$$v_{i}=\tilde{d}_{i}-\tilde{c}_{i}v_{i+1}$$

This is the *backward substitution* necessary to find the solution.

***
<!-- Anna har skrevet dette, ville ikke fjerne det. -->

$a_i = c_i = -1/h^2 \textrm{and} \, b_i = 2$

Then we can write the linear set of equations as

$\mathbf{A}=\left[\begin{matrix}b_1 & c_1 & 0 & \cdots & \cdots & \cdots\\a_2 & b_2 & c_2 & 0 & &\\0 & a_3 &b_3 & c_3 & 0 &\\\vdots&\vdots & \ddots& \ddots&\ddots &\vdots\\0 & & & a_{n-1} & b_{n-1} & c_{n-1}\\0 & & &  & a_n & b_n\end{matrix}\right] \left[\begin{matrix}u_1\\u_2\\ \cdots\\\cdots\\\cdots\\u_n\end{matrix}\right] = \left[\begin{matrix}f_1\\f_2\\ \cdots\\\cdots\\\cdots\\f_n\end{matrix}\right]$


In the $4 \times 4$  case you will get

$\mathbf{A}=\left[\begin{matrix}b_1 & c_1 & 0 & 0 \\a_2 & b_2 & c_2 & 0 &\\0 & a_3 &b_3 & c_3 &\\ 0 & 0 & a_4 & b_4\end{matrix}\right]\left
[\begin{matrix}u_1\\u_2\\u_3\\u_4\end{matrix}\right] = \left[\begin{matrix}f_1\\f_2\\f_3\\f_4\end{matrix}\right]$

#######Forward substitution

If you apply Gaussian elimination by $\textrm{II}- \frac{a_2\cdot \textrm{I}}{b_1}$ you will get

$b_1u_1+c_1u_2 = f_1\\
a_2u_1-(b_1u_1\cdot \frac{a_2}{b_1}) +b_2u_2-(c_1u_2\cdot \frac{a_2}{b_1})+c_2u_3-0=f_2-\frac{a_2f_1}{b_1}\\
a_3u_2+b_3u_3+c_3u_4=f_3\\
a_4u_3+b_4u_4 = f_4$


Then we set

$\tilde b_2 = b_2-\frac{a_2c_1}{\tilde b_1} \,\, \textrm{and} \, \tilde f_2 = f_2 - \frac{a_2f_1}{\tilde b_1}. \textrm{For} \, i = 1 \,\textrm{and}\, i = n,\, \tilde b_i = b_i$.

which gives

$b_1u_1+c_1u_2 =  f_1\\
0 + \tilde b_2u_2+c_2u_3=\tilde f_2
\\a_3u_2+b_3u_3+c_3u_4=f_3\\a_4u_3+b_4u_4 = f_4$

If we apply Gaussian elimination on the rest of the set and assign new variables (tilde) to the "complicated " expressions, you will end up with the following set of linear equations

$\mathbf{A}=\left[\begin{matrix}b_1 & c_1 & 0 & 0 \\0 & \tilde b_2 & c_2 & 0 &\\0 & 0 & \tilde b_3 & c_3 &\\ 0 & 0 & 0 & \tilde b_4\end{matrix}\right]\left
[\begin{matrix}u_1\\u_2\\u_3\\u_4\end{matrix}\right] =
\left[\begin{matrix}f_1\\\tilde f_2\\\tilde f_3\\f_4\end{matrix}\right]$

From the elimination you can notice a pattern which can be generalized as

$\tilde b_i = b_i - \frac{a_i c_{i-1}}{\tilde b_i}\,\, \textrm{and}\,\,\tilde f_i = f_i - \frac{a_i f_{i-1}}{\tilde b_i}$


#######Backward substitution
$\\
\tilde b_1u_1+c_1u_2 =\tilde f_1\\
\tilde b_2u_2+c_2u_3=\tilde f_2\\
\tilde b_3u_3+c_3u_4=\tilde f_3\\
\tilde b_4u_4 = \tilde f_4\\
\\$

$\\
u_4 = \frac{\tilde f_4}{\tilde b_4}\\
u_3 = \frac{\tilde f_3 - c_3u_4}{\tilde b_3} \\
u_2 = \frac{\tilde f_2 - c_2u_3}{\tilde b_2}\\
u_1 = \frac{\tilde f_1 - c_1u_2}{\tilde b_1}\\
\\$

In general

$\\
u_{i-1} = \frac{\tilde f_{i-1} - c_{i-1}u_i}{\tilde b_{i-1}}\\
\\$


######Precise number of floating point operations

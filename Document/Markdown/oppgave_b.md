Project 1 b)
=============

We have a linear set of equations $\mathbf{Au = f}$
The matrix A can be rewritten as

$\mathbf{A}=\left[\begin{matrix}b_1 & c_1 & 0 & \cdots & \cdots & \cdots\\a_2 & b_2 & c_2 & 0 & &\\0 & a_3 &b_3 & c_3 & 0 &\\\vdots&\vdots & \ddots& \ddots&\ddots &\vdots\\0 & & & a_{n-1} & b_{n-1} & c_{n-1}\\0 & & &  & a_{n} & b_n\end{matrix}\right]$

where $a_, \, b \, \textrm{and} \, c$ are one-dimensional arrays with lenght $1:n$.  $a_i = c_i = -1/h^2 \textrm{and} \, b_i = 2$

Then we can write the linear set of equations as

$\mathbf{A}=\left[\begin{matrix}b_1 & c_1 & 0 & \cdots & \cdots & \cdots\\a_2 & b_2 & c_2 & 0 & &\\0 & a_3 &b_3 & c_3 & 0 &\\\vdots&\vdots & \ddots& \ddots&\ddots &\vdots\\0 & & & a_{n-1} & b_{n-1} & c_{n-1}\\0 & & &  & a_n & b_n\end{matrix}\right] \left[\begin{matrix}u_1\\u_2\\ \cdots\\\cdots\\\cdots\\u_n\end{matrix}\right] = \left[\begin{matrix}f_1\\f_2\\ \cdots\\\cdots\\\cdots\\f_n\end{matrix}\right]$


In the $4 \times 4$  case you will get

$\mathbf{A}=\left[\begin{matrix}b_1 & c_1 & 0 & 0 \\a_2 & b_2 & c_2 & 0 &\\0 & a_3 &b_3 & c_3 &\\ 0 & 0 & a_4 & b_4\end{matrix}\right]\left
[\begin{matrix}u_1\\u_2\\u_3\\u_4\end{matrix}\right] = \left[\begin{matrix}f_1\\f_2\\f_3\\f_4\end{matrix}\right]$

##Forward substitution

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


##Backward substitution
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

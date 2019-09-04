# Project 1 c)
##Modified algorithm

$\mathbf{A}=\left[\begin{matrix}2 & -1 & 0 & \cdots & \cdots & \cdots\\-1 & 2 & -1 & 0 & &\\0 & -1 & 2 & -1 & 0 &\\\vdots&\vdots & \ddots& \ddots&\ddots &\vdots\\0 & & & -1 & 2 & -1\\0 & & &  & -1 & 2\end{matrix}\right] \left[\begin{matrix}u_1\\u_2\\ \cdots\\\cdots\\\cdots\\u_n\end{matrix}\right] = \left[\begin{matrix}f_1\\f_2\\ \cdots\\\cdots\\\cdots\\f_n\end{matrix}\right]$

To generalize I will look at the $4 \times 4$  case

$\mathbf{A}=\left[\begin{matrix}2 & -1 & 0 & 0 \\-1 & 2 & -1 & 0 &\\0 & -1 & 2 & -1 &\\ 0 & 0 & -1 & 2 \end{matrix}\right]\left
[\begin{matrix}u_1\\u_2\\u_3\\u_4\end{matrix}\right] = \left[\begin{matrix}f_1\\f_2\\f_3\\f_4\end{matrix}\right]$


So

$\\
2u_1 - u_2 = f_1 \\
-u_1 + 2u_2 - u_3 = f_2\\
-u_2 + 2u_3 - u_4 = f_3\\
-u_3 + 2u_4 = f_4\\
\\$

Gaussian elimination:

$II + \frac{1}{2}\cdot I$



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

##FLOPS

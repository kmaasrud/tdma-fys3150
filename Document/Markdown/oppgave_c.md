# Project 1 c)
## Modified algorithm

$\mathbf{A}=\left[\begin{matrix}d & e & 0 & \cdots & \cdots & \cdots\\e & d & e & 0 & &\\0 & e & d & e & 0 &\\\vdots&\vdots & \ddots& \ddots&\ddots &\vdots\\0 & & & e & d & e\\0 & & &  & e & d\end{matrix}\right] \left[\begin{matrix}u_1\\u_2\\ \cdots\\\cdots\\\cdots\\u_n\end{matrix}\right] = \left[\begin{matrix}f_1\\f_2\\ \cdots\\\cdots\\\cdots\\f_n\end{matrix}\right]$

To generalize I will look at the $4 \times 4$  case

$\mathbf{A}=\left[\begin{matrix}d & e & 0 & 0 \\e & d & e & 0 &\\0 & e &d & e &\\ 0 & 0 & e & d\end{matrix}\right]\left
[\begin{matrix}u_1\\u_2\\u_3\\u_4\end{matrix}\right] = \left[\begin{matrix}f_1\\f_2\\f_3\\f_4\end{matrix}\right]$


So

$\\
du_1 + eu_2 = f_1 \\
eu_1 + du_2 + eu_3 = f_2\\
eu_2 + du_3 + eu_4 = f_3\\
eu_3 + du_4 = f_4\\
\\$

Gaussian elimination:

$II - \frac{e}{d}\cdot I$


$\\
du_1 + eu_2 = f_1 \\
u_2(\frac{d^2 - e ^2}{d} ) + eu_3 = f_2 - f_1\frac{e}{d}\\
eu_1 + du_2 + eu_3 = f_3\\
eu_3 + du_4 = f_4\\
\\$

set

$\tilde d = \frac{d^2 - e ^2}{d}\, \textrm{and}\,\tilde f_2 =f_2-f_2\frac{e}{d}$

...\
Generalized:





## FLOPS

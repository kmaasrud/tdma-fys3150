% Project 1 FYS3150
% 9 September 2019
% Authors

# Abstract {#abstract .unnumbered}

Introduction {#introduction .unnumbered}
============

Theory and technicalites {#theory-and-technicalites .unnumbered}
========================

Conclusion and perspectives {#conclusion-and-perspectives .unnumbered}
===========================

Project 1 a) {#project-1-a .unnumbered}
============

For $i = 0$ and $i = n$ the boundary conditions gives us
$v(0) = v(1) = 0$.\
For $i = 1$

$$-\frac{v_2+v_0-2v_1}{h^2} = f_1$$

\
For $i = 2$\

$$-\frac{v_3+v_1-2v_2}{h^2}{} = f_2$$

\
\
For $i = n-1$\
\

$$-\frac{v_n+v_{n-2}-2v_{n-1}}{h^2}{} = f_{n-1}$$

\
If you multiply both sides by $h^2$

$$-{v_2+v_0-2v_1} = h^2\cdot{f_1}$$

\

$$-{v_3+v_1-2v_2} = {h^2}\cdot{f_2}$$

\

$$-v_n+v_{n-2}-2v_{n-1} = {h^2}\cdot{f_{n-1}}$$

\
Which you can rewrite as a linear set of equations where\

$$A=\left[\begin{matrix}2 & -1 & 0 & & & 0\\-1 & 2 & -1 & 0 & &\\0 & -1 &2 & -1 & 0 &\\\vdots&\vdots & \ddots& \ddots&\ddots &\vdots\\0 & & & -1 & 2 & -1\\0 & & & 0 & -1 & 2\end{matrix}\right]$$

$\hat{v}=\left[\begin{matrix}v_{1}\\v_{2}\\v_{3}\\ \vdots \\ v_{n-1}\end{matrix}\right]$


and $\tilde{b_i}=\left[\begin{matrix}\tilde{b}_{1}\\\tilde{b}_{2}\\\tilde{b}_{3}\\ \vdots \\ \tilde{b}_{n-1}\end{matrix}\right]$

Where $\tilde{b_i} = h^2 \cdot f_i$

Project 1 b) {#project-1-b .unnumbered}
============

Appendix {#appendix .unnumbered}
========

Bibliography {#bibliography .unnumbered}
============

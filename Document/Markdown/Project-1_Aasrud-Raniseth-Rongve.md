---
title: Project 1
author:
  - Anna Stray Rongve
  - Amund Midtgard Raniseth
  - Knut Magnus Aasrud
date: Mandag 9 September 2019
header-includes: |
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \fancyhf{}
  \rhead{Project 1}
  \lhead{\leftmark}
  \rfoot{\thepage}
---

# Abstract
Summary of project.\
The abstract gives the reader a quick overview of what has been done and the most important results. Try to be to the point and state your main findings.


In project 1 a) we solved a one-dimensional Poisson equation with Dirichlet boundary condition by rewriting it as a set of linear equations, **Av=d**.

In Project 1 b) we solved the linear set of equations **Av=d**, where **A** is a tridiagonal matrix, which we expressed as three vectors, $a, b and c$
To solve our equations  we used Gaussian elimination as well as forward and backward substitution.

In Project 1 c) we used our general algorithm to make a special, where the matrix elements along the diagonal where identical

# Introduction

# Theory and technicalites

# Conclusion and perspectives

# Project 1 a)
We have the discretized version of $u$, $v$, with the boundary conditions $v_{0}=v_{n}=0$:

For $i = 1$

$$-\frac{v_2+v_0-2v_1}{h^2} = f_1$$

For $i = 2$

$$-\frac{v_3+v_1-2v_2}{h^2}{} = f_2$$

For $i = n-1$

$$-\frac{v_n+v_{n-2}-2v_{n-1}}{h^2}{} = f_{n-1}$$

Multiplying both sides by $h^2$ gives

$$-v_2+2v_1-v_0 = h^2\cdot{f_1}$$

$$-v_3+2v_2-v_1 = {h^2}\cdot{f_2}$$

$$-v_n+2v_{n-1}-v_{n-2} = {h^2}\cdot{f_{n-1}}$$

Which you can rewrite as a linear set of equations $\mathbf{A}\mathbf{v}=\mathbf{d}$ where

$$\mathbf{A}=\left[\begin{matrix}2 & -1 & 0 & \dots & \dots & 0\\-1 & 2 & -1 & 0 & \ddots & \vdots \\0 & -1 &2 & -1 & 0 & \vdots \\ \vdots & \vdots & \ddots& \ddots & \ddots & \vdots\\0 & \dots & \dots & -1 & 2 & -1\\0 & \dots & \dots & 0 & -1 & 2\end{matrix}\right]$$

$$\mathbf{v}=\left[\begin{matrix}v_{1}\\v_{2}\\v_{3}\\ \vdots \\ v_{n-1}\end{matrix}\right]$$

and

$$\mathbf{d}=\left[\begin{matrix}d_{1}\\ d_{2}\\\ d_{3}\\ \vdots \\ d_{n-1}\end{matrix}\right]$$

<!-- Kaller den d fordi det er litt lettere å holde følge down the road -->

with $d_{i} = h^2 \cdot f_i$

# Project 1 b)
We have a linear set of equations $\mathbf{Av = d}$ we want to solve, where $\mathbf{A}$ is tridiagonal.

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

This *backwards substitution* gives us the solution $\mathbf{v}$.

# Appendix

# Bibliography

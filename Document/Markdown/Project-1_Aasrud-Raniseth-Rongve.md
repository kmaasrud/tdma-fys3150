---
title: Project 1
author:
  - Anna Stray Rongve
  - Amund Midtgard Raniseth
  - Knut Magnus Aasrud
date: Mandag 9 September 2019
bibliography: references.bib
link-citations: true
header-includes: |
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \fancyhf{}
  \rhead{Project 1}
  \lhead{\leftmark}
  \rfoot{\thepage}
---
The programs referenced in this article are in a repository linked in the appendix.

# Abstract
In this project we want to solve a one-dimensional Poisson equation with Dirichlet boundary conditions numerically in order to study the importance of stepsize and floating points operations, FLOPs.

We approached this problem by rewriting the equation as a set of linear equations  **Av=d** under the following assumptions:

+ A is $n\times n$ nonsingular
+ $\mathbf{Ax = b }$ has a unique solution **x** for every **b** in $\mathbf R^n$

Then we solved the equations utilizing the Thomas algorithm, a special case of Gaussian elimination that has two steps - the forward- and backward substitution. Thereafter we specialized our algorithm by choosing a specific matrix $\mathbf A$ in order to reduce the number of FLOPs and compared its CPU time with our general algorithm.

To measure deviation between the analytical($u(x)$) and numerical solution , the relative error was calculated by
$$\epsilon_{i}=\log_{10}\left(\left|\frac{v_{i}-u_{i}}{u_{i}}\right|\right)$$

The stepsize in our algorithm varies between 

By studying the number of floating point operations, FLOPs, we could predict which method would be the most efficient(in measured CPU time). However we realised quickly that computer-factors would play a big roll when increasing the size of the matrix(n).


# Introduction
The purpose of this project is to implement a numerically effective solution of the one-dimensional Poisson equation with Dirichlet boundary conditions
$$-u''(x)=f(x),\ \ \ u(0)=u(1)=0$$

and to implement this in a programming language of choice (Python, in our case). This will be done using two different approaches - the general Thomas algorithm and a specialized Thomas algorithm - the speed of which is compared.

Crucially, the step size affects the results of these methods, and this is also put to the test. The methods are put up against the analytical solution and for one of the algorithms, the relative error is calculated for different step sizes. Lastly, our method is compared to one using LU-decomposition.

# Theory and technicalites
The Poisson equation we are going to solve reads as follows:
$$-u''(x)=100e^{-10x},$$

with the analytical solution:
$$u(x)=1-(1-e^{-10})x-e^{-10x}.$$

## Project 1 a)
We start by discretizing $u(x)$ to $v_i$, with the boundary conditions $v_{0}=v_{n}=0$:

For $i = 1$,

$$-\frac{v_2+v_0-2v_1}{h^2} = f_1.$$

For $i = 2$,

$$-\frac{v_3+v_1-2v_2}{h^2}{} = f_2.$$

For $i = n-1$,

$$-\frac{v_n+v_{n-2}-2v_{n-1}}{h^2}{} = f_{n-1}.$$

Multiplying both sides by $h^2$ gives

$$-v_2+2v_1-v_0 = h^2\cdot{f_1},$$

$$-v_3+2v_2-v_1 = {h^2}\cdot{f_2},$$

$$-v_n+2v_{n-1}-v_{n-2} = {h^2}\cdot{f_{n-1}}.$$

Which you can rewrite as a linear set of equations $\mathbf{A}\mathbf{v}=\mathbf{d}$ where

$$\mathbf{A}=\left[\begin{matrix}2 & -1 & 0 & \dots & \dots & 0\\-1 & 2 & -1 & 0 & \ddots & \vdots \\0 & -1 &2 & -1 & 0 & \vdots \\ \vdots & \vdots & \ddots& \ddots & \ddots & \vdots\\0 & \dots & \dots & -1 & 2 & -1\\0 & \dots & \dots & 0 & -1 & 2\end{matrix}\right],$$

$$\mathbf{v}=\left[\begin{matrix}v_{1}\\v_{2}\\v_{3}\\ \vdots \\ v_{n-1}\end{matrix}\right],$$

and

$$\mathbf{d}=\left[\begin{matrix}d_{1}\\ d_{2}\\\ d_{3}\\ \vdots \\ d_{n-1}\end{matrix}\right],$$

with $d_{i} = h^2 \cdot f_i$.

We see that $\mathbf{A}$ is a tridiagonal matrix which we can employ the Thomas algorithm [@Hjorth-Jensen2018] on. This is done below.

## Project 1 b)
### General algorithm

We have a linear set of equations $\mathbf{Av = d}$

In the general case, we can express any tridiagonal matrix

$$\mathbf{A}=\left[\begin{matrix}b_1 & c_1 & 0 & \cdots & \cdots & 0 \\a_{1} & b_2 & c_2 & \ddots & \ddots &\vdots \\0 & a_{2} &b_3 & \ddots & \ddots &\vdots \\ \vdots& \ddots & \ddots& \ddots& c_{n-2} & 0 \\0 & \dots & 0 & a_{n-2} & b_{n-1} & c_{n-1}\\0 & \dots & \dots & 0 & a_{n-1} & b_n\end{matrix}\right]$$

just by the three vectors $a_, \, b \ \text{and} \, c$, where $b$ has length $n$, and $a$ and $c$ have length $n-1$.

### Forward substitution
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

Notice that $v_{1}$ has been eliminated ($\Leftrightarrow$ the first lower diagonal element has been eliminated).

This can be continued further - to eliminate all the $a_{i}$'s - and is what we call *forward substitution*.

Its apparent that the vector elements get more and more complicated. To solve this, we make modified vectors and find their elements recursively. Furthermore, we ensure that the $\tilde{b}_{i}$'s are 1 by normalizing with the modified diagonal elements.
$$\tilde{b}_{i}=1$$
$$\tilde{c}_{1}=\frac{c_{1}}{b_{1}}$$
$$\tilde{c}_{i}=\frac{c_{i}}{b_{i}-\tilde{c}_{i-1}a_{i-1}}$$
$$\tilde{d}_{1}=\frac{d_{1}}{b_{1}}$$
$$\tilde{d}_{i}=\frac{d_{i}-\tilde{d}_{i-1}a_{i-1}}{b_{i}-\tilde{c}_{i-1}a_{i-1}}$$

### Backward substitution
If we look at the coefficients defined above, we see that they give these equations for every $i$:
$$v_{n}=\tilde{d}_{n}$$
$$v_{i}=\tilde{d}_{i}-\tilde{c}_{i}v_{i+1}$$

This is the *backward substitution* necessary to find the solution.

The whole algorithm runs using $O(n)$ FLOPs, specifically $9n$. This is a major improvement on Gaussian elimination, which requires $O(n^{3})$ FLOPs [@Hjorth-Jensen2018].

## Project 1 c)
### Modified algorithm

In the case of the Poisson equation we can use our general algorithm for a tridiagonal matrix, derived above, and simply replace our variables $a_i, b_i \, \textrm{and}\, c_i \,\textrm{with respectively} -1, 2 \,\,\textrm{and} -1$.

$$\\
\mathbf{A}=\left[\begin{matrix}2 & -1 & 0 & \cdots & \cdots & \cdots\\-1 & 2 & -1 & 0 & &\\0 & -1 & 2 & -1 & 0 &\\\vdots&\vdots & \ddots& \ddots&\ddots &\vdots\\0 & & & -1 & 2 & -1\\0 & & &  & -1 & 2\end{matrix}\right] \left[\begin{matrix}v_1\\v_2\\ \cdots\\\cdots\\\cdots\\v_n\end{matrix}\right] = \left[\begin{matrix}d_1\\d_2\\ \cdots\\\cdots\\\cdots\\d_n\end{matrix}\right]
\\$$

This translates into a simpler algorithm, were we're able to cut down the number of FLOPs.

### Forward substitution special case
Inserting the values of $a_{i}$, $b_{i}$ and $c_{i}$ into the general algorith, we get this:
$$\\
\tilde{b}_{i}=1\\
\tilde{c}_{1}=-\frac{1}{2}\\
\tilde c_i = -\frac{1}{2-(-1)a_{i-1}} = -\frac{1}{2 + \tilde c_{i-1}}\\
\tilde d_1 = \frac{d_1}{2}\\
\tilde d_i = \frac{d_i + \tilde d_{i-1}}{2+ \tilde c_{i-1}} \\
$$


### Backward substitution special case
The backward substitution will not be any different from the one in Project 1 b)

$$\\
v_n = \tilde d_i\\
v_{i}=\tilde{d}_{i}-\tilde{c}_{i}v_{i+1}
\\$$

This also runs using O(n) FLOPs, but by simplifying our algorithm the number of FLOPs decreases from **9n** to **6n**.

## Project 1 d)
### Relative error
The special Thomas algorithm is compared against the analytical solution and the relative error is calculated. This is done using this formula:
$$\epsilon_{i}=\log_{10}\left(\left|\frac{v_{i}-u_{i}}{u_{i}}\right|\right)$$

where $v$ is the numerical solution and $u$ is the analytical solution. For each step size, the maximum value of the $\epsilon_{i}$'s is found and stored.

## Project 1 e)
To compare the TDMA function with an LU decomposition we first put both functions in one code to be ran at the same time. For the LU decomposition we decided to use _lu_factor_ and _lu_decompose_ from the _scipy.linalg_ library. The execution time was counted with _clock()_ from the _time_ library in Python. The counting  started at the start of the recursive algorithm, and were stopped immediately after.

# Results
## Project 1 b)
The program `general_tdma_function.py` is based on the general Thomas algorithm - solving our sample Poisson equation and plotting it at different step sizes. It gives this result:

![**Figure 1**: General TDMA solution for $n=10,100,1000$, compared to the analytical solution.](..\Images\general_tdma_plot.png)

Its quite clear that a smaller step size correlates to higher accuracy for these selections of step sizes.

## Project 1 c)
The program `special_tdma_function.py` is based on our specialized Thomas algorithm. In `General-vs-special-tdma-test.py`, we compare the time spent over the general and special algorithm and print them to the console at different step sizes ($n$-values). The results are:

    General TDMA, time spent on n = 100 is 0.000195 seconds
    Special TDMA, time spent on n = 100 is 0.0002599 seconds


    General TDMA, time spent on n = 1000 is 0.0046473 seconds
    Special TDMA, time spent on n = 1000 is 0.003015 seconds


    General TDMA, time spent on n = 10000 is 0.0573864 seconds
    Special TDMA, time spent on n = 10000 is 0.0366101 seconds


    General TDMA, time spent on n = 100000 is 0.307781 seconds
    Special TDMA, time spent on n = 100000 is 0.216879 seconds

    General TDMA, time spent on n = 1e+06 is 2.97735 seconds
    Special TDMA, time spent on n = 1e+06 is 2.56285 seconds

Its not fully apparent at small matrix sizes, but once they get big, the reduction in FLOPs makes a difference. This is because the overhead in the _scipy.linalg.lu_solve_ function is relatively big for small $n$'s.

## Project 1 d)
The program (`relative_error.py`) gives these results:

![**Figure 2**: log10($\epsilon$) vs log10(h)](..\Images\relative_error.png)

| Relative error  | $log_{10}(\text{Step size})$ |
|-----------------|----------------|
| -1.17969778218 | -1.04139268516 |
| -1.97626186757 | -1.44715803134 |
| -2.8062343362 | -1.86332286012 |
| -3.65484240031 | -2.28780172993 |
| -4.50952402333 | -2.71516735785 |
| -5.36521193786 | -3.14301480025 |
| -6.22236646348 | -3.57159238336 |
| -7.07928513404 | -4.00004342728 |
| -7.93346055078 | -4.42858829767 |
| -8.65847844871 | -4.85715150269 |
| -8.48011516818 | -5.28571704599 |
| -6.41732032512 | -5.71428616043 |
| -6.00098101822 | -6.14285730089 |
| -5.91413531823 | -6.57142872052 |
| -5.52523001828 | -7.00000004343 |

We see that when the $\log_{10}$ of the step size goes below -5, we are losing precision fast.


## Project 1 e)
The code is available in _Project-1/Code/Python/tdma_compare_lu.py_ in our github repository.

|          |      TDMA      |LU decomposition |
|----------|-------------:|------:|
| $n=  10$  |  $0.000045s$ | $0.000151s$ |
| $n= 100$  |    $0.002442s$   |  $0.002045s$ |
| $n= 1000$ | $0.026847s$ |    $0.131573s$|

The table is a bit confusing since for $n=100$ the LU decomposition is faster than the TDMA method, but the general trend is that the TDMA method is wildly superior.

If the LU decomposition is run with a $10^5\times 10^5$ matrix, we quickly run out of RAM. This is because every matrix element takes up 8Bytes, which in our case adds up to 80Gigabytes.

# Conclusion and perspectives


# Appendix
[Source Code](https://github.com/kmaasrud/Project-1/tree/master/Code/Python)

# References
::: {refs}

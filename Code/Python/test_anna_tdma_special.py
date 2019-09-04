import numpy as np



d = 2
e = -1


def test_tdma(d,e,f,g,h):

    n = len(b)

    f_list = np.zeros(n)
    u_list = np.zeros(n)

    for i in range (1,n-1):
        u_list[i+1] = u_list[i] + u_list[i]/i #2 * n flops
        f_list[i+1] = f_list[i-1] + f[1]/i #2*n  flops

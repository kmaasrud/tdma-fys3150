import numpy as np



d = 2
e = -1


def test_tdma(d,e,f,g,h):

    n = len(b)

    f_list = np.zeros(n)
    x_list = np.zeros(n)

    for i in range (1,n-1):
        x_list[i] = x[i]*(i+1)/i
        f_list[i] = f[i] + f[i-1]* (i-1)/i #denne er feil

        '''
        kan forkortes til
        x_list[i] = x[i] + x[i]/i
        f_list[i] = f[i] + (i-1)/i  #denne er feil
        '''
        

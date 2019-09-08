import numpy as np
import matplotlib.pyplot as plt

def fbsub(a,b,c,v,g):
    #a,b og c er diagonalene. x er input og btilde er output
    """
    matrisen ser da slik ut med n=3:
    [ b1  c1  0   0  ]   [v1]   [g1]
    [ a1  b2  c2  0  ] * [v2] = [g2]
    [ 0   a2  b3  c3 ]   [v3]   [g3]
    """
    n = len(v)

    #Forward subst
    d = np.zeros(n) #nytt diagonalelement
    b_tilde = np.zeros(n) #nytt svar for g_i
    b_tilde[0] = g[0]
    b_tilde[1] = g[1]
    d[0] = b[0]
    d[1] = b[1]
    v[0] = 0
    v[n-1] = 0

    for i in range(1,n-1):
        d[i] = b[i] - (c[i-1]*a[i-1])/d[i-1]
        b_tilde[i] = g[i]-b_tilde[i-1]*a[i-1]/d[i-1]
        print("d",d[i])
    #Backward subst
    ny_b_tilde = np.zeros(n) # nytt svar etter back subst
    for i in reversed(range(1,n-1)):
        #ny_b_tilde[i] = b_tilde[i]-b_tilde[i+1]*c[i]/d[i+1]
        ny_b_tilde[i] = (b_tilde[i]-c[i]*ny_b_tilde[i+1])/d[i]
        print("nybtilde",ny_b_tilde[i])
    """
    Nå har vi diagonalene, og svarene i følgende format:
    [ d1  0   0   0  ]   [v1]   [ny_b_tilde1]
    [ 0   d2  0   0  ] * [v2] = [ny_b_tilde2]
    [ 0   0   d3  0  ]   [v3]   [ny_b_tilde3]
    Så det som står igjen er å gjøre d1*v1=ny_b_tilde1 om til v1=ny_b_tilde1/d1
    """

    for i in range(1,n-1):
        v[i] = ny_b_tilde[i]/d[i]
        print(v[i])
    return v

def func(x):
    return 100*np.exp(-10*x)

n = [10,100,1000]
for n in n:

    x = np.linspace(0,1,n)
    a = np.zeros(n); a[:] = -1
    b = np.zeros(n); b[:] = 2
    c = np.zeros(n); c[:] = -1
    v = np.zeros(n)
    h = 1/(n+1)  #stepsize
    svar = fbsub(a,b,c,v,h**2*func(x))
#print(a,b,c,v,x)

    plt.plot(x,svar, label=n)
    #plt.plot(x,func(x),color='g')
plt.plot(x,1-(1-np.exp(-10))*x-np.exp(-10*x), label="Analytisk losning")
plt.legend()
plt.show()

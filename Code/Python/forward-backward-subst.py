import numpy as np

def fbsub(a,b,c,x,g):
    #a,b og c er diagonalene. x er input og btilde er output
    """
    matrisen ser da slik ut med n=3:
    [ b1  c1  0   0  ]   [x1]   [g1]
    [ a1  b2  c2  0  ] * [x2] = [g2]
    [ 0   a2  b3  c3 ]   [x3]   [g3]
    """
    n = len(x)

    #Forward subst
    d = np.zeros(n) #nytt diagonalelement
    b_tilde = np.zeros(n) #nytt svar for g_i

    for i in range(1,n-1):
        d[i] = b[i] - (c[i-1]*a[i-1])/d[i-1]
        b_tilde[i] = g[i]-b_tilde[i-1]*a[i-1]/d[i-1]

    #Backward subst
    ny_b_tilde = np.zeros(n) # nytt svar etter back subst
    for i in reverse(range(1,n-1)):
        ny_b_tilde[i] = b_tilde[i]-b_tilde[i+1]*c[i]/d[i+1]

import numpy as np

def tdma(a,b,c,d):
    n=len(b)

    c_tilde=np.zeros(n)
    d_tilde=np.zeros(n)

    c_tilde[0]=c[0]/b[0]
    d_tilde[0]=d[0]/b[0]

    for i in range(1,n-1):
        m=1.0/(b[i]-a[i]*c_tilde[i-1])
        c_tilde[i]=c[i]*m
        d_tilde[i]=(d[i]-a[i]*d_tilde[i-1])*m

    for i in reversed(range(1,n-1)):
        x[i]=d_tilde[i]-c_tilde[i]+d[i+1]

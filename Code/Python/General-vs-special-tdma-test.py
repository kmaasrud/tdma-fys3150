import numpy as np
import matplotlib.pyplot as plt
import time


def tdma(a,b,c,d,u):
    n=len(b)    #the final solution (u) is of size n+2 because of the boundary conditions
    start_time = time.time()
    c_tilde=np.zeros(n)
    d_tilde=np.zeros(n)

    c_tilde[0]=c[0]/b[0]
    d_tilde[0]=d[0]/b[0]

    for i in range(1,n-1):  #FORWARD substitution
        m=1.0/(b[i]-a[i-1]*c_tilde[i-1])  #saves 1 division, 1 multiplication and 1 subtraction
        c_tilde[i]=c[i]*m
        d_tilde[i]=(d[i]-a[i-1]*d_tilde[i-1])*m

    v=np.zeros(n)   #this represents the vector v, the solution of the linear set of equations Av=d
    v[n-1]=d_tilde[n-1]

    for i in reversed(range(1,n-1)):    #BACKWARD substitution
        v[i]=d_tilde[i]-c_tilde[i]*v[i+1]
    print("General TDMA, time spent on n = %g is %g seconds" % (n,time.time()-start_time))
    u[1:n+1]=v  #inserting the solution of the linear eq. into the final solution, with boundary conditions

def special_tdma(a,b,c,d,u):
    n=len(b)    #the final solution (u) is of size n+2 because of the boundary conditions
    start_time = time.time()
    c_tilde=np.zeros(n)
    d_tilde=np.zeros(n)

    c_tilde[0]=c[0]/b[0]
    d_tilde[0]=d[0]/b[0]

    for i in range(1,n-1):  #FORWARD substitution
        m=1.0/(2+c_tilde[i-1])  #saves 1 division, 1 multiplication and 1 subtraction
        c_tilde[i]=-m
        d_tilde[i]=(d[i]+d_tilde[i-1])*m

    v=np.zeros(n)   #this represents the vector v, the solution of the linear set of equations Av=d
    v[n-1]=d_tilde[n-1]

    for i in reversed(range(1,n-1)):    #BACKWARD substitution
        v[i]=d_tilde[i]-c_tilde[i]*v[i+1]
    print("Special TDMA, time spent on n= %g is %g seconds" % (n,time.time()-start_time))
    u[1:n+1]=v  #inserting the solution of the linear eq. into the final solution, with boundary conditions

n=[1000,10000,100000]

for i in n:     #solving for different n's
    h=1/(i+1)
    a=np.zeros(i-1)
    a[:]=-1
    b=np.zeros(i)
    b[:]=2
    c=np.zeros(i-1)
    c[:]=-1
    d=np.linspace(0,1,i)
    d=h**2*100*np.exp(-10*d)
    u=np.zeros(i+2)
    x=np.linspace(0,1,i+2)
    u[1]=55

    tdma(a,b,c,d,u)
    plt.plot(x,u,label=r'$n=$ '+str(i))
    special_tdma(a,b,c,d,u)
    plt.plot(x,u,label=r'$n=$ '+str(i))


actual_u=1-(1-np.exp(-10))*x-np.exp(-10*x)  #the analytically found solution
plt.plot(x,actual_u,label="Analytical")

plt.legend()
plt.show()

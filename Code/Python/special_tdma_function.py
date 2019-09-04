import numpy as np
import matplotlib.pyplot as plt
import time

def poisson_tdma(d,u):
    n=len(d)    #the final solution (u) is of size n+2 because of the boundary conditions

    c_tilde=np.zeros(n)
    d_tilde=np.zeros(n)
    v=np.zeros(n)   #this represents the vector v, the solution of the linear set of equations Av=d

    start_time = time.clock()
    c_tilde[0]=-0.5
    d_tilde[0]=0.5*d[0]

    for i in range(1,n-1):  #FORWARD substitution
        m=1.0/(2+c_tilde[i-1])
        c_tilde[i]=-m
        d_tilde[i]=(d[i]+d_tilde[i-1])*m

    v[n-1]=d_tilde[n-1]

    for i in reversed(range(1,n-1)):    #BACKWARD substitution
        v[i]=d_tilde[i]-c_tilde[i]*v[i+1]

    time_spent=time.clock()-start_time

    print("Special TDMA, time spent on n = %g is %g seconds" % (n,time_spent))

    u[1:n+1]=v  #inserting the solution of the linear eq. into the final solution, with boundary conditions

n=[10,100,1000]

for i in n:     #solving for different n's
    h=1/(i+1)
    d=np.linspace(0,1,i)
    d=h**2*100*np.exp(-10*d)
    u=np.zeros(i+2)
    x=np.linspace(0,1,i+2)
    u[1]=55

    poisson_tdma(d,u)

    plt.plot(x,u,label=r'$n=$ '+str(i))

actual_u=1-(1-np.exp(-10))*x-np.exp(-10*x)  #the analytically found solution
plt.plot(x,actual_u,label="Analytical")

plt.legend()

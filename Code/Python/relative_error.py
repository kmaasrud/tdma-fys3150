import numpy as np
import matplotlib.pyplot as plt

def poisson_tdma(d,u):
    n=len(d)    #the final solution (u) is of size n+2 because of the boundary conditions

    c_tilde=np.zeros(n)
    d_tilde=np.zeros(n)
    v=np.zeros(n)   #this represents the vector v, the solution of the linear set of equations Av=d

    c_tilde[0]=-0.5
    d_tilde[0]=0.5*d[0]

    for i in range(1,n-1):  #FORWARD substitution
        m=1.0/(2+c_tilde[i-1])
        c_tilde[i]=-m
        d_tilde[i]=(d[i]+d_tilde[i-1])*m

    v[n-1]=d_tilde[n-1]

    for i in reversed(range(1,n-1)):    #BACKWARD substitution
        v[i]=d_tilde[i]-c_tilde[i]*v[i+1]

    u[1:n+1]=v  #inserting the solution of the linear eq. into the final solution, with boundary conditions

n=np.array([int(1e2),int(1e3),int(1e4),int(1e5),int(1e6),int(1e7)])
h=1/(n+1)
epsilon=np.zeros(len(n))

for i in range(len(n)):     #solving for different n's
    d=np.linspace(0,1,n[i])
    d=h[i]**2*100*np.exp(-10*d)
    u=np.zeros(n[i]+2)
    x=np.linspace(0,1,n[i]+2)
    u[1]=55

    x=np.linspace(0,1,n[i]+2)
    actual_u=1-(1-np.exp(-10))*x-np.exp(-10*x)  #the analytically found solution

    poisson_tdma(d,u)

    epsilon[i]=np.amax(np.log10(np.absolute((u[2:n[i]-1]-actual_u[2:n[i]-1])/actual_u[2:n[i]-1])))

plt.plot(np.log10(h),epsilon)
plt.show()

import numpy as np
import scipy.linalg as spla
import matplotlib.pyplot as plt
import time

def tdma(a,b,c,d,u):
    n=len(b)    #the final solution (u) is of size n+2 because of the boundary conditions

    c_tilde=np.zeros(n)
    d_tilde=np.zeros(n)
    v=np.zeros(n)   #this represents the vector v, the solution of the linear set of equations Av=d

    c_tilde[0]=c[0]/b[0]
    d_tilde[0]=d[0]/b[0]

    start_time = time.clock()
    for i in range(1,n-1):  #FORWARD substitution
        m=1.0/(b[i]-a[i-1]*c_tilde[i-1])  #saves 1 division, 1 multiplication and 1 subtraction
        c_tilde[i]=c[i]*m
        d_tilde[i]=(d[i]-a[i-1]*d_tilde[i-1])*m

    v[n-1]=d_tilde[n-1]

    for i in reversed(range(1,n-1)):    #BACKWARD substitution
        v[i]=d_tilde[i]-c_tilde[i]*v[i+1]

    time_spent=time.clock()-start_time

    u[1:n+1]=v  #inserting the solution of the linear eq. into the final solution, with boundary conditions

    print("General TDMA, time spent on n = %g is %g seconds" % (len(u),time_spent))
    print("-")
    plt.plot(x,u,label="TDMA, n = %i" %len(u))

def LU(a,b,c,d,u):
    #Setting up tridiagonal matrix A
    def tridiag(a,b,c,k1=-1, k2=0, k3=1):
        return np.diag(a,k1) + np.diag(b,k2) + np.diag(c,k3)
    A = tridiag(a,b,c)

    u = np.zeros(len(d)+2) #Defining U-array
    #Solving the LU decomposition of A
    start_time = time.clock()
    u[1:-1] = spla.lu_solve(spla.lu_factor(A),d,trans=0)
    time_spent=time.clock()-start_time

    plt.plot(x,u,label="LU,      n = %i" %len(u))
    n = len(u)
    print("LU-decomposition, time spent on n = %g is %g seconds" % (n,time_spent))



<<<<<<< HEAD
n=[10,100,1000]
=======
n=[100,1000,int(1e4)]
>>>>>>> 5bc8ed0124e84f36c121e78637d9ed2e707109c8

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

    LU(a,b,c,d,u)
    tdma(a,b,c,d,u)
    #plt.plot(x,u,label=r'$n=$ '+str(i))

actual_u=1-(1-np.exp(-10))*x-np.exp(-10*x)  #the analytically found solution
plt.plot(x,actual_u,label="Analytical")
plt.legend()
plt.show()

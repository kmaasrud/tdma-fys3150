import numpy as np
import matplotlib.pyplot as plt

def poisson_tdma(d,v):
    n=len(d)    #the final solution (u) is of size n+2 because of the boundary conditions

    c_tilde=np.zeros(n)
    d_tilde=np.zeros(n)
    v_temp=np.zeros(n)   #this represents the vector v, the solution of the linear set of equations Av=d

    c_tilde[0]=-0.5
    d_tilde[0]=0.5*d[0]

    for i in range(n):  #FORWARD substitution
        m=1.0/(2+c_tilde[i-1])
        c_tilde[i]=-m
        d_tilde[i]=(d[i]+d_tilde[i-1])*m

    v_temp[n-1]=d_tilde[n-1]

    for i in reversed(range(1,n-1)):    #BACKWARD substitution
        v_temp[i]=d_tilde[i]-c_tilde[i]*v_temp[i+1]

    v[1:n+1]=v_temp  #inserting the solution of the linear eq. into the final solution, with boundary conditions

n = np.rint(np.logspace(1,7,15))
#n = np.array([1e1,1e2,1e3,1e4,1e5,1e6])
epsilon=np.zeros(len(n))
h=1/(n+1)

print(n)
for i in range(len(n)):     #solving for different n's
    x=np.linspace(0,1,n[i]+2)
    d=h[i]**2*100*np.exp(-10*x[1:-1])
    v=np.zeros(int(n[i]+2))
    v[1]=55

    actual_v=1-(1-np.exp(-10))*x-np.exp(-10*x)  #the analytically found solution

    poisson_tdma(d,v)
    epsilon[i]=np.log10(np.max(np.absolute((v[2:-1]-actual_v[2:-1])/actual_v[2:-1])))


print("| Relative error  | log(Step size) |")
print("|-----------------|----------------|")
for i in range(len(epsilon)):
    print("| "+str(epsilon[i])+" | "+str(np.log10(h[i]))+" |")

plt.title("Log10 of the error againts log10 of the step size")
plt.xlabel("log10(h)")
plt.ylabel("log10($\epsilon_i$)")
plt.plot(np.log10(h), epsilon)
plt.savefig("relative_error.png")

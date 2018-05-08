import numpy as np
import matplotlib.pyplot as plt

G=6.67408e-11
M=1.989e30

rm=np.sqrt(2.133679072387218E-01**2+3.727310311768299E-01**2+5.058864779204983E-02**2)*1.496e+11
vm=np.sqrt(1.892057222101034E-02**2+1.513838055059527E-02**2 +4.995475648824679E-04**2)*1.7315e6

alpha=np.linspace(0,4,100)

beta=vm**2/(rm**(1-alpha))
print beta

betabarra=G*M

proba=np.exp(-1.0*(betabarra-beta)**2/(2*np.var(beta)))
print proba

probaalpha=1/4

probafinal=probaalpha*proba

plt.plot(beta,proba)
plt.show()

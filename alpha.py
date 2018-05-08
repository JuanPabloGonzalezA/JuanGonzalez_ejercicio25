import numpy as np
import matplotlib.pyplot as plt

G=6.67408E-11
M=1.989E30

rm=np.sqrt(2.133679072387218E-01**2+3.727310311768299E-01**2+5.058864779204983E-02**2)*1.496E+11
vm=np.sqrt(1.892057222101034E-02**2+1.513838055059527E-02**2 +4.995475648824679E-04**2)*1.7315E+6
alpha=np.linspace(-2.5,2.5,300)
beta=(vm**2)/(rm**(1-alpha))

betabarra=G*M
proba=np.exp(-((betabarra-beta)**2/(2*np.var(beta))))

probaalpha=np.ones(len(alpha))/len(alpha)

probafinal=probaalpha*proba
plt.plot(beta,probafinal)
inmax=np.argmax(probafinal)
plt.scatter(beta[inmax],probafinal[inmax],label='alpha que maxima la proba '+str(alpha[inmax]))
plt.legend()
plt.savefig('probabilidad.jpg')

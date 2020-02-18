#code for plot in the presentation
#This code plots Bode plot for the given system function
from scipy import signal
import matplotlib.pyplot as plt
s1 = signal.lti([2], [1, 3,2])
w, mag, phase = signal.bode(s1)
plt.figure()

plt.semilogx(w, mag)
plt.grid()    # Bode magnitude plot
plt.figure()
plt.semilogx(w, phase) 
plt.grid() # Bode phase plot
plt.show()

# License
'''
Code by Gugulothu Yashwanth Naik
April 14,2020
Released under GNU GPL
'''

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from pylab import*


#Defining G(s)
Nr_G = np.poly1d([2])           #numerator of G(s),Here it is 2.
Dr_G= np.poly1d([1,3,2])       #denominator of G(s),Here it is s^2+3s+2


#Defining H(s)               
Nr_H= np.poly1d([50])          #numerator of H(s) , Here it is 50.
Dr_H= np.poly1d([1,1])         #denominator of H(s) , Here it is s+1

#Final open loop Transfer Function
Nr=(np.polymul(Nr_G,Nr_H))
Dr=(np.polymul(Dr_G,Dr_H))

s1 = signal.lti(Nr,Dr)
w, mag, phase = signal.bode(s1)

subplot(2,1,1)
plt.ylabel('Mag(deg)')
plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        # Bode Magnitude plot
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase plot')
#plt.axhline(y = -220.15,xmin=0,xmax= 0.8,color = 'r',linestyle='dashed')
#plt.axvline(x = 4.42,ymin=0.1,color='k',linestyle='dashed')
#plt.plot(4.42,-220.15,'o')
#plt.text(4.42,-220.15, '({}, {})'.format(4.42,-220.15))
plt.semilogx(w,phase)          # Bode phase plot
plt.grid() 


plt.show()


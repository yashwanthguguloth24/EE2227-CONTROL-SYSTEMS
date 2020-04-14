# License
'''
Code by Gugulothu Yashwanth Naik
April 14,2020
Released under GNU GPL
'''

#Bode plot using scipy in python
from scipy import signal
import matplotlib.pyplot as plt
from pylab import*

#Defining the transfer function 
#plug [2],[1,3,2] if your transfer function is (2/s^2+3s+2)
s1 = signal.lti([2],[1, 3,2])

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)

subplot(2,1,1)
#plt.xlabel('Frequency(rad/s)')
plt.ylabel('Mag(deg)')
plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        # Bode Magnitude plot
plt.grid() 

subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.grid() 




plt.show()



# change pin control.
ser.write(chr(13))
ser.write(chr(1))	 # write to Arduino to turn ON the LED
r = ser.read(7)

print r

time.sleep(1) 		# delay for 1 second

# change pin control.
ser.write(chr(13))
ser.write(chr(0))   # write to Arduino to turn OFF the LED
r = ser.read(7)

print r

time.sleep(1)


# writing to a file
file = open('Failed.py', 'w')
file.write('whatever')
file.close()
# .writelines(string[] lines)
# .readline(n)
# with open('filename') as file: #prevents need to close()


# plotting the final equations
import numpy as np
import matplotlib.pyplot as plt

# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

x = 0
y = 0

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(x, y, r'$\mu=100,\ \sigma=15$')
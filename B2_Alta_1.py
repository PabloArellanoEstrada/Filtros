#!/usr/bin/env python3
from pylab import *
import sys
import numpy as np
from apply_ltspice_filter import apply_ltspice_filter
import matplotlib.pyplot as plt
from scipy import signal

##################################################
##             VALORES INICIALES                ##
##################################################

R1o = 40
R2o = 100
C1o = 2e-6

R1 = R1o
R2 = R2o
C1 = C1o

##################################################
##            GRAFICAR BODE PYTHON
##################################################

fig = plt.figure(figsize=(11,6))
grid = plt.GridSpec (2,11,wspace=0.4, hspace=0.3)
fig.add_subplot(grid[0,:5])

num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menor 10%");

##################################################

R1=R1*1.056
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menor 5%");

##################################################

R1=R1*1.056
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R1")

##################################################

R1=R1*1.05
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mayor 5%");

##################################################

R1=R1*1.05
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mayor 10%");

plt.xlabel("Frecuencia(f)")
plt.ylabel("Magnitud (dB)")
plt.legend()
R1 = R1o


##################################################
##            GRAFICAR BODE PYTHON
##################################################


fig.add_subplot(grid[0,6:])

R2=R2*0.9
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R2=R2*1.056
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 5%");

##################################################

R2=R2*1.056
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R2")

##################################################

R2=R2*1.05
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 5%");

##################################################

R2=R2*1.05
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

plt.xlabel("Frecuencia(f)")
plt.ylabel("Magnitud (dB)")
plt.legend()
R2 = R2o

##################################################
##            GRAFICAR BODE PYTHON
##################################################

fig.add_subplot(grid[1,:5])

C1=C1*0.8
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 20%");

##################################################

C1=C1*1.125
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

C1=C1*1.11
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal C1")

##################################################

C1=C1*1.1
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

##################################################

C1=C1*1.1
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 20%");

plt.xlabel("Frecuencia(f)")
plt.ylabel("Magnitud (dB)")
plt.legend()




plt.show()



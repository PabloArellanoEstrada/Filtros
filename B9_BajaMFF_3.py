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
R3o = 200
R4o = 300
C1o = 2e-6
C2o = 1e-6
C3o = 2e-6

R1 = R1o
R2 = R2o
R3 = R3o
R4 = R4o
C1 = C1o
C2 = C2o
C3 = C3o

##################################################
##            GRAFICAR BODE PYTHON
##################################################

fig = plt.figure(figsize=(13,6))
plt.subplot(2,4,1)


num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menor 10%");

##################################################

R1=R1*1.056
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menor 5%");

##################################################

R1=R1*1.056
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R1")

##################################################

R1=R1*1.05
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mayor 5%");

##################################################

R1=R1*1.05
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mayor 10%");

plt.ylabel("Magnitud (dB)")
plt.legend()
R1 = R1o


##################################################
##            GRAFICAR BODE PYTHON
##################################################


plt.subplot(2,4,2)

R2=R2*0.9
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R2=R2*1.056
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 5%");

##################################################

R2=R2*1.056
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R2")

##################################################

R2=R2*1.05
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 5%");

##################################################

R2=R2*1.05
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

plt.legend()
R2 = R2o


##################################################
##            GRAFICAR BODE PYTHON
##################################################


plt.subplot(2,4,3)

R3=R3*0.9
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R3=R3*1.056
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 5%");

##################################################

R3=R3*1.056
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R3")

##################################################

R3=R3*1.05
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 5%");

##################################################

R3=R3*1.05
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

plt.legend()
R3=R3o

##################################################
##            GRAFICAR BODE PYTHON
##################################################


plt.subplot(2,4,4)

R4=R4*0.9
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R4=R4*1.056
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 5%");

##################################################

R4=R4*1.056
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R4")

##################################################

R4=R4*1.05
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 5%");

##################################################

R4=R4*1.05
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

plt.legend()
R4=R4o

##################################################
##            GRAFICAR BODE PYTHON
##################################################

plt.subplot(2,4,5)

C1=C1*0.8
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 20%");

##################################################

C1=C1*1.125
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

C1=C1*1.11
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal C1")

##################################################

C1=C1*1.1
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

##################################################

C1=C1*1.1
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 20%");

plt.xlabel("Frecuencia(f)")
plt.ylabel("Magnitud (dB)")
plt.legend()
C1 = C1o


##################################################
##            GRAFICAR BODE PYTHON
##################################################

plt.subplot(2,4,6)

C2=C2*0.8
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 20%");

##################################################

C2=C2*1.125
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

C2=C2*1.11
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal C2")

##################################################

C2=C2*1.1
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

##################################################

C2=C2*1.1
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 20%");

plt.xlabel("Frecuencia(f)")
plt.legend()
C2=C2o

##################################################
##            GRAFICAR BODE PYTHON
##################################################

plt.subplot(2,4,7)

C3=C3*0.8
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 20%");

##################################################

C3=C3*1.125
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

C3=C3*1.11
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal C3")

##################################################

C3=C3*1.1
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

##################################################

C3=C3*1.1
num1_MMF_low_3 = -1/(R1*R2*R3*C1*C2*C3)
den1_MMF_low_3 = 1
den2_MMF_low_3 = (1/(C1*R1)+1/(C1*R2)+1/(C2*R2)+1/(C2*R3)+1/(C2*R4))
den3_MMF_low_3 = (1/(C1*C2*R1*R2)+1/(C1*C2*R1*R3)+1/(C1*C2*R2*R3)+1/(C1*C2*R2*R4)+1/(C1*C2*R1*R4)+1/(C2*C3*R3*R4))
den4_MMF_low_4 = (R1+R2)/(R1*R2*R3*R4*C1*C2*C3)
system = signal.lti([num1_MMF_low_3], [den1_MMF_low_3 , den2_MMF_low_3, den3_MMF_low_3, den4_MMF_low_4 ])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 20%");

plt.xlabel("Frecuencia(f)")
plt.legend()
C3=C3o

plt.show()



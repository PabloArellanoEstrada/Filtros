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
C1o = 2e-6
C2o = 1e-6

R1 = R1o
R2 = R2o
R3 = R3o
C1 = C1o
C2 = C2o


##################################################
##            GRAFICAR BODE PYTHON
##################################################

fig = plt.figure(figsize=(11,6))
plt.subplot(2,3,1)


num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menor 10%");

##################################################

R1=R1*1.056
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menor 5%");

##################################################

R1=R1*1.056
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R1")

##################################################

R1=R1*1.05
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mayor 5%");

##################################################

R1=R1*1.05
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
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


plt.subplot(2,3,2)

R2=R2*0.9
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R2=R2*1.056
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 5%");

##################################################

R2=R2*1.056
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R2")

##################################################

R2=R2*1.05
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 5%");

##################################################

R2=R2*1.05
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

plt.legend()
R2 = R2o


##################################################
##            GRAFICAR BODE PYTHON
##################################################


plt.subplot(2,3,3)

R3=R3*0.9
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R3=R3*1.056
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 5%");

##################################################

R3=R3*1.056
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R3")

##################################################

R3=R3*1.05
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 5%");

##################################################

R3=R3*1.05
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

plt.legend()
R3=R3o

##################################################
##            GRAFICAR BODE PYTHON
##################################################

plt.subplot(2,3,4)

C1=C1*0.8
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 20%");

##################################################

C1=C1*1.125
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

C1=C1*1.11
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal C1")

##################################################

C1=C1*1.1
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

##################################################

C1=C1*1.1
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
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

plt.subplot(2,3,5)

C2=C2*0.8
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 20%");

##################################################

C2=C2*1.125
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

C2=C2*1.11
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal C2")

##################################################

C2=C2*1.1
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

##################################################

C2=C2*1.1
num_MMF_low_2 = -(1/(R1*R3*C2*C1))
den1_MMF_low_2 = 1
den2_MMF_low_2 = (1/R1+1/R3+1/R2)/C2
den3_MMF_low_2 = 1/(R3*R2*C2*C1)
system = signal.lti([num_MMF_low_2], [den1_MMF_low_2, den2_MMF_low_2, den3_MMF_low_2])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 20%");

plt.xlabel("Frecuencia(f)")
plt.legend()
C2=C2o

plt.show()



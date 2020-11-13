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

R1o = 1e3
R2o = 1.5e3
R3o = 2e3
R4o = 3e3
R5o = 2.5e3
R6o = 1e3
C1o = 200e-9
C2o = 150e-9

R1 = R1o
R2 = R2o
R3 = R3o
R4 = R4o
R5 = R5o
R6 = R6o
C1 = C1o
C2 = C2o


##################################################
##            GRAFICAR BODE PYTHON
##################################################

fig = plt.figure(figsize=(13,6))
plt.subplot(2,4,1)

R1=R1*0.9
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menor 10%");

##################################################

R1=R1*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menor 5%");

##################################################

R1=R1*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R1")

##################################################

R1=R1*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mayor 5%");

##################################################

R1=R1*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
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
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R2=R2*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 5%");

##################################################

R2=R2*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R2")

##################################################

R2=R2*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 5%");

##################################################

R2=R2*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
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
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R3=R3*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 5%");

##################################################

R3=R3*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R3")

##################################################

R3=R3*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 5%");

##################################################

R3=R3*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
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
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R4=R4*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 5%");

##################################################

R4=R4*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R4")

##################################################

R4=R4*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 5%");

##################################################

R4=R4*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
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

R5=R5*0.9
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 20%");

##################################################

R5=R5*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R5=R5*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R5")

##################################################

R5=R5*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

##################################################

R5=R5*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 20%");

plt.xlabel("Frecuencia(Hz)")
plt.ylabel("Magnitud (dB)")
plt.legend()
R5=R5o


##################################################
##            GRAFICAR BODE PYTHON
##################################################

plt.subplot(2,4,6)

R6=R6*0.9
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 20%");

##################################################

R6=R6*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

R6=R6*1.056
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal R6")

##################################################

R6=R6*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

##################################################

R6=R6*1.05
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 20%");

plt.xlabel("Frecuencia(Hz)")
plt.legend()
R6=R6o

##################################################
##            GRAFICAR BODE PYTHON
##################################################

plt.subplot(2,4,7)

C1=C1*0.8
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 20%");

##################################################

C1=C1*1.125
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

C1=C1*1.11
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal C1")

##################################################

C1=C1*1.1
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

##################################################

C1=C1*1.1
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 20%");

plt.xlabel("Frecuencia(Hz)")
plt.legend()
C1=C1o

##################################################
##            GRAFICAR BODE PYTHON
##################################################

plt.subplot(2,4,8)

C2=C2*0.8
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 20%");

##################################################

C2=C2*1.125
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Menos 10%");

##################################################

C2=C2*1.11
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Nominal C2")

##################################################

C2=C2*1.1
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 10%");

##################################################

C2=C2*1.1
num1_Notch_Activo = 1
num2_Notch_Activo = (R6-R5)/(R1*R6*C1)
num3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
den1_Notch_Activo = 1
den2_Notch_Activo = (R1+R2)/(R1*R2*C1)
den3_Notch_Activo = R5/(R3*R4*R6*C1*C2)
system = signal.lti([num1_Notch_Activo, num2_Notch_Activo, num3_Notch_Activo], [den1_Notch_Activo, den2_Notch_Activo, den3_Notch_Activo])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag, label="Mas 20%");

plt.xlabel("Frecuencia(Hz)")
plt.legend()
C2=C2o

plt.show()



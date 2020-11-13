#!/usr/bin/env python3
from pylab import *
import sys
import numpy as np
from apply_ltspice_filter import apply_ltspice_filter
import matplotlib.pyplot as plt
from scipy import signal

frec = float(input("Ingrese la frecuencia en Rad/seg de la función para el filto: "))
w_frec = float
w_frec = 2*3.1416*frec

##################################################
##             INYECTAR SENAL ESCALON           ##
##################################################

# our samples shall be 100 ms wide
sample_width=1.5e-3
# time step between samples: 0.1 ms
delta_t=1e-5
samples = int(sample_width/delta_t)

time = np.linspace(0,sample_width,samples)
signal_a = 1*((time > 0)) 

if sys.platform == "darwin":
  """ In order for the command /Applications/LTspice.app/Contents/MacOS/LTspice -b
A2_Alta_1.cir to work, a netlist file is required."""
  file_extension = "cir"
else:
  file_extension = "asc"

##################################################
##             VALORES INICIALES                ##
##################################################

R1 = 1e3
R2 = 2e3
C1 = 200e-9

##################################################
##               ENVIAR A LTSPICE
##################################################

# all values in SI units
configuration_1 = {
  "C1":C1,
  "R1":R1,
  "R2":R2
}

dummy, signal_b1 = apply_ltspice_filter(
      f"A2_Alta_1.{file_extension}",
      time, signal_a,
      params=configuration_1
      )


##################################################
##              GRAFICAR ESCALON LTSPICE
##################################################
  
fig = plt.figure(figsize=(11,6))
grid = plt.GridSpec (2,10,wspace=0.4, hspace=0.3)
fig.add_subplot(grid[0:,:5])
plt.plot(time,signal_a, label="signal")
plt.plot(time,signal_b1, label="Ltspice-real")
plt.xlabel("time (s)")
plt.ylabel("voltage (V)")
plt.ylim((-3,1.5))
plt.grid(True)


##################################################
##              GRAFICAR ESCALON PYTHON
##################################################

num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1
lti = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
time, y = signal.step(lti)
plt.plot(time, y, label="Phyton-ideal" )
plt.legend()


##################################################
##             INYECTAR SENAL SENO
##################################################

# our samples shall be 100 ms wide
sample_width=1e-3
# time step between samples: 0.1 ms
delta_t=1e-7
samples = int(sample_width/delta_t)

time = np.linspace(0,sample_width,samples)
signal_a = np.sin(w_frec*time) ## senal seno

if sys.platform == "darwin":
  """ In order for the command /Applications/LTspice.app/Contents/MacOS/LTspice -b
A2_Alta_1.cir to work, a netlist file is required."""
  file_extension = "cir"
else:
  file_extension = "asc"


##################################################
##                 ENVIAR LTSPICE
##################################################

# all values in SI units
configuration_1 = {
  "C1":C1,
  "R1":R1,
  "R2":R2
}

dummy, signal_b1 = apply_ltspice_filter(
      f"A2_Alta_1.{file_extension}",
      time, signal_a,
      params=configuration_1
      )

##################################################
##               GRAFICAR SENO LTSPICE
##################################################


fig.add_subplot(grid[0,6:])
plt.plot(time,signal_a, label="signal")
plt.plot(time,signal_b1, label="Ltspice-real")
plt.xlabel("time (s)")
plt.ylabel("voltage (V)")
plt.ylim((-3,3))
plt.grid(True)
plt.legend()



##################################################
##            GRAFICAR BODE PYTHON
##################################################

fig.add_subplot(grid[1,6:])
num1_alta_1 = (-R2*C1)
num2_alta_1 = 0
den1_alta_1 = (R1*C1)
den2_alta_1 = 1

system = signal.lti([num1_alta_1, num2_alta_1], [den1_alta_1, den2_alta_1])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag);
plt.xlabel("Frecuencia(Hz)")
plt.ylabel("Magnitud (dB)")
plt.show()



#!/usr/bin/env python3
from pylab import *
import sys
import numpy as np
from apply_ltspice_filter import apply_ltspice_filter
import matplotlib.pyplot as plt
from scipy import signal

##################################################
##             INYECTAR SENAL ESCALON           ##
##################################################

# our samples shall be 100 ms wide
sample_width=2e-3
# time step between samples: 0.1 ms
delta_t=1e-5
samples = int(sample_width/delta_t)

time = np.linspace(0,sample_width,samples)
signal_a = 1*((time > 0)) 

if sys.platform == "darwin":
  """ In order for the command /Applications/LTspice.app/Contents/MacOS/LTspice -b
A5_BajaSK_3.cir to work, a netlist file is required."""
  file_extension = "cir"
else:
  file_extension = "asc"

##################################################
##             VALORES INICIALES                ##
##################################################

R1 = 40
R2 = 100
R3 = 200
C1 = 2e-6
C2 = 1e-6
C3 = 3e-6

##################################################
##               ENVIAR A LTSPICE
##################################################

# all values in SI units
configuration_1 = {
  "C1":C1,
  "C2":C2,
  "C3":C3,
  "R1":R1,
  "R2":R2,
  "R3":R3
}

dummy, signal_b1 = apply_ltspice_filter(
      f"A5_BajaSK_3.{file_extension}",
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
plt.ylim((-0.5,1.5))
plt.grid(True)


##################################################
##              GRAFICAR ESCALON PYTHON
##################################################

num1_sk_low_3 = 1/(R1*R2*R3*C1*C2*C3)
den1_sk_low_3 = 1
den2_sk_low_3 = (1/(C3*R1)+1/(C3*R2)+1/(C1*R3)+1/(C1*R2))
den3_sk_low_3 = (1/(C1*C2*R2*R3)+1/(C3*C1*R2*R3)+1/(C3*C1*R1*R3)+1/(C3*C1*R1*R2))
den4_sk_low_3 = 1/(R1*R2*R3*C1*C2*C3)
lti = signal.lti([num1_sk_low_3], [den1_sk_low_3, den2_sk_low_3 , den3_sk_low_3, den4_sk_low_3])
time, y = signal.step(lti)
plt.plot(time, y, label="Phyton-ideal" )
plt.legend()


##################################################
##             INYECTAR SENAL SENO
##################################################

# our samples shall be 100 ms wide
sample_width=2e-3
# time step between samples: 0.1 ms
delta_t=1e-5
samples = int(sample_width/delta_t)

time = np.linspace(0,sample_width,samples)
signal_a = np.sin(11158*time) ## senal seno

if sys.platform == "darwin":
  """ In order for the command /Applications/LTspice.app/Contents/MacOS/LTspice -b
A5_BajaSK_3.cir to work, a netlist file is required."""
  file_extension = "cir"
else:
  file_extension = "asc"


##################################################
##                 ENVIAR LTSPICE
##################################################

# all values in SI units
configuration_1 = {
  "C1":C1,
  "C2":C2,
  "C3":C3,
  "R1":R1,
  "R2":R2,
  "R3":R3
}

dummy, signal_b1 = apply_ltspice_filter(
      f"A5_BajaSK_3.{file_extension}",
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
plt.ylim((-1.5,1.5))
plt.grid(True)
plt.legend()


##################################################
##            GRAFICAR BODE PYTHON
##################################################

fig.add_subplot(grid[1,6:])
num1_sk_low_3 = 1/(R1*R2*R3*C1*C2*C3)
den1_sk_low_3 = 1
den2_sk_low_3 = (1/(C3*R1)+1/(C3*R2)+1/(C1*R3)+1/(C1*R2))
den3_sk_low_3 = (1/(C1*C2*R2*R3)+1/(C3*C1*R2*R3)+1/(C3*C1*R1*R3)+1/(C3*C1*R1*R2))
den4_sk_low_3 = 1/(R1*R2*R3*C1*C2*C3)
system = signal.lti([num1_sk_low_3], [den1_sk_low_3, den2_sk_low_3 , den3_sk_low_3, den4_sk_low_3])
f = logspace(1, 5)
w = 2 * pi * f
w, mag, phase = signal.bode(system,w)
plt.semilogx(f, mag);
plt.show()


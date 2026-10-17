sr = 44100
ksmps = 32
nchnls = 2
0dbfs = 1.0

instr 1
  iamp = p4
  ifreq = p5
  aenv madsr 0.05, 0.2, 0.7, 0.5
  asig poscil iamp * aenv, ifreq
  areverb freeverb asig, asig, 0.8, 0.5
  outs asig + areverb * 0.3, asig + areverb * 0.3
endin

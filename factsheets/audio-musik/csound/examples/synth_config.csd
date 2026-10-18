<CsoundSynthesizer>
<CsOptions>
-o output.wav -W
</CsOptions>
<CsInstruments>
sr = 44100
ksmps = 32
nchnls = 2
0dbfs = 1.0

instr 1
  iamp = p4
  ifreq = p5
  aenv madsr 0.01, 0.1, 0.8, 0.3
  asrc vco2 iamp, ifreq, 0
  afilt moogladder asrc, 1200, 0.4
  outs afilt * aenv, afilt * aenv
endin
</CsInstruments>
<CsScore>
i 1 0 1.5 0.4 220
i 1 1.5 1.5 0.4 277.18
i 1 3.0 2.0 0.4 329.63
e
</CsScore>
</CsoundSynthesizer>

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
  aenv line 1, p3, 0
  asig poscil iamp * aenv, ifreq
  outs asig, asig
endin
</CsInstruments>
<CsScore>
i 1 0 2 0.5 440
i 1 2 2 0.5 554.37
i 1 4 2 0.5 659.25
e
</CsScore>
</CsoundSynthesizer>

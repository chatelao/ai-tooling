;nyquist plug-in
;version 4
;type generate
;name "440Hz Sine Generator"
;action "Generating 440Hz Sine Wave..."
;control freq "Frequency (Hz)" float "" 440 100 10000
;control dur "Duration (seconds)" float "" 1.0 0.1 30.0

(hz-osc freq)

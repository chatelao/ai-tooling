;nyquist plug-in
;version 4
;type process
;name "Batch Converter"
;action "Processing audio for batch conversion..."

;; Convert audio signal amplitude and apply highpass filter
(defun process-audio (sig)
  (highpass8 sig 80.0))

(if (arrayp *track*)
    (vector (process-audio (aref *track* 0))
            (process-audio (aref *track* 1)))
    (process-audio *track*))

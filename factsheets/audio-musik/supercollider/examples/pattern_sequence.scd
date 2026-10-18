// SuperCollider Pattern Sequence Definition using Pbind
Pbind(
    \instrument, \subtractiveLead,
    \degree, Pseq([0, 2, 4, 7, 9, 7, 4, 2], inf),
    \dur, 0.25,
    \amp, 0.2,
    \cutoff, Pwhite(500, 3000, inf)
);

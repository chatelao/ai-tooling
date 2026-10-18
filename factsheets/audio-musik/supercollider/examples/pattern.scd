// SuperCollider Example 3: Algorithmic pattern sequence using Pbind
Pbind(
    \instrument, \default,
    \degree, Pseq([0, 2, 4, 7, 9, 7, 4, 2], inf),
    \dur, 0.25,
    \amp, 0.3
);

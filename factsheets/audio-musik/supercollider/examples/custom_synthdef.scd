// SuperCollider SynthDef Definition: Subtractive Synth with Resonant Filter
SynthDef(\subtractiveLead, { |out=0, freq=440, gate=1, amp=0.2, cutoff=1200, rq=0.3|
    var osc, filter, env;
    env = EnvGen.kr(Env.adsr(0.01, 0.2, 0.6, 0.5), gate, doneAction: 2);
    osc = Saw.ar([freq, freq * 1.005]);
    filter = RLPF.ar(osc, cutoff, rq);
    Out.ar(out, filter * env * amp);
}).add;

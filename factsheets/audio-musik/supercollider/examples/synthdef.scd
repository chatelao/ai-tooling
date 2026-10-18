// SuperCollider Example 2: Reusable SynthDef with resonant low-pass filter
SynthDef(\resonantSaw, { |out = 0, freq = 220, cutoff = 800, rq = 0.2, amp = 0.5, gate = 1|
    var sig = Saw.ar([freq, freq * 1.005]);
    var env = EnvGen.kr(Env.adsr(0.01, 0.2, 0.6, 0.3), gate, doneAction: 2);
    var filtered = RLPF.ar(sig, cutoff, rq);
    Out.ar(out, filtered * env * amp);
}).writeDefFile("factsheets/audio-musik/supercollider/examples");

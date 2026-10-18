// SuperCollider Example 1: Multi-oscillator ambient drone synthesis
// Renderable via Non-Realtime (NRT) Score synthesis

var synthDef = SynthDef(\ambientDrone, { |out = 0, freq = 110, amp = 0.4, gate = 1|
    var osc1 = Saw.ar(freq * [0.99, 1.01]) * 0.3;
    var osc2 = SinOsc.ar(freq * 0.5) * 0.4;
    var filter = LPF.ar(osc1 + osc2, SinOsc.kr(0.2).range(300, 1200));
    var env = EnvGen.kr(Env.asr(0.5, 1, 0.5), gate, doneAction: 2);
    Out.ar(out, filter * env * amp);
});

var score = Score([
    [0.0, [\d_recv, synthDef.asBytes]],
    [0.0, [\s_new, \ambientDrone, 1000, 0, 0, \freq, 110, \amp, 0.3]],
    [2.5, [\n_set, 1000, \gate, 0]],
    [3.0, [\c_set, 0, 0]]
]);

score.recordNRT(
    outputFilePath: "factsheets/audio-musik/supercollider/examples/rendered_drone.wav".standardizePath,
    headerFormat: "WAV",
    sampleFormat: "int16",
    options: ServerOptions.new.numOutputBusChannels_(2),
    duration: 3.0,
    action: { "Drone rendering complete.".postln; 0.exit; }
);

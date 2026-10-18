// SuperCollider Non-Realtime Synthesis (NRT) Script: Generative Drone
var score, synthDef, outPath;

outPath = if(thisProcess.nowExecutingPath.notNil) {
    thisProcess.nowExecutingPath.dirname +/+ "rendered_buffer.wav"
} {
    "examples/rendered_buffer.wav"
};

synthDef = SynthDef(\drone, { |out=0, freq=110, amp=0.3, dur=3.0|
    var sig, env;
    env = EnvGen.kr(Env.sine(dur, amp), doneAction: 2);
    sig = SinOsc.ar([freq, freq * 1.5, freq * 2.01]) * env;
    sig = LPF.ar(sig, 800);
    Out.ar(out, Splay.ar(sig));
});

score = Score([
    [0.0, [\d_recv, synthDef.asBytes]],
    [0.1, [\s_new, \drone, 1000, 0, 0, \freq, 110, \amp, 0.4, \dur, 2.5]],
    [0.5, [\s_new, \drone, 1001, 0, 0, \freq, 164.81, \amp, 0.3, \dur, 2.0]],
    [3.0, [\c_set, 0, 0]]
]);

score.recordNRT(
    outputFilePath: outPath,
    headerFormat: "WAV",
    sampleFormat: "int16",
    options: ServerOptions.new.numOutputBusChannels_(2),
    action: {
        "Generative Drone NRT rendering complete.".postln;
        0.exit;
    }
);

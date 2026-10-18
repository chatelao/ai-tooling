// SuperCollider Example 4: Server options and audio setup configuration
s = Server.local;
s.options.numOutputBusChannels = 2;
s.options.numInputBusChannels = 2;
s.options.sampleRate = 44100;
s.options.blockSize = 64;
s.options.memSize = 8192 * 16;
"Server options configured successfully.".postln;

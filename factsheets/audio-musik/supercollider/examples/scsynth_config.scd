// SuperCollider Server Configuration Options
s = Server.default;
s.options.numOutputBusChannels = 2;
s.options.numInputBusChannels = 2;
s.options.sampleRate = 44100;
s.options.blockSize = 64;
s.options.numBuffers = 1024;
s.options.memSize = 8192 * 16;

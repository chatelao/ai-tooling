-- WirePlumber Lua Configuration Script for PipeWire Virtual Audio Sink
-- Defines a custom virtual stereo audio sink node for routing and DSP processing.

virtual_sink_script = {
  properties = {
    ["node.name"] = "Virtual_Stereo_Sink",
    ["node.description"] = "PipeWire Headless Virtual Audio Output Sink",
    ["media.class"] = "Audio/Sink",
    ["audio.channels"] = 2,
    ["audio.position"] = "FL,FR",
    ["audio.rate"] = 48000,
    ["factory.name"] = "support.null-audio-sink"
  }
}

function create_virtual_sink()
  local node = Node("adapter", virtual_sink_script.properties)
  node:activate()
  Log.info("Created PipeWire virtual audio sink node")
end

create_virtual_sink()

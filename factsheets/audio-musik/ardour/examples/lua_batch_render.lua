-- Ardour Lua Batch Export Script
-- Executable via Ardour Lua engine for automated session processing

print("Ardour Lua Engine Initialized")
print("Engine Version: " .. ARDOUR.LuaAPI.version())

local session = Session
if session then
    print("Session Name: " .. session:name())
    print("Sample Rate: " .. session:nominal_sample_rate())
else
    print("Batch Mode: No active session open, running standalone validation.")
end

# Connect to a local OpenOCD server
target extended-remote localhost:3333
monitor reset halt
load
breakpoint main
continue

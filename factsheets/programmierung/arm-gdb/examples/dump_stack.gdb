# GDB script to dump the stack
define dump_stack
  echo Stack Trace:\n
  bt
  echo \nRegisters:\n
  info registers
  echo \nStack Memory (top 16 words):\n
  x/16xw $sp
end

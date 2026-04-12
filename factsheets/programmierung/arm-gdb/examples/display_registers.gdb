# Display common registers
define show_arm_regs
  info registers r0 r1 r2 r3 r4 r5 r6 r7
  info registers sp lr pc cpsr
end
document show_arm_regs
  Displays R0-R7 and special registers for ARM.
end

# Breakpoint with logging
break main
commands
  silent
  printf "Reached main\n"
  continue
end

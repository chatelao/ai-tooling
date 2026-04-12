# Makefile for Tang Nano 4K example
# Requires Gowin EDA or open-source Apicula/yosys/nextpnr-gowin

BOARD=tangnano4k
BITSTREAM=project.fs

flash:
	openFPGALoader -b $(BOARD) $(BITSTREAM)

flash_sram:
	openFPGALoader -b $(BOARD) -m $(BITSTREAM)

clean:
	rm -f $(BITSTREAM)

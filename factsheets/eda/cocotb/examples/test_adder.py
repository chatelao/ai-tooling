import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def adder_basic_test(dut):
    """Test for 5 + 10"""
    dut.a.value = 5
    dut.b.value = 10
    await Timer(2, units="ns")
    assert dut.q.value == 15, f"Adder result is incorrect: {dut.q.value} != 15"

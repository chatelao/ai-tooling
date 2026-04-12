from cocotb.runner import get_runner
import os

def test_adder_runner():
    sim = "icarus"
    proj_path = os.path.abspath(os.path.dirname(__file__))
    verilog_sources = [os.path.join(proj_path, "adder.v")]

    runner = get_runner(sim)
    runner.build(
        verilog_sources=verilog_sources,
        hdl_toplevel="adder",
        always=True,
    )

    runner.test(hdl_toplevel="adder", test_module="test_adder")

if __name__ == "__main__":
    test_adder_runner()

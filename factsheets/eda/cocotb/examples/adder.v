module adder (
    input [3:0] a,
    input [3:0] b,
    output [4:0] q
);
    assign q = a + b;
endmodule

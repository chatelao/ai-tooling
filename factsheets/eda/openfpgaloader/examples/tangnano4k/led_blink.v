module led_blink (
    input clk,
    output reg led
);
    reg [23:0] counter;

    always @(posedge clk) begin
        counter <= counter + 1'b1;
        if (counter == 24'd13500000) begin // 27MHz / 2
            counter <= 0;
            led <= ~led;
        end
    end
endmodule

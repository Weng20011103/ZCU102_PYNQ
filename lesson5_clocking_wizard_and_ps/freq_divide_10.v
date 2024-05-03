module freq_div_10(
    input clk, reset,
    output reg clk_div_10
);
    // Define a 4-bit counter to keep track of the division.
    reg [3:0]counter4;

    // This always block triggers on the rising edge of the 'clk' signal or a low-level 'reset' signal.
    always @(posedge clk or negedge reset) begin
        // If 'reset' is active (low), reset the counter to zero.
        if (!reset)
            counter4 <= 4'b0;
        // If the counter reaches 4, reset it to zero.
        else if (counter4 == 4'd4)
            counter4 <= 4'b0;
        // If none of the above conditions are met, increment the counter by 1.
        else
            counter4 <= counter4 + 1'b1;
    end

    // This always block also triggers on the rising edge of 'clk' or a low-level 'reset' signal.
    always @(posedge clk or negedge reset) begin
        // If 'reset' is active (low), the output signal 'clt_div_10' follows the 'clk' input.
        if (!reset)
            clk_div_10 <= 1'b0;
        // If the counter reaches 4, toggle the output signal 'clt_div_10'.
        else if (counter4 == 4'd4)
            clk_div_10 <= ~clk_div_10;
        // If none of the above conditions are met, the output signal 'clt_div_10' follows the 'clk' input.
        else
            clk_div_10 <= clk_div_10;
    end

endmodule

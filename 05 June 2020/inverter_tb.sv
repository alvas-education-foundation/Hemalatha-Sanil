// Code your testbench here
// or browse Examples
`timescale 1ns/1ps

module testbench();
  reg a1;
  wire y1;
  inverter inv1(a1,y1);
  
  initial begin
    a1=1'b1;
    $display("a=%b",a1);
  end
endmodule
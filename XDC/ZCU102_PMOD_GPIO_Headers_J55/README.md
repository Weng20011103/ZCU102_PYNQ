# ZCU102 PMOD GPIO Headers J55  
參考[UG1182 - ZCU102 Evaluation Board User Guide (UG1182) (v1.7)](https://docs.amd.com/v/u/en-US/ug1182-zcu102-eval-bd)的第 74 頁、75 頁。  
  
`PMOD GPIO Headers J55`位置為`UG1182`文檔中的`Figure 2-1`中的`19`。  
![PMOD.png](PMOD.png "PMOD.png")  
  
`UG1182`文檔中的`Figure 3-29`有`J55`的原理圖。  
  
`Table 3-31`給出了`PMOD`的腳位和電壓標準`I/O Standard`。  
|ZCU102 腳位|原理圖中名稱|I/O Standard|
|:--:|:--:|:--:|
|A20|PMOD0_0|LVCMOS33|
|B20|PMOD0_1|LVCMOS33|
|A22|PMOD0_2|LVCMOS33|
|A21|PMOD0_3|LVCMOS33|
|B21|PMOD0_4|LVCMOS33|
|C21|PMOD0_5|LVCMOS33|
|C22|PMOD0_6|LVCMOS33|
|D21|PMOD0_7|LVCMOS33|
  
# XDC 範例  
```text
set_property PACKAGE_PIN A20      [get_ports "PMOD0_0"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "PMOD0_0"] ;
set_property PACKAGE_PIN B20      [get_ports "PMOD0_1"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "PMOD0_1"] ;
set_property PACKAGE_PIN A22      [get_ports "PMOD0_2"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "PMOD0_2"] ;
set_property PACKAGE_PIN A21      [get_ports "PMOD0_3"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "PMOD0_3"] ;
set_property PACKAGE_PIN B21      [get_ports "PMOD0_4"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "PMOD0_4"] ;
set_property PACKAGE_PIN C21      [get_ports "PMOD0_5"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "PMOD0_5"] ;
set_property PACKAGE_PIN C22      [get_ports "PMOD0_6"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "PMOD0_6"] ;
set_property PACKAGE_PIN D21      [get_ports "PMOD0_7"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "PMOD0_7"] ;
```
  
# 參考連結  
[Zynq UltraScale+ MPSoC ZCU102 Evaluation Kit](https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html)  
[UG1182 - ZCU102 Evaluation Board User Guide (UG1182) (v1.7)](https://docs.amd.com/v/u/en-US/ug1182-zcu102-eval-bd)  
  


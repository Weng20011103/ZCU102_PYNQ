# ZCU102 GPIO LED  
參考[UG1182 - ZCU102 Evaluation Board User Guide (UG1182) (v1.7)](https://docs.amd.com/v/u/en-US/ug1182-zcu102-eval-bd)的第 77 頁。  
  
`ZCU102`有 8 個`GPIO_LED`，`GPIO_LED`位置為`UG1182`文檔中的`Figure 2-1`中的`21`。  
  
`UG1182`文檔中的`Figure 3-32`有`GPIO LEDs`的原理圖。  
  
由原理圖可知，`GPIO_LED`必須要給`高電位`才能點亮`LED`。給`低電位`不會點亮`LED`。  
  
`Table 3-33`給出了`GPIO LEDs`的腳位和電壓標準`I/O Standard`。  
|ZCU102 腳位|原理圖中名稱|I/O Standard|
|:--:|:--:|:--:|
|AG14|GPIO_LED_0|LVCMOS33|
|AF13|GPIO_LED_1|LVCMOS33|
|AE13|GPIO_LED_2|LVCMOS33|
|AJ14|GPIO_LED_3|LVCMOS33|
|AJ15|GPIO_LED_4|LVCMOS33|
|AH13|GPIO_LED_5|LVCMOS33|
|AH14|GPIO_LED_6|LVCMOS33|
|AL12|GPIO_LED_7|LVCMOS33|
  
# XDC 範例  
```text
set_property PACKAGE_PIN AG14     [get_ports "GPIO_LED_0"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "GPIO_LED_0"] ;
set_property PACKAGE_PIN AF13     [get_ports "GPIO_LED_1"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "GPIO_LED_1"] ;
set_property PACKAGE_PIN AE13     [get_ports "GPIO_LED_2"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "GPIO_LED_2"] ;
set_property PACKAGE_PIN AJ14     [get_ports "GPIO_LED_3"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "GPIO_LED_3"] ;
set_property PACKAGE_PIN AJ15     [get_ports "GPIO_LED_4"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "GPIO_LED_4"] ;
set_property PACKAGE_PIN AH13     [get_ports "GPIO_LED_5"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "GPIO_LED_5"] ;
set_property PACKAGE_PIN AH14     [get_ports "GPIO_LED_6"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "GPIO_LED_6"] ;
set_property PACKAGE_PIN AL12     [get_ports "GPIO_LED_7"] ;
set_property IOSTANDARD  LVCMOS33 [get_ports "GPIO_LED_7"] ;
```

# 參考連結  
[Zynq UltraScale+ MPSoC ZCU102 Evaluation Kit](https://www.xilinx.com/products/boards-and-kits/ek-u1-zcu102-g.html)  
[UG1182 - ZCU102 Evaluation Board User Guide (UG1182) (v1.7)](https://docs.amd.com/v/u/en-US/ug1182-zcu102-eval-bd)  
  

